from functools import wraps

from flask import url_for, session, g, jsonify
from flask_restful import Resource, fields, marshal_with, request
from werkzeug.utils import redirect

from api_app import db
from models import Book,User
from utils.restful_utils import restful_result,success,sign_in


# def check_user():
#     g.user_id=None
#     logged = False
#     if "user_id" in session:
#         user_id = session.get("user_id")
#         if user_id:
#             user = User.query.get(user_id)
#             g.user_id = user.id
#             logged = True
#
#     return logged

def check_user(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        g.user_id = None
        logged = False
        if "user_id" in session:
            user_id = session.get("user_id")
            if user_id:
                user = User.query.get(user_id)
                g.user_id = user.id
                logged = True

        if not logged:
            return sign_in()

        return func(*args,**kwargs)

    return wrapper

class BookListApi(Resource):
    method_decorators = [check_user]

    resource_fields = {
        'id': fields.Integer,
        'name': fields.String,
        'category': fields.String,
        'price': fields.Float,
    }

    # @marshal_with(resource_fields)
    def get(self):
        """
          书籍列表
          ---
          tags:
            - 书籍相关接口
          description:
             书籍列表接口，json格式

          responses:
            200:
              description: 获取书籍列表成功
              schema:
                id: 所有书籍列表
                properties:
                  name:
                    type: string
                    description: 书名
                    # example: Python Cookbook
                  id:
                    type: integer
                    description: 书号
                    # example:1
                  category:
                    type: string
                    description: 类别
                    # example: programming
                  price:
                    type: float
                    description: 价格
                    # example: 10.50

            401:
              description: 登录状态有误
        """
        books = db.session.query(Book).filter(Book.user_id==g.user_id).all()
        data = [i.to_dict() for i in books]
        return success(data=data)

class BookIDApi(Resource):
    method_decorators = [check_user]

    resource_fields = {
        'id': fields.Integer,
        'name': fields.String,
        'category': fields.String,
        'price': fields.Float,
    }

    # @marshal_with(resource_fields)
    def get(self, id):
        """
          书籍查询
          ---
          tags:
            - 书籍相关接口
          description:
             书籍查询接口，json格式

          responses:
            200:
              description: 获取书籍成功
              schema:
                id: 所有书籍列表
                properties:
                  name:
                    type: string
                    description: 书名
                    # example: Python Cookbook
                  id:
                    type: integer
                    description: 书号
                    # example:1
                  category:
                    type: string
                    description: 类别
                    # example: programming
                  price:
                    type: float
                    description: 价格
                    # example: 10.50

            401:
              description: 没有权限
        """
        # check_user()
        book = db.session.query(Book).get(id)
        if book and book.user_id==g.user_id:
            return success(data=book.to_dict())
        else:
            return restful_result(None,"-1","Not authorized to check this book!")

    def delete(self, id):
        """
          书籍删除
          ---
          tags:
            - 书籍相关接口
          description:
             书籍删除接口，json格式
          responses:
            201:
              description: 删除书籍成功
            401:
              description: 没有权限
        """
        book = db.session.query(Book).get(id)
        if book.user_id==g.user_id:
            book.status="0"
            db.session.commit()

            return restful_result(message="删除书籍成功！",data=book.to_dict())

    def put(self, id):
        """
          书籍修改
          ---
          tags:
            - 书籍相关接口
          description:
             书籍修改接口，json格式
          responses:
            201:
              description: 修改书籍成功
            401:
              description: 没有权限
        """
        params = request.get_json()
        book = db.session.query(Book).get(id)
        price = params.get("price")

        # check_user()
        if book.user_id == g.user_id:
            book.price = price
            db.session.commit()

            return success(message="修改价格成功!",data=book.to_dict())


class BookApi(Resource):
    method_decorators = [check_user]

    resource_fields = {
        'id': fields.Integer,
        'name': fields.String,
        'category': fields.String,
        'price': fields.Float,
    }

    def post(self):
        """
          书籍添加
          ---
          tags:
            - 书籍相关接口
          description:
             书籍添加接口，json格式
          responses:
            201:
              description: 添加书籍成功
            401:
              description: 没有权限
        """
        params = request.get_json()
        # check_user()
        name = params.get("name")
        category = params.get("category")
        price = params.get("price")

        book = Book(name=name, category=category, price=price,user_id=g.user_id)

        db.session.add(book)
        db.session.commit()

        return success(message="新增一本书籍成功", data=book.to_dict())

