from http import HTTPStatus

from flask import current_app
from flask import jsonify
from flask import request
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from sqlalchemy.orm import Query
from sqlalchemy.orm import Session

from app.models import GroupModel
from app.models import users_groups_table
from app.models import UserModel


@jwt_required()
def get_subscribe():
    session: Session = current_app.db.session
    user_auth = get_jwt_identity()

    query: Query = (
        session.query(GroupModel)
        .select_from(users_groups_table)
        .filter_by(user_id=user_auth['id'])
        .join(GroupModel)
        .join(UserModel)
        .all()
    )

    return jsonify(query)


@jwt_required()
def subscribes():
    session: Session = current_app.db.session
    user_auth = get_jwt_identity()

    data = request.get_json()

    for key, value in data.items():
        valid_key = 'group_id'

        if key != valid_key:
            return {
                'error': {'valid_key': valid_key, 'key_sended': f'{key}'}
            }, HTTPStatus.BAD_REQUEST

        if not value.isnumeric():
            return {
                'error': f"`{value}` isn't a valid value"
            }, HTTPStatus.BAD_REQUEST

    groups: GroupModel = session.query(GroupModel).get(data['group_id'])

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

    return jsonify(groups), HTTPStatus.CREATED


@jwt_required()
def delete_subscribe(id: int):
    session: Session = current_app.db.session
    user_auth = get_jwt_identity()

    user: UserModel = UserModel.query.filter_by(id=user_auth['id']).first()

    group: GroupModel = GroupModel.query.get(id)

    if not group:
        return {'error': 'Group nor found'}, HTTPStatus.NOT_FOUND

    if user not in group.users:
        return {'error': 'error'}

    try:
        group.users.remove(user)

    except ValueError:
        return {
            'msg': f'You were not subscribed to group `{group.name}`'
        }, HTTPStatus.BAD_REQUEST

    session.add(group)
    session.commit()

    return {
        'msg': f'You unsubscribed from the group `{group.name}`'
    }, HTTPStatus.OK
