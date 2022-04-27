from flask import current_app, request, jsonify
from app.models.user_model import UserModel
from http import HTTPStatus
from psycopg2.errors import UniqueViolation
from sqlalchemy.exc import IntegrityError
from app.exceptions import InvalidEmailError
from sqlalchemy.orm import Session, Query
from flask_jwt_extended import jwt_required, get_jwt_identity

def create_user():
    try:
        data = request.get_json()
        session : Session = current_app.db.session

        new_user =  UserModel(**data)

        session.add(new_user)
        session.commit()

        return jsonify(new_user),HTTPStatus.CREATED

    except InvalidEmailError:
            return{"error":"Error"}, HTTPStatus.BAD_REQUEST

    except IntegrityError as e:
        if type(e.orig) == UniqueViolation:

            return {"error": "EMAIL is alredy exists"}, HTTPStatus.CONFLICT


@jwt_required()
def get_user():
    users=(
        UserModel.query.all()
    )

    return jsonify(users), HTTPStatus.OK


@jwt_required()
def att_user(id):
    try:
        session : Session = current_app.db.session
        data:dict = request.get_json()
        user_auth = get_jwt_identity()

        user: Query = (
            session
            .query(UserModel)
            .filter_by(id=user_auth["id"])
            .filter_by(id=id)
            .first()
        )

        if not user:
            return {"error": "id not found"}, HTTPStatus.NOT_FOUND


        for key,values in data.items():
            setattr(user,key,values)
        
        session.commit()

        return jsonify(user),HTTPStatus.OK


    except:
        return {"error": "error"}, HTTPStatus.BAD_REQUEST


@jwt_required()
def delete_user(id):
    try:
        session : Session = current_app.db.session
        user_auth = get_jwt_identity()

        user: Query = (
            session
            .query(UserModel)
            .filter_by(id=user_auth["id"])
            .filter_by(id=id)
            .first()
        )

        if not user:
            return {"error": "id not found"}, HTTPStatus.NOT_FOUND

        session.delete(user)
        session.commit()

        return "", HTTPStatus.NO_CONTENT
    except:
        return {"error": "error"}, HTTPStatus.BAD_REQUEST