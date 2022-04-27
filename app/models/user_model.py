from dataclasses import dataclass

from sqlalchemy.orm import validates, relationship
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, String
from werkzeug.security import check_password_hash, generate_password_hash

from app.configs import db
from app.exceptions import InvalidEmailError


@dataclass
class UserModel(db.Model):

    id:int
    name:str
    email:str
    skills:list
    works:list
    # password:str

    __tablename__ = "users"


    id = Column(Integer, primary_key = True)
    name = Column(String(50), nullable = False)
    email = Column(String(100), nullable = False, unique = True)
    password = Column(String)

    skills = relationship("SkillModel", backref="user")
    works = relationship("WorkModel", backref="user")


    @validates("email")
    def validate_email(self, key, email):
        if "@" not in email or email.endswith(".com"):
            raise InvalidEmailError
        return email
            
    
    @property
    def password(self):
        raise AttributeError("Password cannot be accessed!")


    @password.setter
    def password(self, password_to_hash):
        self.password = generate_password_hash(password_to_hash)


    def verify_password(self, compare_to_password):
        return check_password_hash(self.password, compare_to_password)
        