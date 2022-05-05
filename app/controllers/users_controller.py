from http import HTTPStatus

from flask import current_app
from flask import jsonify
from flask import request
from flask import url_for
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_mail import Message
from itsdangerous import URLSafeTimedSerializer
from psycopg2.errors import UniqueViolation
from psycopg2.errors import IntegrityError
from sqlalchemy.orm import Query
from sqlalchemy.orm import Session

from app.exceptions import IdNotFoundError
from app.exceptions import InvalidEmailError
from app.models import GroupModel
from app.models import UserModel
from app.models import users_groups_table
from app.services import check_mandatory_keys
from app.services import check_user_data
from app.services import check_value_type
from app.services import get_by_id
from app.services import normalize_data

s = URLSafeTimedSerializer('Thisisasecret!')


def create_user():

    data = request.get_json()

    received_keys, valid_keys, invalid_keys = check_user_data(data)

    if invalid_keys:
        return {
            'invalid_keys': list(invalid_keys),
            'valid_keys': list(valid_keys),
        }, HTTPStatus.BAD_REQUEST

    if check_mandatory_keys(data):
        return {
            'error': 'name, email and password are mandatory keys'
        }, HTTPStatus.BAD_REQUEST

    if check_value_type(data):
        return {'error': 'all values must be strings'}, HTTPStatus.BAD_REQUEST
    try:
        normalize_data(data)
        session: Session = current_app.db.session
        data['is_validate'] = False
        new_user = UserModel(**data)

        session.add(new_user)
        session.commit()

        # validates_email(new_user.email)

        return jsonify({'msg': 'verify you email!'}), HTTPStatus.CREATED

    except InvalidEmailError:
        return {'error': 'Error'}, HTTPStatus.BAD_REQUEST

    except IntegrityError as err:
        if isinstance(err.orig, UniqueViolation):
            return {'error': 'Email is already exists'}, HTTPStatus.CONFLICT


@jwt_required()
def get_user():
    users = UserModel.query.all()

    return jsonify(users), HTTPStatus.OK


@jwt_required()
def att_user(id):
    try:
        session: Session = current_app.db.session
        data: dict = request.get_json()
        user_auth = get_jwt_identity()

        user: Query = (
            session.query(UserModel)
            .filter_by(id=user_auth['id'])
            .filter_by(id=id)
            .first()
        )

        if not user:
            return {'error': 'User not found'}, HTTPStatus.NOT_FOUND

        for key, values in data.items():
            setattr(user, key, values)

        session.commit()

        return jsonify(user), HTTPStatus.OK

    except:
        return {
            'invalid_email': 'Past email should have a format similar to: something@something.com'
        }, HTTPStatus.BAD_REQUEST


@jwt_required()
def delete_user(id):
    # try:
    session: Session = current_app.db.session
    user_auth = get_jwt_identity()
    print(f'{user_auth["id"]=}')

    user: Query = session.query(UserModel).get(id)
    print(f'{user=}')

    if not user:
        return {'error': 'User not found'}, HTTPStatus.NOT_FOUND

    group_owner: Query = session.query(GroupModel).get(id)
    # group_owner: Query = (
    #     session.query(users_groups_table)
    #     .filter_by(user_id=user_auth['id'])
    #     .first()
    # )


    print(f'{group_owner=}')
    # if not group_owner:
    #     session.delete(user)
    #     session.commit()
    #     print('EEEEEEEEEUUUUUUUU')
    # else:
    #     return {
    #         'error': 'Before deleting your account, delete the groups associated with it'
    #     }, HTTPStatus.UNPROCESSABLE_ENTITY

    # return ''
    return '', HTTPStatus.NO_CONTENT
    # except:
    #     return {'error': 'error'}, HTTPStatus.BAD_REQUEST
    # group=[GroupModel(id=5, name='Mens 1', description='Mens group formmed',
    # users=[UserModel(id=10, name='Leandro Medvedev', email='leandromedvedev@hotmail.com', skills=[], works=[])],
    # user=UserModel(id=10, name='Leandro Medvedev', email='leandromedvedev@hotmail.com', skills=[], works=[]),
    # remark=[])]
    # print(f'{group=}')

@jwt_required()
def get_user_by_id(id):
    try:
        user = get_by_id(UserModel, id)
    except IdNotFoundError:
        return {'error': 'User not found'}, HTTPStatus.NOT_FOUND

    return jsonify(user), HTTPStatus.OK


def confirm_email(token):
    session: Session = current_app.db.session
    email = s.loads(token, salt='email-confirm', max_age=3600)

    user = session.query(UserModel).filter_by(email=email).first()
    print(f'{user=}')

    if user.is_validate:
        return '<h1>Email já foi confirmado.</h1>'

    setattr(user, 'is_validate', True)

    session.commit()

    return '<h1>Email confirmado.</h1>'


def validates_email(email):

    token = s.dumps(email, salt='email-confirm')

    msg = Message(
        'Confirm Email', sender='codebygirls5@gmail.com', recipients=[email]
    )

    link = url_for('.confirm_email', token=token, _external=True)

    msg.body = f'Your link is {link}'

    current_app.mail.send(msg)

    return ''
