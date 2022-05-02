from dataclasses import dataclass

from sqlalchemy.orm import relationship
from sqlalchemy.orm import validates
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, Text, VARCHAR

from app.configs import db
from app.exceptions import InvalidDataError
from .user_group_table import users_groups_table


@dataclass
class GroupModel(db.Model):
    id: int
    name: str
    description: str
    users: list
    user: dict
    remark: list

    __tablename__ = "groups"

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(50), nullable=False, unique=True)
    description = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    users = relationship(
        "UserModel", secondary=users_groups_table, backref="groups")

    user = relationship("UserModel", backref=db.backref(
        "group", uselist=False), uselist=False)

    remark = relationship(
        "CommentUserGroupModel", backref="groupComments")

    @validates("name")
    def name_title(self, key: str, value: str):
        if type(value) != str:
            raise InvalidDataError

        return value.title()

    @validates("description")
    def description_capitalize(self, key: str, value: str):
        if type(value) != str:
            raise InvalidDataError

        return value.capitalize()
