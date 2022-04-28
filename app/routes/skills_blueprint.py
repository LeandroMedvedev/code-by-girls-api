from flask import Blueprint
from app.controllers.skill_controller import create_skill,get_skill,atualize_skill,delete_skill,get_skill_id

bp_skill = Blueprint("skills", __name__, url_prefix ='/users')

bp_skill.post("/skills")(create_skill)
bp_skill.get("/skills")(get_skill)
bp_skill.patch("/skills/<int:id>")(atualize_skill)
bp_skill.delete("/skills/<int:id>")(delete_skill)
bp_skill.get("/skills/<int:id>")(get_skill_id)