from flask_testing import TestCase

from config import create_app
from db import db
from tests.factories import ComplainerFactory
from tests.helpers import generate_token

ENDPOINTS_DATA = (
    ("/complaint", "GET"),
    ("/complaint", "POST"),
    ("/complaint", "POST"),
    ("/complaint/1/approve", "PUT"),
    ("/complaint/1/reject", "PUT"),
)


class TestApp(TestCase):
    def create_app(self):
        return create_app("config.TestConfig")

    def setUp(self):
        db.init_app(self.app)
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def iterate_endpoints(
        self,
        endpoints_data,
        status_code_method,
        expected_resp_body,
        headers=None,
        payload=None,
    ):
        if not headers:
            headers = {}
        if not payload:
            payload = {}

        resp = None
        for url, method in endpoints_data:
            if method == "GET":
                resp = self.client.get(url, headers=headers)
            elif method == "POST":
                resp = self.client.post(url, headers=headers)
            elif method == "PUT":
                resp = self.client.put(url, headers=headers)
            elif method == "DELETE":
                resp = self.client.delete(url, headers=headers)
            status_code_method(resp)
            self.assertEqual(resp.json, expected_resp_body)

    def test_login_required(self):
        self.iterate_endpoints(
            ENDPOINTS_DATA, self.assert_401, {"message": "Missing token"}
        )

    def test_invalid_token_raises(self):
        headers = {"Authorization": "Bearer eyJ0eX"}
        self.iterate_endpoints(
            ENDPOINTS_DATA, self.assert_401, {"message": "Invalid token"}, headers
        )

    def test_missing_permissions_for_approver_raises(self):
        endpoints = (
            ("/complaint/1/approve", "PUT"),
            ("/complaint/1/reject", "PUT"),
        )
        user = ComplainerFactory()
        token = generate_token(user)
        headers = {"Authorization": f"Bearer {token}"}
        resp = None
        for url, method in endpoints:
            if method == "PUT":
                resp = self.client.put(url, headers=headers)
            self.assert403(resp)
            self.assertEqual(resp.json, {'message': 'Permission denied!'})

    def test_register_schema_raises_invalid_first_name(self):
        data = {"last_name": "Test", "email": "test@test.com", "iban": "aaaaaaaaaaaaaaaaaaaaaa", "phone": "11111111111111", "password": "12345@assd1"}
        headers = {"Content-Type": "application/json"}
        url = "/register"

        # Missing name
        resp = self.client.post(url, headers=headers, json=data)
        self.assert400(resp)
        assert resp.json == {'message': {'first_name': ['Missing data for required field.']}}

        data["first_name"] = "A"
        resp = self.client.post(url, headers=headers, json=data)
        self.assert400(resp)
        assert resp.json == {'message': {'first_name': ['Length must be between 2 and 20.']}}

        data["first_name"] = "AAAAAAAAAAAAAAAAAAAAAAA"
        resp = self.client.post(url, headers=headers, json=data)
        self.assert400(resp)
        assert resp.json == {'message': {'first_name': ['Length must be between 2 and 20.']}}

