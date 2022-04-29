from http import HTTPStatus
from flask import current_app, jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from sqlalchemy.orm import Session, Query
from app.models.comment_user_group_table import CommentUserGroupModel
from datetime import datetime


@jwt_required()
def get_all():
    ...


@jwt_required()
def get_by_id(id: int):
    ...


@jwt_required()
def created():
    session: Session = current_app.db.session
    data: dict = request.get_json()
    dt = datetime.now()
    data["timestamp"] = dt

    try:

        comment = CommentUserGroupModel(**data)

        session.add(comment)
        session.commit()

        return jsonify(comment), HTTPStatus.CREATED
    except TypeError:
        expected = ["comments", "timestamp", "user_id", "group_id"]
        obtained = [key for key in data.keys()]
        return {"expected": expected, "obtained": obtained}, HTTPStatus.BAD_REQUEST


@jwt_required()
def update(id: int):
    ...


@jwt_required()
def delete(id: int):
    ...
