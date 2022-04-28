from flask import Blueprint

from app.controllers import group_controller

bp = Blueprint('groups', __name__)

bp.post('/group')(group_controller.create_group)
bp.get('/groups')(group_controller.get_groups)
bp.get('group/<int:id>')(group_controller.get_group_by_id)
bp.patch('group/<int:id>')(group_controller.update_group)
bp.delete('group/<int:id>')(group_controller.delete_group)
