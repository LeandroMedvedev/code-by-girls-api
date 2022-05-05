from dataclasses import dataclass
from datetime import datetime

from app.configs import db
from app.models.group_model import GroupModel
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import DateTime, Integer, Text


@dataclass
class CommentUserGroupModel(db.Model):
    id: int
    comments: str
    timestamp: str
    user: dict

    __tablename__ = 'comments_users_groups'

    id = Column(Integer, primary_key=True)
    comments = Column(Text)
    timestamp = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    group_id = Column(Integer, ForeignKey('groups.id'), nullable=False)

    user = db.relationship('UserModel', backref='comments')
