from flask import Flask

from app import routes
from app.configs import database
from app.configs import env_config
from app.configs import jwt_auth
from app.configs import mail
from app.configs import migration


def create_app():
    app = Flask(__name__)

    mail.init_app(app)
    env_config.init_app(app)
    database.init_app(app)
    migration.init_app(app)
    jwt_auth.init_app(app)
    routes.init_app(app)

    return app
