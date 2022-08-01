from decouple import config
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api

from db import db
from resources.routes import routes


class ProductionConfig:
    FLASK_ENV = "prod"
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{config('DB_USER')}:{config('DB_PASSWORD')}"
        f"@localhost:{config('DB_PORT')}/{config('DB_NAME')}"
    )


class DevelopmentConfig:
    FLASK_ENV = "development"
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{config('DB_USER')}:{config('DB_PASSWORD')}"
        f"@localhost:{config('DB_PORT')}/{config('DB_NAME')}"
    )


class TestConfig:
    FLASK_ENV = "test"
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{config('TEST_DB_USER')}:{config('TEST_DB_PASSWORD')}"
        f"@localhost:{config('TEST_DB_PORT')}/{config('TEST_DB_NAME')}"
    )


def create_app(config="config.DevelopmentConfig"):
    app = Flask(__name__)
    db.init_app(app)
    app.config.from_object(config)
    migrate = Migrate(app, db)
    CORS(app)
    api = Api(app)
    [api.add_resource(*route_data) for route_data in routes]
    return app
