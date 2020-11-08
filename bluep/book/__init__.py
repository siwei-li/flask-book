
from flask import Blueprint
from flask_restful import Api

index_blu = Blueprint('index', __name__,url_prefix="/books")
index_api = Api(index_blu)

from .api_book import BookIDApi, BookListApi,BookApi

index_api.add_resource(BookIDApi, '/book/<int:id>')
index_api.add_resource(BookApi, '/book')
index_api.add_resource(BookListApi, '')
