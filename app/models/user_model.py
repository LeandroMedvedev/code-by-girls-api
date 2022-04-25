from dataclasses import dataclass
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer,String

from app.configs import db


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
