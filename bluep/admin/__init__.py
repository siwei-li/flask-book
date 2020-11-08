from flask import Blueprint
from flask_restful import Api

# 创建蓝图对象,设置访问前缀,所有的访问该蓝图的请求都需要加上/passport
admin_blu = Blueprint("admin", __name__, url_prefix="/passport")
admin_api = Api(admin_blu)

from .api_portal import RegisterApi, SignInApi

# 如果不写endpoint，那么将会使用视图的名字的小写来作为endpoint
admin_api.add_resource(RegisterApi, '/register',endpoint="register")
admin_api.add_resource(SignInApi, '/signin',endpoint="signin")
