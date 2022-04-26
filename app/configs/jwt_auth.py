from secrets import token_hex

from flask import Flask
from flask_jwt_extended import JWTManager


def init_app(app: Flask):
    app.config["JWT_SECRET_KEY"] = token_hex(32)

    JWTManager(app)
