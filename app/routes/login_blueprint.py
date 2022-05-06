from flask import Blueprint

from app.controllers import login_controllers

bp_login = Blueprint('login', __name__, url_prefix='/login')
bp_login.post('')(login_controllers.login)
