from crypt import methods
from flask import Blueprint
from .services import (add_staff_service, get_staff_service, update_staff_by_id_service, delete_staff_by_id_service,
                      get_staff_by_id_service)
from flask_mail import Mail, Message


staffs = Blueprint("staff", __name__)

@staffs.route("/staff-management/staff", methods = ["POST"])
def add_staff():
    return add_staff_service()

@staffs.route("/staff-management/staffs", methods = ["GET"])
def get_staff():
    return get_staff_service()

@staffs.route("/staff-management/staff/<int:id>", methods = ["GET"])
def get_staff_by_id(id):
    return get_staff_by_id_service(id)

@staffs.route("/staff-management/staff/<int:id>", methods = ["PUT"])
def update_staff_by_id(id):
    return update_staff_by_id_service(id)

@staffs.route("/staff-management/staff/<int:id>", methods = ["DELETE"])
def delete_staff_by_id(id):
    return delete_staff_by_id_service(id)

