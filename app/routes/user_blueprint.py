from flask import Blueprint
from app.controllers.users_controller import create_user, get_user, att_user, delete_user, get_user_by_id, validates_email, confirm_email

bp_user = Blueprint("users", __name__, url_prefix='/users')
bp_user.post("")(create_user)
bp_user.get("")(get_user)
bp_user.patch("<int:id>")(att_user)
bp_user.delete("<int:id>")(delete_user)
bp_user.get('/<int:id>')(get_user_by_id)

bp_user.get("/confirm_email/<token>")(confirm_email)

bp_user.post("/send")(validates_email)
