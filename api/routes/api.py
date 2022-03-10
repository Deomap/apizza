from fastapi import APIRouter
from api.routes import orders, users, products


router = APIRouter()
router.include_router(orders.router, prefix="/orders")
router.include_router(users.router, prefix="/users")
router.include_router(products.router, prefix="/products")
