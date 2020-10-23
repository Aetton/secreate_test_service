from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.models import Model


class Goods(Model):
    """
    Модель товара.
    sku - SKU товара. Уникальное поле;
    name - наименование товара;
    group - группа товара;
    quantity - количество товара на складе;
    """

    sku = fields.IntField(pk=True)
    name = fields.CharField(max_length=50)
    group = fields.CharField(max_length=50, default='Нет группы', null=True)
    quantity = fields.IntField(default=0)


Goods_Pydantic = pydantic_model_creator(Goods)
