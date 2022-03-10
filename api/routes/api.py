from fastapi import APIRouter
from api.routes import orders, users


router = APIRouter()
router.include_router(orders.router, prefix="/orders")
router.include_router(users.router, prefix="/users")
