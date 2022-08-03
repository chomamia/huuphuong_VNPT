from flask_pymongo import PyMongo
from flask import request, jsonify, make_response
from library.extension import db, mail
from library.library_ma import  SchemaNews, Schemagetnewpost
from flask import current_app, g
from werkzeug.local import LocalProxy
import jwt
from datetime import datetime
from functools import wraps
from datetime import datetime
import uuid
from itertools import chain
import imgbbpy


new_post_schema = Schemagetnewpost()
new_post_schemas = Schemagetnewpost(many= True)

def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = PyMongo(current_app).db
    return db

db = LocalProxy(get_db)

def get_new_post_service():
    token = None
    if "Authorization" in request.headers:
        token = request.headers["Authorization"].split(" ")[1]
    if not token:
        return jsonify({'message' : 'Token is missing !!'}), 401
    if not db.blacklist_token.find_one({"token": token}):
        data = db.news.find().sort('time')
        new_post = []
        for x in data:
            member = db.member.find_one({'public_id': x['id_member']})
            user_name = member['user_name']
            post = {
                'title' : x['title'],
                'user_name': user_name,
                'time': x['time'],
                'name_category': x['name_category'],
                'views' : x['view']
            }
            new_post.append(post)
        return new_post_schemas.jsonify(new_post)
    else:
        return "Vui lòng đăng nhập để tiếp tục"

def get_category_post_service(name_category):
    token = None
    if "Authorization" in request.headers:
        token = request.headers["Authorization"].split(" ")[1]
    if not token:
        return jsonify({'message' : 'Token is missing !!'}), 401
    if not db.blacklist_token.find_one({"token": token}):
        data = db.news.find({'name_category': name_category}).sort('time')
        new_post = []
        for x in data:
            member = db.member.find_one({'public_id': x['id_member']})
            user_name = member['user_name']
            post = {
                'title' : x['title'],
                'user_name': user_name,
                'time': x['time'],
                'name_category': x['name_category'],
                'views' : x['view']
            }
            new_post.append(post)
        return new_post_schemas.jsonify(new_post)
    else:
        return "Vui lòng đăng nhập để tiếp tục"

def get_author_post_service(user_name):
    token = None
    if "Authorization" in request.headers:
        token = request.headers["Authorization"].split(" ")[1]
    if not token:
        return jsonify({'message' : 'Token is missing !!'}), 401
    if not db.blacklist_token.find_one({"token": token}):
        member = db.member.find_one({'user_name': user_name})
        data = db.news.find({'id_member': member['public_id']}).sort('time')
        new_post = []
        for x in data:
            member = db.member.find_one({'public_id': x['id_member']})
            user_name = member['user_name']
            post = {
                'title' : x['title'],
                'user_name': user_name,
                'time': x['time'],
                'name_category': x['name_category'],
                'views' : x['view']
            }
            new_post.append(post)
        return new_post_schemas.jsonify(new_post)
    else:
        return "Vui lòng đăng nhập để tiếp tục"

