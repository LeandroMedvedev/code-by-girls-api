from datetime import datetime as dt
from http import HTTPStatus

from flask import current_app
from flask import jsonify
from flask import request
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from sqlalchemy.orm import Query
from sqlalchemy.orm import Session

from app.exceptions import InvalidDataError
from app.models import CommentUserGroupModel
from app.models import GroupModel
from app.models import users_groups_table
from app.models import UserModel


@jwt_required()
def get_all():
    user_auth = get_jwt_identity()

    session: Session = current_app.db.session
    comments: CommentUserGroupModel = (
        session.query(CommentUserGroupModel)
        .filter_by(user_id=user_auth['id'])
        .all()
    )

    remarks = [
        {
            'id': comm.id,
            'comments': comm.comments,
            'timestamp': comm.timestamp,
            'author': {
                'id': comm.user.id,
                'name': comm.user.name,
                'email': comm.user.email,
            },
        }
        for comm in comments
    ]

    return jsonify(remarks), HTTPStatus.OK


@jwt_required()
def get_by_id(id: int):
    comment = CommentUserGroupModel.query.get(id)

    if comment == None:
        return {'msg': 'Non-existent comment'}, HTTPStatus.NOT_FOUND

    remark = {
        'id': comment.id,
        'comments': comment.comments,
        'timestamp': comment.timestamp,
        'author': {
            'id': comment.user.id,
            'name': comment.user.name,
            'email': comment.user.email,
        },
    }

    return remark, HTTPStatus.OK


@jwt_required()
def create(id: int):
    user_auth = get_jwt_identity()

    data: dict = request.get_json()
    received_keys = [key for key in data.keys()]
    data['timestamp'] = dt.now()
    data['user_id'] = user_auth['id']

    try:
        session: Session = current_app.db.session
        """
            query looks for the groups in which the user is subscribed
        """
        query: Query = (
            session.query(GroupModel)
            .select_from(users_groups_table)
            .filter_by(user_id=user_auth['id'])
            .join(GroupModel)
            .join(UserModel)
            .all()
        )

        is_registered = list()

        for q in query:
            is_registered.append(q.id)

        is_enrolled = is_registered.index(id)

        """
            is_enrolled is equal to zero because, if the validation was done only with 'if is_enrolled' and the index was 0, 0 is equal to False
        """
        if is_enrolled or is_enrolled == 0:
            group_to_comment: GroupModel = GroupModel.query.get(id)
            comment: CommentUserGroupModel = CommentUserGroupModel(**data)

            group_to_comment.remark.append(comment)
            session.add(comment)
            session.commit()

            remark = {
                'id': comment.id,
                'comment': comment.comments,
                'timestamp': comment.timestamp,
                'author': {'id': comment.user_id, 'name': comment.user.name},
            }

            return remark, HTTPStatus.CREATED

    except ValueError:
        return {
            'error': 'Either you are not subscribed or the group does not exist'
        }, HTTPStatus.NOT_FOUND

    except TypeError:
        return {
            'valid_key': 'comments',
            'received_keys': received_keys,
        }, HTTPStatus.BAD_REQUEST

    except InvalidDataError:
        return {
            'error': 'Invalid data type. The comment must be of type string'
        }, HTTPStatus.BAD_REQUEST


@jwt_required()
def update(id: int):
    user: dict = get_jwt_identity()
    data: dict = request.get_json()

    comment: CommentUserGroupModel = CommentUserGroupModel.query.get(id)

    if comment == None:
        return {'msg': 'Non-existent comment'}, HTTPStatus.NOT_FOUND

    if user['id'] != comment.user_id:
        return {
            'msg': 'It is possible to update only your comments'
        }, HTTPStatus.BAD_REQUEST

    try:
        for key, value in data.items():
            if key == 'comments':
                setattr(comment, key, value)

                session: Session = current_app.db.session
                session.add(comment)
                session.commit()

                updated_comment = {
                    'id': comment.id,
                    'comments': comment.comments,
                    'timestamp': comment.timestamp,
                    'user': {
                        'id': comment.user.id,
                        'name': comment.user.name,
                    },
                }
                return updated_comment, HTTPStatus.OK
            else:
                return {
                    'valid_key': 'comment',
                    'invalid_keys': list(data.keys()),
                }, HTTPStatus.BAD_REQUEST

    except InvalidDataError:
        return {
            'error': 'Invalid data type. The comment must be of type string'
        }, HTTPStatus.BAD_REQUEST


@jwt_required()
def delete(id: int):
    user: dict = get_jwt_identity()

    comment: CommentUserGroupModel = CommentUserGroupModel.query.get(id)

    if comment == None:
        return {'msg': 'Non-existent comment'}, HTTPStatus.NOT_FOUND

    if user['id'] != comment.user_id:
        return {
            'msg': 'It is possible to delete only your comments'
        }, HTTPStatus.UNAUTHORIZED

    session: Session = current_app.db.session
    session.delete(comment)
    session.commit()

    return '', HTTPStatus.NO_CONTENT
