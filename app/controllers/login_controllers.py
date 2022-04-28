from datetime import timedelta
from http import HTTPStatus
from flask import current_app, request
from sqlalchemy.orm import Session
from app.models.user_model import UserModel
from flask_jwt_extended import create_access_token


def login():
    session: Session = current_app.db.session
    data = request.get_json()
    new_data = {
        "email": data["email"],
        "password_hash": data["password"]
    }

    print(data)

    user: UserModel = session.query(UserModel).filter_by(email=data["email"]).first()

    if not user:
        return {"error": "user not found!"}, HTTPStatus.NOT_FOUND

    
    if user.verify_password(new_data["password_hash"]):
        data = {
            "id": user.id,
            "name": user.name,
            "email": user.email
        }

        accessToken = create_access_token(identity=data, expires_delta=timedelta(days=1))
        return {"token": accessToken, "user": data}, HTTPStatus.OK
    else:
        return {"error": "Unauthorized"}, HTTPStatus.UNAUTHORIZED