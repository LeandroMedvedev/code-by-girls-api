from http import HTTPStatus

from app.configs.database import db
from app.models.work_model import WorkModel
from flask import current_app, jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from psycopg2.errors import UniqueViolation
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Query
from sqlalchemy.orm.session import Session


@jwt_required()
def create_work():
    data = request.get_json()

    correct_keys = ['title', 'description']
    validate_keys = list(correct_keys - data.keys())

    try:

        for key, value in data.items():
            if key == 'title':
                data[key] = value.title()

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
                'error': f"The title '{work_title}' is alredy exists"
            }, HTTPStatus.CONFLICT

    except KeyError:
        missing_key = validate_keys.pop()

        return {
            'error': f'key {missing_key.upper()} is missing'
        }, HTTPStatus.BAD_REQUEST


@jwt_required()
def get_work():
    works: Query = db.session.query(WorkModel).all()

    return jsonify(works), HTTPStatus.OK


@jwt_required()
def delete_work(work_id):

    query = WorkModel.query.get(work_id)
    session: Session = db.session
    session.delete(query)
    session.commit()

    return '', HTTPStatus.NO_CONTENT


@jwt_required()
def patch_work(work_id):

    session: Session = db.session
    data = request.get_json()
    work_changed = WorkModel.query.get(work_id)

    for key, values in data.items():
        setattr(work_changed, key, values)

    session.add(work_changed)
    session.commit()

    return jsonify(work_changed), HTTPStatus.OK
