from http import HTTPStatus

from flask import current_app
from flask import jsonify
from flask import request
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from psycopg2.errors import NotNullViolation
from sqlalchemy.exc import IntegrityError
from sqlalchemy.exc import ProgrammingError
from sqlalchemy.orm import Session

from app.exceptions import IdNotFoundError
from app.exceptions import InvalidDataError
from app.exceptions import UserUnauthorizedError
from app.models import GroupModel
from app.models import UserModel
from app.services import check_data
from app.services import get_by_id
from app.services import is_authorized


@jwt_required()
def create_group():

    data: dict = request.get_json()

    received_keys, valid_keys, invalid_keys = check_data(data)

    if invalid_keys:
        return {
            'invalid_keys': list(invalid_keys),
            'valid_keys': list(valid_keys),
        }, HTTPStatus.BAD_REQUEST

    try:
        group_exists: GroupModel = GroupModel.query.filter_by(
            name=data.get('name').title()
        ).first()

        if group_exists:
            return {
                'error': 'Group already exists, choose another name.'
            }, HTTPStatus.CONFLICT

        user_auth: dict = get_jwt_identity()
        data['user_id'] = user_auth['id']

        group: GroupModel = GroupModel(**data)

        user: UserModel = UserModel.query.filter_by(id=user_auth['id']).first()

        group.users.append(user)

        session: Session = current_app.db.session
        session.add(group)
        session.commit()

        new_group = {
            'name': group.name,
            'description': group.description,
            'id': group.id,
        }

        return jsonify(new_group), HTTPStatus.CREATED

    except IntegrityError as err:
        if isinstance(err.orig, NotNullViolation):
            return {
                'required_keys': list(valid_keys),
                'received_keys': list(received_keys),
            }, HTTPStatus.UNPROCESSABLE_ENTITY

    except (AttributeError, InvalidDataError, ProgrammingError):
        return {
            'error': 'Invalid data type. Type must be a string'
        }, HTTPStatus.BAD_REQUEST


@jwt_required()
def get_groups():
    groups: GroupModel = GroupModel.query.all()

    all_groups = [
        {
            'id': group.id,
            'name': group.name,
            'description': group.description,
            'group_owner': {
                'id': group.user.id,
                'name': group.user.name,
            },
            'subscribes': [
                {'name': subs.name, 'email': subs.email}
                for subs in group.users
            ],
            'remarks': [
                {
                    'id': rem.id,
                    'comments': rem.comments,
                    'timestamp': rem.timestamp,
                    'author': {
                        'id': rem.user.id,
                        'name': rem.user.name,
                    },
                }
                for rem in group.remark
            ],
        }
        for group in groups
    ]

    return jsonify(all_groups), HTTPStatus.OK


@jwt_required()
def get_group_by_id(id: int):
    try:
        group = get_by_id(GroupModel, id)

        researched_group = {
            'id': group.id,
            'name': group.name,
            'description': group.description,
            'subscribes': [
                {'name': subs.name, 'email': subs.email}
                for subs in group.users
            ],
            'group_owner': {
                'id': group.user.id,
                'name': group.user.name,
            },
            'remarks': [
                {
                    'id': rem.id,
                    'comments': rem.comments,
                    'timestamp': rem.timestamp,
                    'author': {
                        'id': rem.user.id,
                        'name': rem.user.name,
                    },
                }
                for rem in group.remark
            ],
        }

    except IdNotFoundError:
        return {'error': 'Group not found'}, HTTPStatus.NOT_FOUND

    return researched_group, HTTPStatus.OK


@jwt_required()
def update_group(id: int):
    try:
        group: GroupModel = get_by_id(GroupModel, id)

        has_authorized: type = is_authorized(group.user_id)

        data: dict = request.get_json()

        received_keys, valid_keys, invalid_keys = check_data(data)

        for key, value in data.items():
            if key == 'name' and type(value) == str:
                data[key] = value.title()
            if key == 'description' and type(value) is str:
                data[key] = value.capitalize()

        group_exists: GroupModel = GroupModel.query.filter_by(
            name=data.get('name')
        ).first()

        if group_exists:
            return {
                'error': 'Group already exists, choose another name.'
            }, HTTPStatus.CONFLICT

        for key, value in data.items():
            setattr(group, key, value)

        updated_group = {
            'id': group.id,
            'name': group.name,
            'description': group.description,
            'subscribes': [
                {'id': subs.id, 'name': subs.name, 'email': subs.email}
                for subs in group.users
            ],
            'group_owner': {
                'id': group.user.id,
                'name': group.user.name,
                'email': group.user.email,
            },
            'remarks': [
                {
                    'id': rem.id,
                    'comments': rem.comments,
                    'timestamp': rem.timestamp,
                    'user': {
                        'id': rem.user.id,
                        'name': rem.user.name,
                        'email': rem.user.email,
                    },
                }
                for rem in group.remark
            ],
        }

        session: Session = current_app.db.session
        session.commit()

    except IdNotFoundError:
        return {'error': 'Group not found'}, HTTPStatus.NOT_FOUND

    except AttributeError:
        return {
            'error': 'Values must be of type string'
        }, HTTPStatus.BAD_REQUEST

    except UserUnauthorizedError:
        return {
            'error': 'Unauthorized update. You are only allowed to update groups created by you'
        }, HTTPStatus.UNAUTHORIZED

    except (InvalidDataError, ProgrammingError):
        return {
            'error': 'Invalid data type. Type must be a string'
        }, HTTPStatus.BAD_REQUEST

    return updated_group, HTTPStatus.OK


@jwt_required()
def delete_group(id: int):
    try:
        group: GroupModel = get_by_id(GroupModel, id)

        has_authorized: type = is_authorized(group.user_id)

        session: Session = current_app.db.session
        session.delete(group)
        session.commit()

    except IdNotFoundError:
        return {'error': 'Group not found'}, HTTPStatus.NOT_FOUND
    except UserUnauthorizedError:
        return {
            'error': 'Unauthorized deletion. You are only allowed to delete groups created by you'
        }, HTTPStatus.UNAUTHORIZED

    return '', HTTPStatus.NO_CONTENT
