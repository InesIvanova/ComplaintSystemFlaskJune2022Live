import os
from unittest.mock import patch

from flask_testing import TestCase

from constants.common import TEMP_DIR
from db import db
from config import create_app
from managers.complaint import ComplaintManager
from models import ComplaintState, ComplaintModel, TransactionModel
from services.s3 import S3Service
from tests.factories import ComplainerFactory
from tests.helpers import (
    generate_token,
    encoded_photo,
    encoded_photo_extension,
    mock_uuid,
)


class TestComplaint(TestCase):
    url = "/complaint"

    def create_app(self):
        return create_app("config.TestConfig")

    def setUp(self):
        db.init_app(self.app)
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_complaint_schema_missing_fields_raises(self):
        complaints = ComplaintModel.query.all()
        assert len(complaints) == 0

        transactions = TransactionModel.query.all()
        assert len(transactions) == 0

        user = ComplainerFactory()
        token = generate_token(user)
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }
        data = {}
        resp = self.client.post(self.url, headers=headers, json=data)
        self.assert400(resp)

        assert resp.json == {
            "extension": ["Missing data for required field."],
            "amount": ["Missing data for required field."],
            "photo": ["Missing data for required field."],
            "title": ["Missing data for required field."],
            "description": ["Missing data for required field."],
        }

        complaints = ComplaintModel.query.all()
        assert len(complaints) == 0

        transactions = TransactionModel.query.all()
        assert len(transactions) == 0

    @patch("uuid.uuid4", mock_uuid)
    @patch.object(
        ComplaintManager,
        "issue_transaction",
        return_value={
            "quote_id": "11-22",
            "recipient_id": "11",
            "transfer_id": "012",
            "target_account_id": "321",
            "amount": 10,
            "complaint_id": 1,
        },
    )
    @patch.object(S3Service, "upload_photo", return_value="some.s3.url")
    def test_crete_complaint(self, mocked_s3, mocked_transaction):
        complaints = ComplaintModel.query.all()
        assert len(complaints) == 0

        transactions = TransactionModel.query.all()
        assert len(transactions) == 0

        user = ComplainerFactory()
        token = generate_token(user)
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }
        data = {
            "title": "Test Title",
            "description": "Test desc",
            "amount": 10,
            "photo": encoded_photo,
            "extension": encoded_photo_extension,
        }
        resp = self.client.post(self.url, headers=headers, json=data)
        # assert resp.status_code == 201
        assert resp.status_code == 201
        resp = resp.json
        resp.pop("created_on")
        expected_resp = {
            "status": ComplaintState.pending.value,
            "description": data["description"],
            "photo_url": mocked_s3.return_value,
            "amount": data["amount"],
            "id": resp["id"],
            "title": data["title"],
        }
        assert resp == expected_resp

        file_name = f"{str(mock_uuid())}.{encoded_photo_extension}"
        path = os.path.join(TEMP_DIR, file_name)

        mocked_s3.assert_called_once_with(path, file_name)
        mocked_transaction.assert_called_once_with(
            data["amount"],
            f"{user.first_name} {user.last_name}",
            user.iban,
            mocked_transaction.return_value["complaint_id"],
        )

        complaints = ComplaintModel.query.all()
        assert len(complaints) == 1

        transactions = TransactionModel.query.all()
        assert len(transactions) == 1
