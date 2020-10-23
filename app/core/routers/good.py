from typing import List

from fastapi import HTTPException, APIRouter

from app.core.models.pydantic import GoodCreate, Status, GoodQuantityChange
from app.core.models.tortoise import Goods, Goods_Pydantic

router = APIRouter()


@router.get(
    '/{sku}',
    response_model=Goods_Pydantic,
    description='Получение товара по его SKU',
)
async def get_good(sku: int):
    try:
        return await Goods_Pydantic.from_queryset_single(Goods.get(sku=sku))
    except:
        raise HTTPException(status_code=404, detail=f'Товар {sku} не найден')


@router.post(
    '',
    response_model=Goods_Pydantic,
    description='Заведение нового товара',
)
async def create_good(good: GoodCreate):
    good_db = await Goods.create(**good.dict(exclude_unset=True))
    return await Goods_Pydantic.from_tortoise_orm(good_db)


@router.delete(
    '/{good_sku}',
    response_model=Goods_Pydantic,
    description='Удаление товара по его SKU',
)
async def delete_good(sku: int):
    deleted_count = await Goods.filter(sku=sku).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f'Товар {sku} не найден')
    return Status(message=f'Удален товар {sku}')


@router.post(
    '/update',
    response_model=Goods_Pydantic,
    description='Изменение остатков для единичного товара',
)
async def update_single_good_quantity(good: GoodQuantityChange):
    updated_count = await Goods.filter(sku=good.sku).update(quantity=good.quantity)
    if updated_count:
        return await Goods_Pydantic.from_queryset_single(Goods.get(sku=good.sku))
    else:
        raise HTTPException(status_code=404, detail=f'Товар {good.sku} не найден')
