from flask import request, jsonify
from models.user_model import UserModel
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

    return jsonify(users), 200