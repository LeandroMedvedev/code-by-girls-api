from http import HTTPStatus

from flask import current_app
from flask import jsonify
from flask import request
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from sqlalchemy.orm import Session

from app.exceptions import LevelInvalidError
from app.models import SkillModel


@jwt_required()
def create_skill():
    try:
        data: dict = request.get_json()
        user = get_jwt_identity()
        data['user_id'] = user['id']

        skill: SkillModel = SkillModel(**data)

        session: Session = current_app.db.session
        session.add(skill)
        session.commit()

        return jsonify(skill), HTTPStatus.CREATED

    except TypeError:
        return {
            'msg': {
                'valid_keys': {'skill': '', 'level': ''},
                'your_keys': data,
            }
        }, HTTPStatus.BAD_REQUEST

    except KeyError:
        return {
            'msg': {
                'valid_keys': {'skill': '', 'level': ''},
                'your_keys': data,
            }
        }, HTTPStatus.BAD_REQUEST

    except LevelInvalidError:
        return {
            'msg': 'Invalid level, value must be: Iniciante, Intermediario ou Avançado'
        }, HTTPStatus.BAD_REQUEST


@jwt_required()
def get_skill():
    user = get_jwt_identity()
    id = user['id']

    skills: SkillModel = SkillModel.query.filter(SkillModel.user_id == id)

    serializer = [
        {'id': skill.id, 'skill': skill.skill, 'level': skill.level}
        for skill in skills
    ]

    return jsonify(serializer), HTTPStatus.OK


def get_skill_id(id):
    skill: SkillModel = SkillModel.query.get(id)

    if not skill:
        return {'msg': 'Non-existent skill'}, HTTPStatus.NOT_FOUND

    return jsonify(skill), HTTPStatus.OK


@jwt_required()
def update_skill(id):
    try:
        data: dict = request.get_json()

        user = get_jwt_identity()

        skill: SkillModel = SkillModel.query.get(id)

        if skill == None:
            return {'msg': 'Non-existent skill'}, HTTPStatus.NOT_FOUND
        if user['id'] != skill.user_id:
            return {
                'msg': 'It is possible to update only your skills'
            }, HTTPStatus.BAD_REQUEST

        for key, value in data.items():
            skill.skill = data['skill'].title()
            setattr(skill, key, value)

        session = current_app.db.session
        session.add(skill)
        session.commit()

        return jsonify(skill), HTTPStatus.OK

    except LevelInvalidError:
        return {
            'msg': 'Invalid level, value must be: Iniciante, Intermediario ou Avançado'
        }, HTTPStatus.BAD_REQUEST
    except KeyError:
        return {
            'msg': {
                'valid_keys': {'skill': '', 'level': ''},
                'your_keys': data,
            }
        }, HTTPStatus.BAD_REQUEST


@jwt_required()
def delete_skill(id):

    skill: SkillModel = SkillModel.query.get(id)

    user = get_jwt_identity()

    if skill == None:
        return {'msg': 'Non-existent skill'}, HTTPStatus.NOT_FOUND
    if user['id'] != skill.user_id:
        return {
            'msg': 'It is possible to delete only your skills'
        }, HTTPStatus.BAD_REQUEST

    session = current_app.db.session
    session.delete(skill)
    session.commit()

    return '', HTTPStatus.NO_CONTENT
