from flask import Flask

from app import routes
from app.configs import database, env_config, migration,jwt


def create_app():
    app = Flask(__name__)

    env_config.init_app(app)
    database.init_app(app)
    migration.init_app(app)
    jwt.init_app(app)
    routes.init_app(app)

    return app
