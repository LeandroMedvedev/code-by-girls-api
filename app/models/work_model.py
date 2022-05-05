from dataclasses import dataclass

from app.configs import db
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Text


@dataclass
class WorkModel(db.Model):
    id: int
    title: str
    description: str

    __tablename__ = 'works'

    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False, unique=True)
    description = Column(Text, nullable=False)

    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
