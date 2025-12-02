from marshmallow import Schema, fields


class StudentSchema(Schema):

    created_date = fields.Float()
    id = fields.Int()
    name = fields.Str()
    score = fields.Int(required=True)
    score_name = fields.Str()
    updated_date = fields.DateTime()


