from flask import request
from flask_restful import Resource
from managers.complainer import ComplainerManager
from schemas.requests.auth import RegisterSchemaRequest, LoginSchemaRequest
from utils.decorators import validate_schema


class RegisterResource(Resource):
    @validate_schema(RegisterSchemaRequest)
    def post(self):
        data = request.get_json()
        token = ComplainerManager.register(data)
        return {"token": token}, 201


class LoginResource(Resource):
    @validate_schema(LoginSchemaRequest)
    def post(self):
        data = request.get_json()
        token = ComplainerManager.login(data)
        return {"token": token}, 200


class ApproverLoginResource(Resource):
    @validate_schema(LoginSchemaRequest)
    def post(self):
        data = request.get_json()
        token = ApproverManager.login(data)
        return {"token": token}, 200
