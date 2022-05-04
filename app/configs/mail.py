from flask import Flask
from flask_mail import Mail

mail = Mail()


def init_app(app: Flask):
    app.config.from_pyfile('config.cfg')
    mail.init_app(app)
    app.mail = mail
