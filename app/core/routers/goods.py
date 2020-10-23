from typing import List

from fastapi import APIRouter, HTTPException

from app.core.models.pydantic import GoodQuantityChange
from app.core.models.tortoise import Goods, Goods_Pydantic

router = APIRouter()


@router.get(
    '',
    response_model=List[Goods_Pydantic],
    description='Получение списка всех товаров',
)
async def get_goods():
    return await Goods_Pydantic.from_queryset(Goods.all())


@router.get(
    '/{group}',
    response_model=List[Goods_Pydantic],
    description='Получение списка всех товаров, с фильтром по группе',
)
async def get_goods_filtered(group: str):
    return await Goods_Pydantic.from_queryset(Goods.filter(group=group))


@router.post(
    '',
    response_model=List[Goods_Pydantic],
    description='Изменение остатков для нескольких товаров',
)
async def change_multiple_goods_quantity(goods: List[GoodQuantityChange]):
    for good in goods:
        good_entity = Goods.filter(sku=good.sku)
        if good_entity.count():
            await good_entity.update(quantity=good.quantity)
        else:
            raise HTTPException(status_code=404, detail=f'Товар {good.sku} не найден')
    goods = [good.sku for good in goods]
    return await Goods_Pydantic.from_queryset(Goods.filter(sku__in=goods))
