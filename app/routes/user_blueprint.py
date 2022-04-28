from flask import Blueprint
from app.controllers.users_controller import create_user,get_user,att_user,delete_user

bp_user = Blueprint("users", __name__, url_prefix ='/users')
bp_user.post("")(create_user)
bp_user.get("")(get_user)
bp_user.patch("<int:id>")(att_user)
bp_user.delete("<int:id>")(delete_user)
