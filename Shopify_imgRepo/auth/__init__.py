"""auth blueprint """
from flask import Blueprint

auth_bp = Blueprint("auth", __name__, template_folder='templates')

from Shopify_imgRepo.auth import routes