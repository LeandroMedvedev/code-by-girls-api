from flask import Blueprint
from app.controllers.work_controller import create_work, delete_work, get_work, patch_work

bp_work = Blueprint("works",__name__, url_prefix ='works')

bp_work.post("")(create_work)

bp_work.get("")(get_work)

bp_work.patch("/<int:work_id>")(patch_work)

bp_work.delete("/<int:work_id>")(delete_work)
