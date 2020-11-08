from flask import Flask, config
from flasgger import Swagger
from flask_sqlalchemy import SQLAlchemy

from config.config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)


# from bluep.index import index_api
# api = index_api

def create_app():
    pass

from bluep.admin import admin_blu
app.register_blueprint(admin_blu)
from bluep.book import index_blu
app.register_blueprint(index_blu)


swagger_config = Swagger.DEFAULT_CONFIG
# config = Config()
swagger_config['title'] = Config.SWAGGER_TITLE
swagger_config['description'] = Config.SWAGGER_DESC
swagger_config['host'] = Config.SWAGGER_HOST

swagger = Swagger(app, config=swagger_config)

