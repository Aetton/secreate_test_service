from app.core.routers.good import router as good_router
from app.core.routers.goods import router as goods_router
from app.utils.api.router import TypedAPIRouter


good_router = TypedAPIRouter(
    router=good_router,
    prefix='/good',
    tags=['single_good'],
)

goods_router = TypedAPIRouter(
    router=goods_router,
    prefix='/goods',
    tags=['multiple_goods'],
)
