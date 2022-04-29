from http import HTTPStatus

from flask import current_app
from flask import jsonify
from flask import request
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from psycopg2.errors import NotNullViolation
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.exceptions import IdNotFoundError
from app.exceptions import InvalidDataError
from app.exceptions import UserUnauthorizedError
from app.models import GroupModel
from app.services import check_data
from app.services import get_by_id
from app.services import is_authorized


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
        data["user_id"] = get_user["id"]

        group: GroupModel = GroupModel(**data)

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

    data_groups = [
        {
            "id": group.id,
            "name": group.name,
            "description": group.description,
        }
        for group in groups
    ]

    return jsonify(data_groups), HTTPStatus.OK


@jwt_required()
def get_group_by_id(id: int):
    try:
        group = get_by_id(GroupModel, id)
    except IdNotFoundError:
        return {"error": "Group not found"}, HTTPStatus.NOT_FOUND

    return jsonify(group), HTTPStatus.OK


@jwt_required()
def update_group(id: int):
    try:
        group: GroupModel = get_by_id(GroupModel, id)

        has_authorized: type = is_authorized(group.user_id)

        data: dict = request.get_json()

        received_keys, valid_keys, invalid_keys = check_data(data)

        data["name"] = data["name"].title()
        data["description"] = data["description"].capitalize()

        for key, value in data.items():
            setattr(group, key, value)

        session: Session = current_app.db.session
        session.commit()
    except IdNotFoundError:
        return {"error": "Group not found"}, HTTPStatus.NOT_FOUND
    except KeyError:
        return {
            "invalid_keys": list(invalid_keys),
            "valid_keys": list(valid_keys),
        }, HTTPStatus.BAD_REQUEST
    except AttributeError:
        return {"error": "Values must be of type string"}, HTTPStatus.BAD_REQUEST
    except UserUnauthorizedError:
        return {
            "error": "Unauthorized update. You are only allowed to update groups created by you"
        }, HTTPStatus.UNAUTHORIZED

    return jsonify(group), HTTPStatus.OK


@jwt_required()
def delete_group(id: int):
    try:
        group: GroupModel = get_by_id(GroupModel, id)

        has_authorized: type = is_authorized(group.user_id)
    except IdNotFoundError:
        return {"error": "Group not found"}, HTTPStatus.NOT_FOUND
    except UserUnauthorizedError:
        return {
            "error": "Unauthorized deletion. You are only allowed to delete groups created by you"
        }, HTTPStatus.UNAUTHORIZED

    session: Session = current_app.db.session
    session.delete(group)
    session.commit()

    return "", HTTPStatus.NO_CONTENT
