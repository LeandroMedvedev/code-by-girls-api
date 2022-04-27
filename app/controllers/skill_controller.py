from flask_jwt_extended import get_jwt_identity, jwt_required
from flask import request, current_app, jsonify
from ..models.skill_model import SkillModel
from ..exceptions import LevelInvalidError


@jwt_required()
def create_skill():
    try:
        session = current_app.db.session
        data = request.get_json()
        user = get_jwt_identity()
        data["user_id"]=user["id"]
        skill = SkillModel(**data)
        session.add(skill)
        session.commit()
        return jsonify(skill),201
    except TypeError:
        return{"msg":{"valid_keys":
        {"skill":"","level":""},
        "your_keys":data}},400

    except LevelInvalidError:
        return {"msg":"Level invalido, o valor deve ser Iniciante,Intermediario ou Avançado"},400

@jwt_required()
def get_skill():
    user = get_jwt_identity()
    id=user["id"]
    skills = (SkillModel.query.filter(SkillModel.user_id==id))
    serializer = [{"id":skill.id,
     "skill": skill.skill,
     "level": skill.level}for skill in skills]
    return jsonify(serializer),200

    


def atualize_skill(id):
    try:
        data:dict = request.get_json()
        session = current_app.db.session 

        skill = SkillModel.query.get(id)
        if skill == None:
            return{"msg": "skill não existente"},404

        for key, value in data.items():
            if key == "skill" or key == "level":
                setattr(skill, key, value)

        session.add(skill)
        session.commit()
        return jsonify(skill), 200
    except LevelInvalidError:
        return {"msg":"Level invalido, o valor deve ser Iniciante,Intermediario ou Avançado"},400





def delete_skill(id):  
    skill = SkillModel.query.get(id)
    session = current_app.db.session
    if skill == None:
        return{"msg": "skill não existente"},404
        
    session.delete(skill)
    session.commit()
    return "", 204
