from dataclasses import dataclass

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import validates

from app.configs import db
from app.exceptions import LevelInvalidError


@dataclass
class SkillModel(db.Model):
    id: int
    skill: str
    level: str

    __tablename__ = 'skills'

    id = Column(Integer, primary_key=True)
    skill = Column(String(100), nullable=False)
    level = Column(String(50), nullable=False)
    user_id = Column(
        Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False
    )

    @validates('level')
    def validade_importance(self, key, level):
        if (
            level != 'Iniciante'
            and level != 'Intermediario'
            and level != 'Avançado'
        ):
            raise LevelInvalidError
        return level
