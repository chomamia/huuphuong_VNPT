from flask_pymongo import PyMongo
from flask import request, jsonify, make_response
from library.extension import db, mail
from library.library_ma import  SchemaNews, CustomerNews, SchemagetNews
from flask import current_app, g
from werkzeug.local import LocalProxy
import jwt
from datetime import datetime
from functools import wraps
from datetime import datetime
import uuid
from itertools import chain
import imgbbpy

news_schema = SchemaNews()
news_schemas = SchemaNews(many= True)
get_news_schemas = SchemagetNews(many=True)
get_news_schema = SchemagetNews()

def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = PyMongo(current_app).db
    return db

db = LocalProxy(get_db)

def add_news_service():
    token = None
    if "Authorization" in request.headers:
        token = request.headers["Authorization"].split(" ")[1]
    if not token:
        return jsonify({'message' : 'Token is missing !!'}), 401
    if not db.blacklist_token.find_one({"token": token}):
        data = request.json
        data = CustomerNews().load(data)
        token_decode = jwt.decode(token, 'member', algorithms='HS256')
        if data and ("title" in data) and ("name_category" in data) and ("URL" in data) and ("status" in data):
            title = data["title"]
            name_category = data["name_category"]
            URL_local = data["URL"]
            status = data["status"]
            client = imgbbpy.SyncClient('f27f4dff286642132235d3ae1eb5c7dc')
            image = client.upload(file=URL_local)
            URL = image.url
            time = datetime.now()
            view = 0
            news = {
                "id_member": token_decode["public_id"],
                "id_news": str(uuid.uuid4()),
                "title" : title,
                "name_category" : name_category,
                "URL_local": URL_local,
                "URL": URL,
                "status": status,
                "time" : time,
                "view" : view
            }
            try:
                db.news.insert_one(news)
                return "Thêm tin bài thành công!"
            except:
                return "Thêm tin bài thất bại!"
        else:
            return "Vùi lòng nhập đầy đủ !"

def get_news_service():
    token = None
    if "Authorization" in request.headers:
        token = request.headers["Authorization"].split(" ")[1]
    if not token:
        return jsonify({'message' : 'Token is missing !!'}), 401
    if not db.blacklist_token.find_one({"token": token}):
        data = request.json
        if not "search" in data and not "start_date" in data and not "end_date" in data:
            return get_news_schemas.jsonify(db.news.find())
        if not "search" in data and "start_date" in data:
            if "end_date" in data:
                news = db.news.find({
                "time": {
                "$gt" :datetime.strptime(data["start_date"], '%Y-%m-%d'),
                "$lt" :datetime.strptime(data["end_date"],  '%Y-%m-%d')
                }
                })
                return get_news_schemas.jsonify(news)
            else:
                news = db.news.find({
                "time": {
                "$gt" :datetime.strptime(data["start_date"], '%Y-%m-%d'),
                "$lt" :datetime.now()
                }
                })
                return get_news_schemas.jsonify(news)
        if "search" in data:
            title = db.news.find({"title": data["search"]})
            if "start_date" in data:
                if "end_date" in data:
                    news = db.news.find({
                    "time": {
                    "$gt" :datetime.strptime(data["start_date"], '%Y-%m-%d'),
                    "$lt" :datetime.strptime(data["end_date"],  '%Y-%m-%d')
                    }
                    })
                else:
                    news = db.news.find({
                    "time": {
                    "$gt" :datetime.strptime(data["start_date"], '%Y-%m-%d'),
                    "$lt" :datetime.now()
                    }
                    })
                data_news = []
                for x in title:
                    if x in news:
                        data_news.append(x)
                return get_news_schemas.jsonify(data_news)
            else:
                return get_news_schemas.jsonify(title)
    else:
        return "Vui lòng đăng nhập để tiếp tục "


def edit_news_service(id):
    token = None
    if "Authorization" in request.headers:
        token = request.headers["Authorization"].split(" ")[1]
    if not token:
        return jsonify({'message' : 'Token is missing !!'}), 401
    if not db.blacklist_token.find_one({"token": token}):
        data = request.json
        data = CustomerNews().load(data)
        token_decode = jwt.decode(token, 'member', algorithms='HS256')
        if data and ("title" in data) and ("name_category" in data) and ("URL" in data) and ("status" in data):
            news = {"id_news" : id}
            time = datetime.now()
            new_news = { "$set": {
                "id_member": token_decode["public_id"],
                "title" : data["title"],
                "name_category" : data["name_category"],
                "URL_local": data["URL"],
                "status": data["status"],
                "time" : time
            }}
            try:
                db.news.update_one(news, new_news)
                return "Cập nhật tin bài thành công!"
            except: 
                return "Cập nhật tin bài không thành công!"
        else:
            return "Vùi lòng nhập đầy đủ !"

def detail_news_service(id):
    token = None
    if "Authorization" in request.headers:
        token = request.headers["Authorization"].split(" ")[1]
    if not token:
        return jsonify({'message' : 'Token is missing !!'}), 401
    if not db.blacklist_token.find_one({"token": token}):
        data = db.news.find_one({"id_news": id})
        if data:
            return news_schema.jsonify(data)
        else:
            return "Không tìm thấy tin bài!"
    else:
        return "Vui lòng đăng nhập để tiếp tục!"

def delete_news_service(id):
    token = None
    if "Authorization" in request.headers:
        token = request.headers["Authorization"].split(" ")[1]
    if not token:
        return jsonify({'message' : 'Token is missing !!'}), 401
    if not db.blacklist_token.find_one({"token": token}):
        data = db.news.find_one({"id_news": id})
        if data:
            db.news.delete_one(data)
            return "Xóa thành công tin bài!"
        else:
            return "Xóa  không thành công tin bài"
    else:
        return "Vui lòng đăng nhập để tiếp tục!"
