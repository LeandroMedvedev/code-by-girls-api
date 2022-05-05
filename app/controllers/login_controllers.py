from datetime import timedelta
from http import HTTPStatus

from flask import request
from flask_jwt_extended import create_access_token

from app.models import UserModel


def login():
    data = request.get_json()

    data['email'] = data['email'].lower()

    data['is_validate'] = False
    user: UserModel = UserModel.query.filter_by(email=data['email']).first()

    if not user and user.is_validate:
        if not user.is_validate:
            return {"error": "verifucar seu email."}, HTTPStatus.BAD_REQUEST
        return {'error': 'User not found!'}, HTTPStatus.NOT_FOUND

    if user.verify_password(data['password']):
        data = {'id': user.id, 'name': user.name, 'email': user.email}

        accessToken = create_access_token(
            identity=data, expires_delta=timedelta(days=1)
        )
        return {'token': accessToken, 'user': data}, HTTPStatus.OK
    else:
        return {'error': 'Unauthorized'}, HTTPStatus.UNAUTHORIZED
