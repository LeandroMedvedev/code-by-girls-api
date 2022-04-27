from flask import Blueprint
from app.controllers.login_controllers import login

bp_login = Blueprint("login", __name__, url_prefix ='/login')
bp_login.post("")(login)