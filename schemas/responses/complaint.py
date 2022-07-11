from marshmallow import Schema, fields
from marshmallow_enum import EnumField

from models import ComplaintState
from schemas.base import ComplaintBase


class ComplaintSchemaResponse(ComplaintBase):
    id = fields.Int(required=True)
    created_on = fields.DateTime(required=True)
    status = EnumField(ComplaintState, by_value=True)
    # TODO make nested schema for complainer obj
    # complainer = fields.Nested()
