from werkzeug.exceptions import BadRequest

from db import db
from managers.auth import AuthManager
from models.user import ComplainerModel
from werkzeug.security import generate_password_hash, check_password_hash


class ComplainerManager:
    @staticmethod
    def register(complainer_data):
        complainer_data["password"] = generate_password_hash(complainer_data["password"])
        user = ComplainerModel(**complainer_data)
        db.session.add(user)
        return AuthManager.encode_token(user)

    @staticmethod
    def login(login_data):
        complainer = ComplainerModel.query.filter_by(email=login_data["email"]).first()
        if not complainer:
            raise BadRequest("No such email! Please register!")

        if check_password_hash(complainer.password, login_data["password"]):
            return AuthManager.encode_token(complainer)
        raise BadRequest("Wrong credentials!")

