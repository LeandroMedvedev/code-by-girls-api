from http import HTTPStatus
from wsgiref import validate
from flask_mail import Message

from app.exceptions import InvalidEmailError, IdNotFoundError
from app.models.user_model import UserModel
from app.services import get_by_id, check_user_data, check_mandatory_keys, normalize_data, check_value_type
from flask import current_app, jsonify, request, url_for
from flask_jwt_extended import get_jwt_identity, jwt_required
from psycopg2.errors import UniqueViolation
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Query, Session
from itsdangerous import URLSafeTimedSerializer, SignatureExpired

s = URLSafeTimedSerializer('Thisisasecret!')


def create_user():
    data = request.get_json()

    received_keys, valid_keys, invalid_keys = check_user_data(data)

    if invalid_keys:
        return {
            "invalid_keys": list(invalid_keys),
            "valid_keys": list(valid_keys),
        }, HTTPStatus.BAD_REQUEST

    if check_mandatory_keys(data):
        return {
            "error": "name, email and password are mandatory keys"
        }, HTTPStatus.BAD_REQUEST

    if check_value_type(data):
        return {"error": "all values must be strings"}, HTTPStatus.BAD_REQUEST

    try:
        normalize_data(data)
        session: Session = current_app.db.session

        new_user = UserModel(**data)

        session.add(new_user)
        session.commit()

        validates_email(new_user.email)

        return jsonify(new_user), HTTPStatus.CREATED

    except InvalidEmailError:
        return{"error": "Error"}, HTTPStatus.BAD_REQUEST

    except IntegrityError as e:
        if type(e.orig) == UniqueViolation:

            return {"error": "EMAIL is alredy exists"}, HTTPStatus.CONFLICT


@jwt_required()
def get_user():
    users = (
        UserModel.query.all()
    )

    return jsonify(users), HTTPStatus.OK


@jwt_required()
def att_user(id):
    try:
        session: Session = current_app.db.session
        data: dict = request.get_json()
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

        for key, values in data.items():
            setattr(user, key, values)

        session.commit()

        return jsonify(user), HTTPStatus.OK

    except:
        return {"error": "error"}, HTTPStatus.BAD_REQUEST


@jwt_required()
def delete_user(id):
    try:
        session: Session = current_app.db.session
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


@jwt_required()
def get_user_by_id(id):
    try:
        user = get_by_id(UserModel, id)
    except IdNotFoundError:
        return {"error": "User not found"}, HTTPStatus.NOT_FOUND

    return jsonify(user), HTTPStatus.OK


def confirm_email(token):
    session: Session = current_app.db.session
    user = (
        session
        .query(UserModel)
        .filter_by(email=token)
        .first()
    )

    setattr(user, "is_validate", True)
    session.commit()

    return jsonify({"msg": "user verify!"}), HTTPStatus.OK


def validates_email(email):

    token = s.dumps(email, salt='email-confirm')

    msg = Message('Confirm Email',
                  sender='codebygirls5@gmail.com', recipients=[email])

    link = url_for('.confirm_email', token=token, _external=True)

    msg.body = f'Your link is {link}'

    current_app.mail.send(msg)

    return ""
