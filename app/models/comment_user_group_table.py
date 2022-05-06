from dataclasses import dataclass
from datetime import datetime

from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.sql.sqltypes import Integer
from sqlalchemy.sql.sqltypes import Text

from app.configs import db

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

    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))
    group_id = Column(Integer, ForeignKey('groups.id', ondelete='CASCADE'))

    user = db.relationship('UserModel', backref='comments')
