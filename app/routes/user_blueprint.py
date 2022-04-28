from flask import Blueprint
from app.controllers.users_controller import create_user,get_user,att_user,delete_user
from app.controllers.skill_controller import create_skill,get_skill,atualize_skill,delete_skill

bp_user = Blueprint("users", __name__, url_prefix ='/users')
bp_user.post("")(create_user)
bp_user.get("")(get_user)
bp_user.patch("<int:id>")(att_user)
bp_user.delete("<int:id>")(delete_user)

bp_user.post("/skills")(create_skill)
bp_user.get("/skills")(get_skill)
bp_user.patch("/skills/<int:id>")(atualize_skill)
bp_user.delete("/skills/<int:id>")(delete_skill)
