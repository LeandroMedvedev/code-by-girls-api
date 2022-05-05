from app.controllers import work_controller
from flask import Blueprint

bp_work = Blueprint('works', __name__, url_prefix='/users/works')

bp_work.post('')(work_controller.create_work)

bp_work.get('')(work_controller.get_work)

bp_work.patch('/<int:work_id>')(work_controller.patch_work)

bp_work.delete('/<int:work_id>')(work_controller.delete_work)

bp_work.get('/<int:work_id>')(work_controller.get_work_to_id)
