from flask import Blueprint
from flask import Flask

from app.routes.user_blueprint import bp_user

bp_api = Blueprint("api", __name__, url_prefix="/api")


def init_app(app: Flask):
    bp_api.register_blueprint(bp_user)

    app.register_blueprint(bp_api)
