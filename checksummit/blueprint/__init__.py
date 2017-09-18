"""
checksummit
"""
import logging

from flask import Blueprint, jsonify, request
from flask_restful import Resource, Api, reqparse

from .exceptions import Error

from nothashes import crc32, adler32
import multihash
# Add crc32 and adler32 to the multihash interface
multihash.additional_hashers.add(crc32)
multihash.additional_hashers.add(adler32)

__author__ = "Brian Balsamo"
__email__ = "brian@brianbalsamo.com"
__version__ = "0.2.0"


BLUEPRINT = Blueprint('checksummit', __name__)

BLUEPRINT.config = {
    'BUFF': 1024 * 1000
}

API = Api(BLUEPRINT)

log = logging.getLogger(__name__)


@BLUEPRINT.errorhandler(Error)
def handle_errors(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


class Version(Resource):
    def get(self):
        return {"version": __version__}


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
        for n in args['hash']:
            if n in BLUEPRINT.config['DISALLOWED_ALGOS']:
                return {"message": "Disallowed algorithm included. ({})".format(n)}
            try:
                hashers.append(
                    multihash.new(n)
                )
            except:
                return {"message": "Unsupported algorithm included ({}".format(n)}

        file_key = [x for x in request.files.keys()][0]
        h = multihash.MultiHash.from_flo(
            request.files[file_key],
            hashers=hashers,
            chunksize=BLUEPRINT.config['BUFF']
        )
        return h.hexdigest()


class TextIn(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('hash', action="append")
        parser.add_argument('text')
        args = parser.parse_args()
        if len(args['hash']) < 1:
            return {"message": "No hashes detected"}

        hashers = []
        for n in args['hash']:
            if n in BLUEPRINT.config['DISALLOWED_ALGOS']:
                return {"message": "Disallowed algorithm included. ({})".format(n)}
            try:
                hashers.append(
                    multihash.new(n)
                )
            except:
                return {"message": "Unsupported algorithm included ({}".format(n)}

        h = multihash.MultiHash(
            args['text'].encode(),
            hashers=hashers
        )
        return h.hexdigest()


class AvailableAlgos(Resource):
    def get(self):
        return list(
            multihash.algorithms_available().difference(set(BLUEPRINT.config['DISALLOWED_ALGOS']))
        )


@BLUEPRINT.record
def handle_configs(setup_state):
    app = setup_state.app
    BLUEPRINT.config.update(app.config)
    if BLUEPRINT.config.get('DEFER_CONFIG'):
        log.debug("DEFER_CONFIG set, skipping configuration")
        return

    if BLUEPRINT.config.get("DISALLOWED_ALGOS"):
        BLUEPRINT.config['DISALLOWED_ALGOS'] = BLUEPRINT.config['DISALLOWED_ALGOS'].split(",")
    else:
        BLUEPRINT.config['DISALLOWED_ALGOS'] = []

    if BLUEPRINT.config.get("VERBOSITY"):
        log.debug("Setting verbosity to {}".format(str(BLUEPRINT.config['VERBOSITY'])))
        logging.basicConfig(level=BLUEPRINT.config['VERBOSITY'])
    else:
        log.debug("No verbosity option set, defaulting to WARN")
        logging.basicConfig(level="WARN")


API.add_resource(FileIn, "/")
API.add_resource(TextIn, "/text")
API.add_resource(Version, "/version")
API.add_resource(AvailableAlgos, "/available")
