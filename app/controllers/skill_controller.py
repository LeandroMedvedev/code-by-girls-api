from flask import request, current_app, jsonify
from flask_jwt_extended import get_jwt_identity
from psycopg2 import IntegrityError
from ..exeptions import LevelInvalidError
from ..models.skill_model import Skill


def create_skill():
    try:
        session = current_app.db.session
        data = request.get_json()
        user = get_jwt_identity()
        level = data.pop["level"]
        data["user_id"]=user.id
        data["level_id"] = level
        skill = Skill(**data)

        session.add(skill)
        session.commit()
        return jsonify(skill),201
    except LevelInvalidError:
        return {"msg":"Level invalido, o valor deve ser Iniciante,Intermediario ou Avançado"},400
    except IntegrityError:
        return{"msg": "skill ja existente"},409


 