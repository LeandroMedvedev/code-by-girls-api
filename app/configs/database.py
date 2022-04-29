from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_app(app: Flask):
    db.init_app(app)

    app.db = db

    from app.models import GroupModel
    from app.models import SkillModel
    from app.models import UserModel
    from app.models import WorkModel
    from app.models import comment_user_group_table
    from app.models import users_groups_table
