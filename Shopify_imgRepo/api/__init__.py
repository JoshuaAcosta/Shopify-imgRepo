"""API implementation """
from flask import Blueprint
from flask_restful  import Api
from .resources import ImageResources

api_bp = Blueprint('api', __name__)

api = Api(api_bp)

api.add_resource(ImageResources, '/api/images', methods=["GET", "POST"])
