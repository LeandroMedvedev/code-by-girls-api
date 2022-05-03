from http import HTTPStatus
from flask import current_app, jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from sqlalchemy.orm import Session, Query
from app.models.comment_user_group_table import CommentUserGroupModel
from datetime import datetime
from ipdb import set_trace

from app.models.group_model import GroupModel
from app.models.user_model import UserModel
from app.models.user_group_table import users_groups_table


@jwt_required()
def get_all():
    session: Session = current_app.db.session

    comments: CommentUserGroupModel = session.query(
        CommentUserGroupModel).all()

    return jsonify(comments), HTTPStatus.OK


@jwt_required()
def get_by_id(id: int):
    comment = (CommentUserGroupModel.query.get(id))
    if comment == None:
            return{"msg": "Non-existent comment"},HTTPStatus.NOT_FOUND
    return jsonify(comment),HTTPStatus.OK


@jwt_required()
def created():
    user_auth = get_jwt_identity()
    session: Session = current_app.db.session
    data: dict = request.get_json()
    dt = datetime.now()
    data["timestamp"] = dt
    data["user_id"] = user_auth["id"]

    try:
        query: Query = (
            session
            .query(GroupModel)
            .select_from(users_groups_table)
            .filter_by(user_id=user_auth["id"])
            .join(GroupModel)
            .join(UserModel)
            .all()
        )

        if query:

            comment = CommentUserGroupModel(**data)

            session.add(comment)
            session.commit()

            return jsonify(comment), HTTPStatus.CREATED

        return {"error": "To post a comment, you must be subscribed to a group"}, HTTPStatus.UNAUTHORIZED

    except TypeError:
        expected = ["comments", "timestamp", "user_id", "group_id"]
        obtained = [key for key in data.keys()]
        return {"expected": expected, "obtained": obtained}, HTTPStatus.BAD_REQUEST


@jwt_required()
def update(id: int):
    
        session: Session = current_app.db.session 
        data:dict = request.get_json()
        user = get_jwt_identity()
        comment = CommentUserGroupModel.query.get(id)
        
        if comment == None:
            return{"msg": "Non-existent comment"},HTTPStatus.NOT_FOUND
        
        if user["id"]!= comment.user_id:
            return{"msg": "It is possible to update only your comments"},HTTPStatus.BAD_REQUEST

        for key, value in data.items():
            if key == "comments":
                setattr(comment, key, value)

                session.add(comment)
                session.commit()
                return jsonify(comment), HTTPStatus.OK
            else:
                return {"error": "You can only update the comments field"}, HTTPStatus.BAD_REQUEST


@jwt_required()
def delete(id: int):
    comment = CommentUserGroupModel.query.get(id)
    session = current_app.db.session
    user = get_jwt_identity()
    if comment == None:
        return{"msg": "Non-existent comment"},HTTPStatus.NOT_FOUND
    if user["id"] != comment.user_id:
        return{"msg": "It is possible to delete only your comments"},HTTPStatus.BAD_REQUEST
        
    session.delete(comment)
    session.commit()
    return "", HTTPStatus.NO_CONTENT
