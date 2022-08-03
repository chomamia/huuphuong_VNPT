from hashlib import new
from flask import Blueprint
from .services import get_new_post_service, get_category_post_service, get_author_post_service

new_post = Blueprint("new_post", __name__)

@new_post.route("/get_new_post", methods = ["GET"])
def get_new_post():
    return get_new_post_service()

@new_post.route("/get_category_post/<name_category>", methods = ["GET"])
def get_category_post(name_category):
    return get_category_post_service(name_category)

@new_post.route("/get_author_post/<user_name>", methods = ["GET"])
def get_author_post(user_name):
    return get_author_post_service(user_name)