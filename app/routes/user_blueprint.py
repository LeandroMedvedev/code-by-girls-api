from app.controllers.users_controller import (
    att_user,
    create_user,
    delete_user,
    get_user,
    get_user_by_id,
)
from flask import Blueprint

bp_user = Blueprint('users', __name__, url_prefix='/users')
bp_user.post('')(create_user)
bp_user.get('')(get_user)
bp_user.patch('<int:id>')(att_user)
bp_user.delete('<int:id>')(delete_user)
bp_user.get('/<int:id>')(get_user_by_id)
