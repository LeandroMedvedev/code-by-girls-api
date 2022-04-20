from dataclasses import dataclass

from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer

from app.configs import db


@dataclass
class Skill(db.Model):

    __tablename__ = "skills"
