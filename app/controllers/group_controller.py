from http import HTTPStatus

from app.exceptions import (
    IdNotFoundError,
    InvalidDataError,
    UserUnauthorizedError,
)
from app.models import GroupModel, UserModel, users_groups_table
from app.services import check_data, get_by_id, is_authorized
from flask import current_app, jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from psycopg2.errors import NotNullViolation
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Query, Session


@jwt_required()
def create_group():
    data: dict = request.get_json()
    print(f'{data=}')

    received_keys, valid_keys, invalid_keys = check_data(data)

    if invalid_keys:
        return {
            'invalid_keys': list(invalid_keys),
            'valid_keys': list(valid_keys),
        }, HTTPStatus.BAD_REQUEST

    try:
        user_auth: dict = get_jwt_identity()
        data['user_id'] = user_auth['id']
        print(f'{data=}')

        group: GroupModel = GroupModel(**data)
        print(f'{group=}')

        user: UserModel = UserModel.query.filter_by(id=user_auth['id']).first()

        group.users.append(user)

        session: Session = current_app.db.session
        session.add(group)
        session.commit()

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

    return jsonify(group), HTTPStatus.CREATED


@jwt_required()
def get_groups():
    groups: GroupModel = GroupModel.query.all()

    return jsonify(groups), HTTPStatus.OK


@jwt_required()
def get_group_by_id(id: int):
    try:
        group = get_by_id(GroupModel, id)
    except IdNotFoundError:
        return {'error': 'Group not found'}, HTTPStatus.NOT_FOUND

    return jsonify(group), HTTPStatus.OK


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

    return jsonify(group), HTTPStatus.OK


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
    # except IntegrityError as e:
    #     if isinstance(e.orig, NotNullViolation):
    #         return {'error': 'Group not found'}, HTTPStatus.NOT_FOUND

    return jsonify(group)


# @jwt_required()
# def get_groups():
#     session: Session = current_app.db.session
#     user_auth = get_jwt_identity()

#     query: Query = (
#         session.query(GroupModel).all()
#     )

#     data_groups = [
#         {
#             'id': group.id,
#             'name': group.name,
#             'description': group.description,
#             'owner_group': {
#                 'id': group.user.id,
#                 'name': group.user.name,
#                 'email': group.user.email,
#             },
#             'subscribe': [
#                 {'id': subs.id, 'name': subs.name, 'email': subs.email}
#                 for subs in group.users
#             ],
#             'comments': [
#                 {
#                     'id': commenttator.id,
#                     'comments': commenttator.comments,
#                     'timestamp': commenttator.timestamp,
#                     'user': {
#                         'id': commenttator.user.id,
#                         'name': commenttator.user.name,
#                         'email': commenttator.user.email,
#                     },
#                 }
#                 for commenttator in group.remark
#             ],
#         }
#         for group in query
#     ]

#     return jsonify(data_groups), HTTPStatus.OK
