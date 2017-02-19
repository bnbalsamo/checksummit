from hashlib import new

from flask import Blueprint, request
from flask_restful import Resource, Api, reqparse

from nothashes import crc32, adler32

BLUEPRINT = Blueprint('checksummit', __name__)

BLUEPRINT.config = {
    'DISALLOWED_ALGOS': [],
    'BUFF': 1024*1000*8
}


API = Api(BLUEPRINT)


def get_hasher_obj(x):
    additional_algos = {
        "crc32": crc32,
        "adler32": adler32
    }
    if x in additional_algos:
        return additional_algos[x]()
    else:
        return new(x)


def produce_checksums(f, hashers):
    data = f.read(BLUEPRINT.config['BUFF'])
    while data:
        for x in hashers:
            x.update(data)
        data = f.read()
    return {x.name: x.hexdigest() for x in hashers}


class FileIn(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('hash', action="append")
        args = parser.parse_args()
        if len(request.files) < 1:
            return {"message": "No file(s) detected."}
        if len(request.files) > 1:
            return {"message": "Too many files"}
        if len(args['hash']) < 1:
            return {"message": "No hashes detected"}
        hashers = []
        for x in args['hash']:
            if x in BLUEPRINT.config['DISALLOWED_ALGOS']:
                return {"message": "Disallowed algorithm included. ({})".format(x)}
            try:
                h = get_hasher_obj(x)
                hashers.append(h)
            except:
                return {"message": "Unsupported algorithm included ({}".format(x)}

        file_key = [x for x in request.files.keys()][0]
        return produce_checksums(request.files[file_key], hashers)


@BLUEPRINT.record
def handle_configs(setup_state):
    app = setup_state.app
    BLUEPRINT.config.update(app.config)

API.add_resource(FileIn, '/')
