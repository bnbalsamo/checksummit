from hashlib import new, algorithms_available

from flask import Blueprint, request
from flask_restful import Resource, Api, reqparse

from nothashes import crc32, adler32

additional_algos = ["crc32", "adler32"]
additional_algos = set(additional_algos)
disallowed_algos = []
disallowed_algos = set(disallowed_algos)


BLUEPRINT = Blueprint('checksummit', __name__)

API = Api(BLUEPRINT)


def produce_checksums(f, hashers):
    data = f.read()
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
        hashers = []
        for x in args['hash']:
            if x in disallowed_algos:
                return {"message": "Disallowed algorithm included. ({})".format(x)}
            elif x not in algorithms_available and x not in additional_algos:
                return {"message": "Algorithm not supported. ({})".format(x)}
            elif x == "crc32":
                hashers.append(crc32())
            elif x == "adler32":
                hashers.append(adler32())
            else:
                hashers.append(new(x))

        if len(request.files) < 1:
                return {"message": "No file(s) detected."}

        return {request.files[x].name: produce_checksums(request.files[x], hashers) for x in request.files}


API.add_resource(FileIn, '/')
