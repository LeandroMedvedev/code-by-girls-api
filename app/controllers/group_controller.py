from http import HTTPStatus

from flask import current_app
from flask import jsonify
from flask import request
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from psycopg2.errors import NotNullViolation
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.exceptions import InvalidDataError
from app.models import GroupModel

# from app.models import UserModel
from app.services import check_data


@jwt_required()
def create_group():
    data: dict = request.get_json()

    received_keys, valid_keys, invalid_keys = check_data(data)

    if invalid_keys:
        return {
            "invalid_keys": list(invalid_keys),
            "valid_keys": list(valid_keys),
        }, HTTPStatus.BAD_REQUEST

    try:
        get_user: dict = get_jwt_identity()
        data.update({"user_id": get_user["id"]})

        group: GroupModel = GroupModel(**data)
        # user: UserModel = UserModel.query.filter_by(id=get_user["id"]).first()
        # print(f"{user=}")
        # print(f"{group.users.append(user)=}")
        # group.users.append(user)
        session: Session = current_app.db.session
        session.add(group)
        session.commit()
    except IntegrityError as err:
        if isinstance(err.orig, NotNullViolation):
            return {
                "required_keys": list(valid_keys),
                "received_keys": list(received_keys),
            }, HTTPStatus.UNPROCESSABLE_ENTITY
    except InvalidDataError:
        return {
            "error": "Invalid data type. Type must be a string"
        }, HTTPStatus.BAD_REQUEST

    return jsonify(group), HTTPStatus.CREATED


@jwt_required()
def get_groups():
    groups: GroupModel = GroupModel.query.all()
    group: GroupModel = get_jwt_identity()
    print(f"{group=}")

    return jsonify(groups), HTTPStatus.OK


@jwt_required()
def update_group(id: int):

    group: GroupModel = GroupModel.query.filter_by(id=id).first()
    print(f"{group=}")
    # if not group:
    #     return {'error': 'Group not found'}, HTTPStatus.NOT_FOUND

    data: dict = request.get_json()
    print(f"{data=}")
    # valid_keys = {'name', "description"}
    # received_keys = set(data.keys())
    # invalid_keys
    updated_group = GroupModel(**data)
    print(f"{updated_group=}")

    return "", HTTPStatus.OK


@jwt_required()
def delete_group(id: int):

    return "", HTTPStatus.NO_CONTENT
