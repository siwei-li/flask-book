from flask import session, current_app, jsonify
from flask_restful import Resource, fields, marshal_with, request
from werkzeug.utils import redirect

from api_app import db
from models import Book,User
from utils.restful_utils import restful_result,success,sign_in

class RegisterApi(Resource):
    resource_fields = {
        'mobile': fields.String,
        'nickname': fields.String,
    }

    # @marshal_with(resource_fields)
    def post(self):
        """
          用户注册
          ---
          tags:
            - 用户相关接口
          description:
              用户注册接口，json格式
          parameters:
            - name: body
              in: body
              required: true
              schema:
                id: 用户注册
                required:
                  - nickname
                  - password
                  - mobile
                properties:
                  nickname:
                    type: string
                    description: 昵称
                  password:
                    type: string
                    description: 密码
                  mobile:
                    type: string
                    description: 手机号.

          responses:
            201:
                description: 注册成功
            406:
              description: 注册参数有误

        """
        params = request.get_json()
        mobile = params.get("mobile")
        nickname = params.get("nickname")
        password = params.get("password")

        # if User.query.filter_by(mobile=mobile).first():
        #     return redirect(url_for('admin.signin'))

        user = User(mobile=mobile,nickname=nickname,password=password)

        db.session.add(user)
        db.session.commit()

        return success(message="注册成功！",data=user.to_dict())

class SignInApi(Resource):

    resource_fields = {
        'mobile': fields.String,
        'nickname': fields.String,
    }

    # @marshal_with(resource_fields)
    def post(self):
        """
          用户登录
          ---
          tags:
            - 用户相关接口
          description:
              用户登录接口，json格式
          parameters:
            - name: body
              in: body
              required: true
              schema:
                id: 用户登录
                required:
                  - password
                  - mobile
                properties:
                  password:
                    type: string
                    description: 密码
                  mobile:
                    type: string
                    description: 手机号
          responses:
            201:
              description: '登录成功'

            406:
              description: 登录参数有误
        """

        params = request.get_json()
        mobile = params.get("mobile")
        password = params.get("password")

        user = User.query.filter(User.mobile == mobile).first()
        if not user:
            return restful_result(data=None,code="-1",message="Non-existent user, please register!")

        if user.password!=password:
            return restful_result(data=None,code="-1",message="Wrong password!")

        session["user_id"] = user.id
        session["mobile"] = user.mobile
        db.session.add(user)
        db.session.commit()

        return success(message="登录成功！",data=user.to_dict())

