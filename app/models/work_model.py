from dataclasses import dataclass

from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, Text, String

from app.configs import db


@dataclass
class WorkModel(db.Model):
    title: str
    description: str

    __tablename__ = "works"

    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    description = Column(Text,nullable=False)
    user_id = Column(Integer,ForeignKey('users.id'),nullable=False)
    