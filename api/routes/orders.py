from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from db.crud import orders as crud_orders
from models.order import Order, OrderCreate
from sqlalchemy.orm import Session
from api.dependencies import get_db

router = APIRouter()


@router.get(
    '/{order_id}',
    response_model=Order,
)
def get_order(
    order_id: int,
    db: Session = Depends(get_db),
):
    return crud_orders.get_order(
        db=db,
        order_id=order_id,
    )


@router.post(
    '/{order_id}',
    response_class=JSONResponse,
)
def create_order(
    user_id: int,
    order: OrderCreate,
    db: Session = Depends(get_db),
):
    return crud_orders.create_order(
        db=db,
        order=order,
        user_id=user_id,
    )


@router.put(
    '/',
    response_class=JSONResponse,
)
def upd_order(
    order_id: int,
    order: OrderCreate,
    db: Session = Depends(get_db),
):
    return crud_orders.upd_order(
        db=db,
        order=order,
        order_id=order_id,
    )


@router.delete(
    '/{order_id}',
    response_class=JSONResponse,
)
def del_order(
    order_id: int,
    db: Session = Depends(get_db),
):
    return crud_orders.del_order(
        db=db,
        order_id=order_id,
    )
