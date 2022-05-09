from http import HTTPStatus

from flask import current_app
from flask import jsonify
from flask import request
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from sqlalchemy.exc import DataError
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm import Query
from sqlalchemy.orm import Session

from app.models import GroupModel
from app.models import users_groups_table
from app.models import UserModel


@jwt_required()
def get_subscribe():
    user_auth = get_jwt_identity()

    session: Session = current_app.db.session
    query: Query = (
        session.query(GroupModel)
        .select_from(users_groups_table)
        .filter_by(user_id=user_auth['id'])
        .join(GroupModel)
        .join(UserModel)
        .all()
    )

    enrolled = [
        {
            'id': subs.id,
            'name': subs.name,
            'description': subs.description,
            'group_owner': {
                'id': subs.user.id,
                'name': subs.user.name,
                'email': subs.user.email,
            },
            'subscribes': [
                {'id': subs.id, 'name': subs.name, 'email': subs.email}
                for subs in subs.users
            ],
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
                for rem in subs.remark
            ],
        }
        for subs in query
    ]

    return jsonify(enrolled)


@jwt_required()
def subscribes():
    user_auth = get_jwt_identity()

    data: dict = request.get_json()

    for key, value in data.items():
        valid_key = 'group_id'

        if key != valid_key:
            return {
                'error': {'valid_key': valid_key, 'key_sended': f'{key}'}
            }, HTTPStatus.BAD_REQUEST

    try:
        session: Session = current_app.db.session
        groups: GroupModel = session.query(GroupModel).get(data['group_id'])
    except (DataError, InvalidRequestError):
        return {
            'error': 'Invalid data type. The type must be an integer'
        }, HTTPStatus.BAD_REQUEST

    if not groups:
        return {'error': "Group doesn't exists"}, HTTPStatus.NOT_FOUND

    user = session.query(UserModel).get(user_auth['id'])

    if user in groups.users:
        return {
            'msg': 'You are already subscribed to this group'
        }, HTTPStatus.CONFLICT

    else:
        groups.users.append(user)

    session.add(groups)
    session.commit()

    subscription = {
        'id': groups.id,
        'name': groups.name,
        'description': groups.description,
        'group_owner': {
            'id': groups.user.id,
            'name': groups.user.name,
            'email': groups.user.email,
        },
        'subscribes': [
            {'id': subs.id, 'name': subs.name, 'email': subs.email}
            for subs in groups.users
        ],
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
            for rem in groups.remark
        ],
    }

    return subscription, HTTPStatus.CREATED


@jwt_required()
def delete_subscribe(id: int):
    user_auth = get_jwt_identity()

    user: UserModel = UserModel.query.filter_by(id=user_auth['id']).first()

    group: GroupModel = GroupModel.query.get(id)

    if not group:
        return {'error': 'Group not found'}, HTTPStatus.NOT_FOUND

    if user not in group.users:
        return {'error': 'Subscribe not found!'}, HTTPStatus.NOT_FOUND

    try:
        group.users.remove(user)

    except ValueError:
        return {
            'msg': f'You were not subscribed to group "{group.name}"'
        }, HTTPStatus.BAD_REQUEST

    session: Session = current_app.db.session
    session.add(group)
    session.commit()

    return {
        'msg': f'You unsubscribed from the group `{group.name}`'
    }, HTTPStatus.OK
