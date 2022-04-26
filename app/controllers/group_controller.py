from http import HTTPStatus

from flask import current_app
from flask import jsonify
from flask import request
from flask_jwt_extended import get_jwt_identity, jwt_required
from sqlalchemy.orm import Session

from app.models import GroupModel
from app.models import UserModel

# @jwt_required()
def create_group():
    data: dict = request.get_json()
    user: UserModel = get_jwt_identity()
    data.update({'user_id': user.id})
    print(f'{data=}')

    return '', HTTPStatus.CREATED


@jwt_required()
def get_groups():
    groups: GroupModel = GroupModel.query.all()
    group: GroupModel = get_jwt_identity()

    return jsonify(groups), HTTPStatus.OK


# @jwt_required()
def update_group(id: int):

    return '', HTTPStatus.OK

# @jwt_required()
def delete_group(id: int):

    return '', HTTPStatus.NO_CONTENT
