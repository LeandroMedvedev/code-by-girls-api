from dataclasses import dataclass

from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, Text

from app.configs import db


commentUserGroupTable = db.Table("comment_user_group", 
    db.Column("id", db.Integer, primary_key=True),
    db.Column("user_id", db.Integer, db.ForeignKey("users.id")),
    db.Column("group_id", db.Integer, db.ForeignKey("groups.id")),
    db.Column("comments", db.Text),
    db.Column("timestemp", db.Date),
)
