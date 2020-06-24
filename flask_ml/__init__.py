from dotenv import load_dotenv

load_dotenv()

from os import environ
from flask import Flask


from flask_ml.blueprints.api import apibp


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = environ.get(
        "FLASK_ML_SECRET_KEY", "ifthereisnokeythisonewillbeused"
    )

    app.register_blueprint(apibp)

    return app
