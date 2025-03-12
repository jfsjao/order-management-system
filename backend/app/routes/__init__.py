from fastapi import APIRouter
from app.routes.products import router as products_router
from app.routes.users import router as users_router
from app.routes.orders import router as orders_router

router = APIRouter()

router.include_router(products_router, prefix="/api", tags=["Produtos"])
router.include_router(users_router, prefix="/api", tags=["Usuários"])
router.include_router(orders_router, prefix="/api", tags=["Pedidos"])
