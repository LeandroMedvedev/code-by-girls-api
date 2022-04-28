from flask import current_app
from sqlalchemy.orm import Session

from app.exceptions import IdNotFoundError


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
