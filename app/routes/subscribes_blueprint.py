from flask import Blueprint
from app.controllers import subscribe_controller


bp = Blueprint('subscribes', __name__, url_prefix='/groups/subscribes')


bp.get('')(subscribe_controller.get_subscribe)
bp.post('')(subscribe_controller.subscribes)
bp.delete('/<int:id>')(subscribe_controller.delete_subscribe)
