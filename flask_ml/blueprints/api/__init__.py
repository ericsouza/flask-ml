from flask import Blueprint

from .resources import iris_classication

apibp = Blueprint("api", __name__, url_prefix="/api/v1.0")

apibp.add_url_rule(
    "/iris_classication", "iris_classication", iris_classication, methods=["GET"]
)
