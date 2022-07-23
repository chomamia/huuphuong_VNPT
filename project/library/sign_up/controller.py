from cgitb import html
from crypt import methods
from textwrap import wrap
from flask import Blueprint, render_template, request
from .services import signup_service, signin_service, forget_password_service, very_acc_service, reset_password_service

members = Blueprint("member", __name__)

@members.route("/signup", methods = ["POST"])
def signup():
    return signup_service()

@members.route("/signin", methods = ["POST"])
def signin():
    return signin_service()

@members.route("/forget_password", methods=["POST"])
def forget_password():
    return forget_password_service()

@members.route("/very_acc", methods=["POST"])
def very_acc():
    return very_acc_service()

@members.route("/reset_password", methods=["PUT"])
def reset_password():
    return reset_password_service()