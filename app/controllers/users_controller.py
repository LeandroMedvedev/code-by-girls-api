import json
from flask import request, current_app, jsonify
from flask_jwt_extended import get_jwt_identity
from models.user_model import UserModel

def create_user():
    try:
        data = request.get_json()
        session = current_app.db.session
        new_user =  UserModel(**data)

        session.add(new_user)
        session.commit()


        return jsonify(new_user),201
    except:
        ...

def get_user():
    users=(
        UserModel.query.all()
    )

    return jsonify(users), 200