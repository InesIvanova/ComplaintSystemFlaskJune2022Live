from sqlalchemy import func

from db import db
from models.enums import ComplaintState


class ComplaintModel(db.Model):
    __tablename__ = 'complaint'

    id = db.Column(db.Integer, primary_key=True)
    photo_url = db.Column(db.String(255), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    created_on = db.Column(db.DateTime, nullable=False, server_default=func.now())
    status = db.Column(db.Enum(ComplaintState), nullable=False, default=ComplaintState.pending)
    complainer_id = db.Column(db.Integer, db.ForeignKey("complainers.id"), nullable=False)
    complainer = db.relationship("ComplainerModel")