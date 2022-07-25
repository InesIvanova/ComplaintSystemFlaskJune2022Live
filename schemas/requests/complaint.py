from schemas.base import ComplaintBase
from marshmallow import fields


class ComplaintSchemaRequest(ComplaintBase):
    photo = fields.String(required=True)
    extension = fields.String(required=True)
