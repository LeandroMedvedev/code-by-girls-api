from dataclasses import dataclass

from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, Text

from app.configs import db


@dataclass
class CommentUserGroup(db.Model):

    __tablename__ = "comments"
