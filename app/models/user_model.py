from dataclasses import dataclass
from sqlalchemy.orm import validates
from app.configs import db
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, String

from app.exeptions import InvalidEmailError


@dataclass
class User(db.Model):
    id : int
    name: str
    email: str
    password: str

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String)


    @validates("email")
    def validate_email(self, key, email):
        if "@" not in email or email.endswith(".com"):
            raise InvalidEmailError
            