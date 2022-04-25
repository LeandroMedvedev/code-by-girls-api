from dataclasses import dataclass

from sqlalchemy.orm import validates
from ..exeptions import LevelInvalidError
from sqlalchemy import Column, String, Integer

from app.configs import db


@dataclass
class Skill(db.Model):
    skill = str
    level = str

    __tablename__ = "skills"

    id = Column(Integer, primary_key=True)
    skill = Column(String(100), nullable=False, unique=True)
    level = Column(String(50), nullable=False)
    user_id = Column(Integer, db.ForeignKey("users.id"), nullable=False)

    @validates("level")
    def validade_importance(self, key, level):
        if level != "Iniciante" and level != "Intermediario" and level != "Avançado":
            raise LevelInvalidError
