from flask import Blueprint

main_bp = Blueprint("main", __name__, template_folder='templates')

from Shopify_imgRepo.main import routes