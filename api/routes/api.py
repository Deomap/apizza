from fastapi import APIRouter
from api.routes import orders, users, pizzerias, auth


router = APIRouter()
router.include_router(orders.router, prefix="/orders")
router.include_router(users.router, prefix="/users")
router.include_router(pizzerias.router, prefix="/pizzerias")
router.include_router(auth.router, prefix="/auth")
