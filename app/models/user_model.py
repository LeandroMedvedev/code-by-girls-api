from dataclasses import dataclass

from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer

from app.configs import db


@dataclass
class User(db.Model):

    __tablename__ = "users"
