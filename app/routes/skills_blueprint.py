from flask import Blueprint

from app.controllers import skill_controller

bp_skill = Blueprint('skills', __name__, url_prefix='/users')

bp_skill.post('/skills')(skill_controller.create_skill)
bp_skill.get('/skills')(skill_controller.get_skill)
bp_skill.patch('/skills/<int:id>')(skill_controller.update_skill)
bp_skill.delete('/skills/<int:id>')(skill_controller.delete_skill)
bp_skill.get('/skills/<int:id>')(skill_controller.get_skill_id)
