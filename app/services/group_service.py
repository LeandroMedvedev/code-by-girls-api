from flask import current_app
from flask_jwt_extended import get_jwt_identity
from sqlalchemy.orm import Session

from app.exceptions import IdNotFoundError
from app.exceptions import UserUnauthorizedError


def check_data(data: dict):
    received_keys = set(data.keys())
    valid_keys = {"name", "description"}
    invalid_keys = received_keys.difference(valid_keys)

    return received_keys, valid_keys, invalid_keys


def get_by_id(model: object, id: int):
    session: Session = current_app.db.session

    query = session.query(model).get(id)

    if not query:
        raise IdNotFoundError

    return query


def is_authorized(group_creator: int):
    user_auth = get_jwt_identity()

    if user_auth["id"] != group_creator:
        raise UserUnauthorizedError
