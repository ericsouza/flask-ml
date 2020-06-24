from flask import Blueprint

from .resources import get_classication

apibp = Blueprint("api", __name__, url_prefix="/api/v1.0")

apibp.add_url_rule(
    "/classification", "get_classication", get_classication, methods=["GET"]
)
