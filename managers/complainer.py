from db import db
from managers.auth import AuthManager
from models.user import ComplainerModel
from werkzeug.security import generate_password_hash


class ComplainerManager:
    @staticmethod
    def register(complainer_data):
        complainer_data["password"] = generate_password_hash(complainer_data["password"])
        user = ComplainerModel(**complainer_data)
        db.session.add(user)
        db.session.commit()
        return AuthManager.encode_token(user)