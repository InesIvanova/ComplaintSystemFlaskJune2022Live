import os
import uuid

from constants.common import TEMP_DIR
from db import db
from models import ComplaintModel, UserRole, ComplaintState, TransactionModel
from services.s3 import S3Service
from services.wise import WiseService
from utils.common import decode_file

wise = WiseService()


class ComplaintManager:
    @staticmethod
    def get_complaints(user):
        if user.role == UserRole.complainer:
            return ComplaintModel.query.filter_by(complainer_id=user.id).all()
        return ComplaintModel.query.all()


    @staticmethod
    def create(data, user):
        data["complainer_id"] = user.id
        extension = data.pop("extension")
        photo = data.pop("photo")
        file_name = f"{str(uuid.uuid4())}.{extension}"
        path = os.path.join(TEMP_DIR, file_name)
        decode_file(path, photo)
        s3 = S3Service()
        photo_url = s3.upload_photo(path, file_name)

        try:
            data["photo_url"] = photo_url
            complaint = ComplaintModel(**data)
            db.session.add(complaint)
            db.session.flush()
            transaction_data = ComplaintManager.issue_transaction(data["amount"], f"{user.first_name} {user.last_name}", user.iban, complaint.id)
            transaction = TransactionModel(**transaction_data)
            db.session.add(transaction)
            db.session.flush()
            return complaint
        except Exception:
            s3.delete_photo(file_name)
        finally:
            os.remove(path)

    @staticmethod
    def approve(complaint_id):
        transaction = TransactionModel.query.filter_by(complaint_id=complaint_id).first()
        wise.fund_transfer(transaction.transfer_id)
        ComplaintModel.query.filter_by(id=complaint_id).update({"status": ComplaintState.approved})

    @staticmethod
    def reject(complaint_id):
        transaction = TransactionModel.query.filter_by(complaint_id=complaint_id).first()
        # Here cancel the transfer
        # wise.fund_transfer(transaction.transfer_id)
        ComplaintModel.query.filter_by(id=complaint_id).update({"status": ComplaintState.rejected})

    @staticmethod
    def issue_transaction(amount, full_name, iban, complaint_id):
        quote_id = wise.create_quote("EUR", "EUR", amount)
        recipient_id = wise.create_recipient(full_name, iban)
        customer_transaction_id = str(uuid.uuid4())
        transfer_id = wise.create_transfer(recipient_id, quote_id, customer_transaction_id)["id"]
        data = {
            "quote_id": quote_id,
            "recipient_id": recipient_id,
            "transfer_id": transfer_id,
            "target_account_id": customer_transaction_id,
            "amount": amount,
            "complaint_id": complaint_id,
        }
        return data


