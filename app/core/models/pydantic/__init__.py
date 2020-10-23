from typing import Optional

from pydantic import Field
from pydantic.main import BaseModel


class GoodCreate(BaseModel):
    sku: int = Field(..., example=172358)
    name: str = Field(..., example='Тестовый товар')
    group: Optional[str] = Field('Нет группы', example='Нет группы')
    quantity: Optional[int] = Field(0, example=12)


class GoodQuantityChange(BaseModel):
    sku: int = Field(..., example=172358)
    quantity: int = Field(0, example=12)


class Status(BaseModel):
    message: str = 'Message'