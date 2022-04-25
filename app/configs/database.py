from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_app(app: Flask):
    db.init_app(app)

    app.db = db

    from app.models import Group
    from app.models import Skill
    from app.models import User
    from app.models import Work
    from app.models import comments_users_groups_table
    from app.models import users_groups_table
