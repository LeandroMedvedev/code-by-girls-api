from flask import Blueprint
from app.controllers import comment_user_group

bp = Blueprint('comments', __name__, url_prefix='/comments')

bp.get('')(comment_user_group.get_all)
bp.get('/<int:id>')(comment_user_group.get_by_id)
bp.post('/<int:id>')(comment_user_group.create)
bp.patch('/<int:id>')(comment_user_group.update)
bp.delete('/<int:id>')(comment_user_group.delete)
