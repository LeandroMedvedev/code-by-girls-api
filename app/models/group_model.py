from dataclasses import dataclass

from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, Text, VARCHAR

from app.configs import db


@dataclass
class Group(db.Model):
    name: str
    description: str

    __tablename__ = "groups"

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(50), nullable=False)
    description = Column(Text, nullable=False)
