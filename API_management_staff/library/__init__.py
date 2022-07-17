from flask import Flask, request, Blueprint
from library.staff.controller import staffs
from .extension import db, ma, mail
import os
from flask_mail import Mail, Message


def create_db(app):
    if not os.path.exists("library/staff.db"):
        db.create_all(app=app)
        print("Created db!")

def create_app(config_file = "config.py"):
    app = Flask(__name__)
    db.init_app(app)
    ma.init_app(app)
    app.config.from_pyfile(config_file)
    mail.init_app(app)
    create_db(app)
    app.register_blueprint(staffs)
    return app