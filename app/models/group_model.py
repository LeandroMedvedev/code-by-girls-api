from dataclasses import dataclass

from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, Text, VARCHAR

from app.configs import db


@dataclass
class GroupModel(db.Model):
    name: str
    description: str

    __tablename__ = "groups"

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(50), nullable=False)
    description = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
