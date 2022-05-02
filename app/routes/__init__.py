from flask import Blueprint
from flask import Flask

from .group_blueprint import bp as bp_group
from .login_blueprint import bp_login
from .skills_blueprint import bp_skill
from .user_blueprint import bp_user
from .work_blueprint import bp_work
from .comment_user_group_blueprint import bp as bp_comments
from .subscribes_blueprint import bp as bp_subscribe

bp_api = Blueprint("api", __name__, url_prefix="/api")


def init_app(app: Flask):
    bp_api.register_blueprint(bp_group)
    bp_api.register_blueprint(bp_login)
    bp_api.register_blueprint(bp_skill)
    bp_api.register_blueprint(bp_user)
    bp_api.register_blueprint(bp_work)
    bp_api.register_blueprint(bp_comments)
    bp_api.register_blueprint(bp_subscribe)

    app.register_blueprint(bp_api)
