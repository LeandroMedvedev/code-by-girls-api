from flask import Blueprint

from app.controllers import group_controller

bp = Blueprint('groups', __name__, url_prefix='/groups')

bp.post('')(group_controller.create_group)
bp.get('')(group_controller.get_groups)
bp.get('/<int:id>')(group_controller.get_group_by_id)
bp.patch('/<int:id>')(group_controller.update_group)
bp.delete('/<int:id>')(group_controller.delete_group)
