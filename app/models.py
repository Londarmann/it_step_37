from tortoise import fields, models


class Item(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=30)
    description = fields.TextField()
    price = fields.FloatField()
    tax = fields.FloatField(null=True)
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "items"
