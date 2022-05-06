from app.configs import db

users_groups_table = db.Table(
    'users_groups',
    db.Column('id', db.Integer, primary_key=True),
    db.Column(
        'user_id', db.Integer, db.ForeignKey('users.id', ondelete='CASCADE')
    ),
    db.Column(
        'group_id', db.Integer, db.ForeignKey('groups.id', ondelete='CASCADE')
    ),
)
