from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate

from db import db
from resources.routes import routes

app = Flask(__name__)
db.init_app(app)
app.config.from_object("config.DevelopmentConfig")
api = Api(app)
migrate = Migrate(app, db)


@app.after_request
def return_resp(resp):
    db.session.commit()
    return resp


[api.add_resource(*route_data) for route_data in routes]


if __name__ == "__main__":
    app.run()
