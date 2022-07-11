from werkzeug.exceptions import BadRequest
from werkzeug.security import check_password_hash

from managers.auth import AuthManager
from models import ApproverModel


class ApproverManager:
    @staticmethod
    def login(data):
        # Todo refector as sub-func and reuse in complainer as well, later in admin
        approver = ApproverModel.query.filter_by(email=data["email"]).first()
        if not approver:
            raise BadRequest("does not exist")

        if check_password_hash(approver.password, data["password"]):
            return AuthManager.encode_token(approver)
        raise BadRequest("Invalid credentials")
