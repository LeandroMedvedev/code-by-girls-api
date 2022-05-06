from http import HTTPStatus

from app.configs import db
from app.models import WorkModel
from flask import current_app, jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from psycopg2.errors import UniqueViolation
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Query, Session


@jwt_required()
def create_work():
    data = request.get_json()

    correct_keys = ['title', 'description']

    try:
        for key, value in data.items():
            if key == 'title' and type(value) == str:
                data[key] = value.title()
            if key == 'description' and type(value) is str:
                data[key] = value.capitalize()

            if not value:
                return {
                    'error': f'{key.upper()} is empty!'
                }, HTTPStatus.BAD_REQUEST

            if key not in correct_keys:
                return {
                    'error': {'valid_keys': correct_keys, 'key_sended': key}
                }, HTTPStatus.BAD_REQUEST

        validate_keys = list(correct_keys - data.keys())
        if len(validate_keys) != 0:
            return {
                'error': {'misssing_keys': validate_keys}
            }, HTTPStatus.BAD_REQUEST

        session: Session = current_app.db.session
        user_auth = get_jwt_identity()

        data['user_id'] = user_auth['id']
        work_title = data['title']

        work = WorkModel(**data)
        session.add(work)
        session.commit()

        return jsonify(work), HTTPStatus.CREATED

    except IntegrityError as e:
        if type(e.orig) == UniqueViolation:
            return {
                'error': f"The Work Title: '{work_title}', is alredy exists"
            }, HTTPStatus.CONFLICT


@jwt_required()
def get_work():
    user = get_jwt_identity()
    id = user['id']
    works = WorkModel.query.filter(WorkModel.user_id == id)

    serializer = [
        {'id': work.id, 'title': work.title, 'description': work.description}
        for work in works
    ]

    return jsonify(serializer), HTTPStatus.OK


@jwt_required()
def delete_work(work_id):

    work = WorkModel.query.get(work_id)
    session = current_app.db.session
    user = get_jwt_identity()

    if not work:
        return {'error': "Work doesn't exists!"}, HTTPStatus.NOT_FOUND

    if user['id'] != work.user_id:
        return {
            'error': "It is only possible to delete your 'works'"
        }, HTTPStatus.BAD_REQUEST

    session.delete(work)
    session.commit()

    return '', HTTPStatus.NO_CONTENT


@jwt_required()
def patch_work(work_id):
    correct_keys = ['title', 'description']

    data = request.get_json()

    try:
        session: Session = db.session
        user = get_jwt_identity()
        work_to_change = WorkModel.query.get(work_id)

        if not work_to_change:
            return {'error': "Work doesn't exists!"}, HTTPStatus.NOT_FOUND

        if user['id'] != work_to_change.user_id:
            return {
                'error': "It is only possible to update your 'works'"
            }, HTTPStatus.BAD_REQUEST

        for key, value in data.items():
            if key == 'title' and type(value) == str:
                data[key] = value.title()
            if key == 'description' and type(value) is str:
                data[key] = value.capitalize()

            if not value:
                return {
                    'error': f'{key.upper()} is empty!'
                }, HTTPStatus.BAD_REQUEST

            if key not in correct_keys:
                return {
                    'error': {'valid_keys': correct_keys, 'key_sended': key}
                }, HTTPStatus.BAD_REQUEST

            if type(value) != str:
                return {
                    'error': f'The value of {key.upper()} only accepted Strings'
                }, HTTPStatus.BAD_REQUEST

        for key, values in data.items():
            setattr(work_to_change, key, values)

        session.add(work_to_change)
        session.commit()

        return jsonify(work_to_change), HTTPStatus.OK

    except IntegrityError as e:
        if type(e.orig) == UniqueViolation:
            work_title = data['title']

            return {
                'error': f"The title '{work_title}' is already exists"
            }, HTTPStatus.CONFLICT

    validate_keys = list(correct_keys - data.keys())
    if len(validate_keys) != 0:
        return {
            'error': {'misssing_keys': validate_keys}
        }, HTTPStatus.BAD_REQUEST


@jwt_required()
def get_work_to_id(work_id):

    work = WorkModel.query.get(work_id)
    session = current_app.db.session

    if not work:
        return {'error': "Work doesn't exists!"}, HTTPStatus.NOT_FOUND

    session.commit()
 
    return jsonify(work), HTTPStatus.OK
