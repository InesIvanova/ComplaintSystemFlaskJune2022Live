from flask import request
from flask_api import status
from flask_restful import Resource

from managers.approver import ApproverManager
from managers.complainer import ComplainerManager
from schemas.requests.auth import RegisterSchemaRequest, LoginSchemaRequest
from utils.decorators import validate_schema


class RegisterResource(Resource):
    @validate_schema(RegisterSchemaRequest)
    def post(self):
        data = request.get_json()
        token = ComplainerManager.register(data)
        return {"token": token},  status.HTTP_201_CREATED


class LoginResource(Resource):
    @validate_schema(LoginSchemaRequest)
    def post(self):
        data = request.get_json()
        token = ComplainerManager.login(data)
        return {"token": token}, status.HTTP_200_OK


class ApproverLoginResource(Resource):
    @validate_schema(LoginSchemaRequest)
    def post(self):
        data = request.get_json()
        token = ApproverManager.login(data)
        return {"token": token},  status.HTTP_200_OK
