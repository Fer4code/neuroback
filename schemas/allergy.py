from ma import ma
from models.allergy import AllergyModel


class AllergySchema(ma.ModelSchema):
    class Meta:
        model = AllergyModel
        dump_only = ("id",)