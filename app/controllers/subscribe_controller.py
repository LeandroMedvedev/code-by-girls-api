from http import HTTPStatus
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy.orm import Session, Query
from flask import request, current_app, jsonify

from app.models.group_model import GroupModel
from app.models.user_model import UserModel
from app.models.user_group_table import users_groups_table
from ipdb import set_trace


@jwt_required()
def get_subscribe():
    session: Session = current_app.db.session
    user_auth = get_jwt_identity()

    query: Query = (
        session
        .query(GroupModel)
        .select_from(users_groups_table)
        .filter_by(user_id=user_auth["id"])
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

    groups: GroupModel = (
        session
        .query(GroupModel)
        .get(data["group_id"])
    )

    users = (
        session
        .query(UserModel)
        .get(user_auth["id"])
    )

    groups.users.append(users)

    session.add(groups)
    session.commit()

    return jsonify(groups)


@jwt_required()
def delete_subscribe(id: int):
    session: Session = current_app.db.session
    user_auth = get_jwt_identity()

    query: Query = (
        session
        .query(GroupModel)
        .select_from(users_groups_table)
        .filter_by(user_id=user_auth["id"])
        .filter_by(group_id=id)
        .first()
    )

    print(query)

    # session.delete(query)
    # session.commit()

    # return "", HTTPStatus.NO_CONTENT
    return jsonify(query)

    # query: Query = (
    #     session
    #     .query(GroupModel)
    #     .select_from(users_groups_table)
    #     .filter_by(user_id=user_auth["id"])
    #     .join(GroupModel)
    #     .filter_by(id=id)
    #     .join(UserModel)
    #     .first()
    # )

    # if query:
    # groups: GroupModel = (
    # session
    # .query(GroupModel)
    # .get(data["group_id"])
    # )

    # users = (
    #     session
    #     .query(UserModel)
    #     .get(user_auth["id"])
    # )

    # groups.users.append(users)

    # set_trace()

    # for user in query.users:
    #     if user.id == user_auth["id"]:
    #         print(query.user.remove(user))

    # session.commit()

    # data = request.get_json()

    # user: UserModel = UserModel.query.filter_by(id=user_auth["id"]).first()

    # group: GroupModel = GroupModel.query.get(id)

    # group.users.remove(user)

    # print(teste)
    # session.commit()

    # return jsonify(group)
