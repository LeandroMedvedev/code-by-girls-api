from flask import Blueprint
from flask import Flask

from .group_route import bp as bp_group

bp_api = Blueprint("api", __name__, url_prefix="/api")


def init_app(app: Flask):
    bp_api.register_blueprint(bp_group)

    app.register_blueprint(bp_api)
