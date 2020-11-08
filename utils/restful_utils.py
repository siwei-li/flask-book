# @Time    : 2020-10-26 17:59
# @Author  : 老赵
# @File    : restful_utils.py
from flask import jsonify


class HttpCode(object):
    # ok = 200
    ok = 0
    un_auth_error = 401
    params_error = 400
    server_error = 500


# def restful_result(code, message, data):
#     return jsonify({"data": data or {},"code": code, "message": message})
#
def restful_result(data, code, message):
    return jsonify({"data": data or {},"code": code, "message": message})


def success(message="success", data=None):
    # return restful_result(data=data,code=HttpCode.ok, message=message)
    return restful_result(data=data,code="0", message=message)

def sign_in(message="Please sign in!", data=None):
    # return restful_result(data=data,code=HttpCode.ok, message=message)
    return restful_result(data=data,code="-1", message=message)
