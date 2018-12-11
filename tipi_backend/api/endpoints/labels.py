import logging

from flask import request
from flask_restplus import Resource
from tipi_backend.api.restplus import api
from tipi_backend.api.business import extract_labels_from_text, get_tags

log = logging.getLogger(__name__)

ns = api.namespace('labels', description='Operations related to label extraction')


@ns.route('/')
class LabelsExtractor(Resource):
    def get(self):
        """Returns list of active deputies."""
        example = "¿Considera aceptable el Gobierno recortar las prestaciones por desempleo cuando la economía está creciendo"
        return extract_labels_from_text(example, get_tags())