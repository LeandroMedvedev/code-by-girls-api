from flask import request, jsonify
from app.models.user_model import UserModel
from http import HTTPStatus
from psycopg2.errors import UniqueViolation
from sqlalchemy.exc import IntegrityError
from app.exceptions import InvalidEmailError
from app.configs.database import db
from sqlalchemy.orm.session import Session

def create_user():
    try:
        data = request.get_json()
        session : Session = db.session
        new_user =  UserModel(**data)

        session.add(new_user)
        session.commit()


        return jsonify(new_user),HTTPStatus.CREATED

    except InvalidEmailError:
            return{"error":"Error"}, HTTPStatus.BAD_REQUEST

    except IntegrityError as e:
        if type(e.orig) == UniqueViolation:

            return {"error": "EMAIL is alredy exists"}, HTTPStatus.CONFLICT


def get_user():
    users=(
        UserModel.query.all()
    )

    return jsonify(users), HTTPStatus.OK


def att_user(id):
    try:
        session : Session = db.session
        data = request.get_json()
        value_in_update = UserModel.query.get(id)

        for key,values in data.items():
            setattr(value_in_update,key,values)
        
        session.add(value_in_update)
        session.commit()

        return jsonify(value_in_update),HTTPStatus.OK


    except:
        ...


def delete_user(id):
    try:
        query = UserModel.query.get(id)
        session : Session = db.session
        session.delete(query)
        session.commit()
        return "",HTTPStatus.NO_CONTENT
    except:
        ...