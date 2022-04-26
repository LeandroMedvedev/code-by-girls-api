from http import HTTPStatus

from flask import request, jsonify
from app.exceptions import InvalidEmailError
from app.models.user_model import UserModel
from sqlalchemy.orm.session import Session
from psycopg2.errors import UniqueViolation
from sqlalchemy.exc import IntegrityError

from app.configs.database import db


def create_user():
    data = request.get_json()

    try:
        session: Session = db.session
        user = UserModel(**data)
        session.add(user)
        session.commit()

        return jsonify(user), HTTPStatus.CREATED

    except InvalidEmailError:
        return {"error": "Error"}, HTTPStatus.BAD_REQUEST
    except IntegrityError as e:
        if type(e.orig) == UniqueViolation:
            return {"error": "EMAIL is alredy exists"}, HTTPStatus.CONFLICT
