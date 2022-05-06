from http import HTTPStatus

from app.exceptions import (
    IdNotFoundError,
    InvalidDataError,
    UserUnauthorizedError,
)
from app.models import GroupModel, UserModel
from app.services import check_data, get_by_id, is_authorized
from flask import current_app, jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from psycopg2.errors import NotNullViolation
from sqlalchemy.exc import IntegrityError, PendingRollbackError
from sqlalchemy.orm import Session


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
        user_auth: dict = get_jwt_identity()
        data['user_id'] = user_auth['id']

        group: GroupModel = GroupModel(**data)

        user: UserModel = UserModel.query.filter_by(id=user_auth['id']).first()

        group.users.append(user)

        session: Session = current_app.db.session
        session.add(group)
        session.commit()

    except TypeError:
        return {'error': 'Group name already exists!'}, HTTPStatus.CONFLICT
    except IntegrityError as err:
        if isinstance(err.orig, NotNullViolation):
            return {
                'required_keys': list(valid_keys),
                'received_keys': list(received_keys),
            }, HTTPStatus.UNPROCESSABLE_ENTITY
    except InvalidDataError:
        return {
            'error': 'Invalid data type. Type must be a string'
        }, HTTPStatus.BAD_REQUEST

    except PendingRollbackError:
        return {'error': 'Group name already exists!'}, HTTPStatus.CONFLICT

    return jsonify(group), HTTPStatus.CREATED


@jwt_required()
def get_groups():
    groups: GroupModel = GroupModel.query.all()

    new_groups = [
        {
            'id': grupo.id,
            'name': grupo.name,
            'description': grupo.description,
            'subscribes': [
                {'id': subs.id, 'name': subs.name, 'email': subs.email}
                for subs in grupo.users
            ],
            'group_owner': {
                'id': grupo.user.id,
                'name': grupo.user.name,
                'email': grupo.user.email,
            },
            'commits': [
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
                for rem in grupo.remark
            ],
        }
        for grupo in groups
    ]

    return jsonify(new_groups), HTTPStatus.OK


@jwt_required()
def get_group_by_id(id: int):
    try:
        group = get_by_id(GroupModel, id)

        new_groups = {
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
            'commits': [
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

    except IdNotFoundError:
        return {'error': 'Group not found'}, HTTPStatus.NOT_FOUND

    return jsonify(new_groups), HTTPStatus.OK


@jwt_required()
def update_group(id: int):
    try:
        group: GroupModel = get_by_id(GroupModel, id)

        has_authorized: type = is_authorized(group.user_id)

        data: dict = request.get_json()

        received_keys, valid_keys, invalid_keys = check_data(data)

        data['name'] = data['name'].title()
        data['description'] = data['description'].capitalize()

        for key, value in data.items():
            setattr(group, key, value)

        new_groups = {
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
            'commits': [
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
    except KeyError:
        return {
            'invalid_keys': list(invalid_keys),
            'valid_keys': list(valid_keys),
        }, HTTPStatus.BAD_REQUEST
    except AttributeError:
        return {
            'error': 'Values must be of type string'
        }, HTTPStatus.BAD_REQUEST
    except UserUnauthorizedError:
        return {
            'error': 'Unauthorized update. You are only allowed to update groups created by you'
        }, HTTPStatus.UNAUTHORIZED

    return jsonify(new_groups), HTTPStatus.OK


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
