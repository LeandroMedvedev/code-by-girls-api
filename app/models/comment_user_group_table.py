from app.configs import db


comments_users_groups_table = db.Table("comments_users_groups", 
    db.Column("id", db.Integer, primary_key=True),
    db.Column("user_id", db.Integer, db.ForeignKey("users.id")),
    db.Column("group_id", db.Integer, db.ForeignKey("groups.id")),
    db.Column("comments", db.Text),
    db.Column("timestemp", db.Date),
)
