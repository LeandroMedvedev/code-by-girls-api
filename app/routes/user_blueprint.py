from flask import Blueprint

from app.controllers import users_controller


bp_user = Blueprint('users', __name__, url_prefix='/users')
bp_user.post('')(users_controller.create_user)
bp_user.get('')(users_controller.get_user)
bp_user.patch('<int:id>')(users_controller.att_user)
bp_user.delete('<int:id>')(users_controller.delete_user)
bp_user.get('/<int:id>')(users_controller.get_user_by_id)

bp_user.get('/confirm_email/<token>')(users_controller.confirm_email)

bp_user.post('/send')(users_controller.validates_email)
