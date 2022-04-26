from flask_jwt_extended import get_jwt_identity,jwt_required
from flask import request, current_app, jsonify
from ..models.skill_model import Skill
from psycopg2 import IntegrityError
from ..exceptions import LevelInvalidError


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
    except IntegrityError:
        return{"msg": "skill ja existente"},409
    except LevelInvalidError:
        return {"msg":"Level invalido, o valor deve ser Iniciante,Intermediario ou Avançado"},400

@jwt_required
def get_skill():
    user = get_jwt_identity()
    skills = Skill.query.get_by("user_id" == user.id)
    return jsonify(skills),200

    
@jwt_required
def atualize_skill(id):
    user = get_jwt_identity()
    data = request.get_json()
    session = current_app.db.session 
    skill = Skill.query.get(id)
    if skill == None:
        return{"msg": "skill não existente"},404
    for key, value in data.items():
        setattr(skill, key, value)
    session.add(skill)
    session.commit()
    return jsonify(skill), 200

@jwt_required
def delete_skill(id):  
    skill= Skill.query.get(id)
    session = current_app.db.session
    if skill == None:
        return{"msg": "skill não existente"},404
    session.delete(skill)
    session.commit()
    return "", 204

 
   