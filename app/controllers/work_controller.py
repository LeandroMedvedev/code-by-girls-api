from http import HTTPStatus
from app.configs.database import db
from app.models.work_model import WorkModel
from flask import jsonify, request
from sqlalchemy.orm.session import Session
from sqlalchemy.orm import Query


def create_work():
    data = request.get_json()

    session: Session = db.session
    work = WorkModel(**data)
    session.add(work)
    session.commit()

    return jsonify(work), HTTPStatus.CREATED
    

def get_work():
    works: Query =db.session.query(WorkModel).all()

    return jsonify(works), HTTPStatus.OK


def delete_work(work_id):

    query = WorkModel.query.get(work_id)
    session : Session = db.session
    session.delete(query)
    session.commit()

    return "", HTTPStatus.NO_CONTENT


def patch_work(work_id):

    session : Session = db.session
    data = request.get_json()
    work_changed = WorkModel.query.get(work_id)

    for key, values in data.items():
        setattr(work_changed, key, values)
    
    session.add(work_changed)
    session.commit()

    return jsonify(work_changed),HTTPStatus.OK

