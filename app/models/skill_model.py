from sqlalchemy import Column, String, Integer, Enum
from dataclasses import dataclass
from app.configs import db
import enum


class Values(enum.Enum):
    one = "Iniciante"
    two = "Intermediario"
    three = "Avançado"

@dataclass
class SkillModel(db.Model):
    skill = str
    level = str

    __tablename__ = "skills"

    id = Column(Integer, primary_key=True)
    skill = Column(String(100), nullable=False, unique=True)
    level = Column(Enum(Values), nullable=False)
    user_id = Column(Integer, db.ForeignKey("users.id"), nullable=False)
