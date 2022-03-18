from fastapi import APIRouter, Depends, Security
from fastapi.responses import JSONResponse
from db.crud import orders as crud_orders
from models.order import Order, OrderCreate
from sqlalchemy.orm import Session
from api.dependencies.dependencies import get_db
from api.dependencies.auth import verify_token

router = APIRouter()


@router.get(
    '/{order_id}',
    response_model=Order,
)
def get_order(
    order_id: int,
    auth=Security(
        verify_token,
        scopes=[
            'authed',
        ]
    ),
    db: Session = Depends(get_db),
):
    return crud_orders.get_order(
        db=db,
        order_id=order_id,
    )


@router.get(
    '/',
    response_model=list[Order],
)
def get_all_orders(
    auth=Security(
        verify_token,
        scopes=[
            'authed',  # authed only for reading own orders
        ]
    ),
    db: Session = Depends(get_db),
):
    if auth.get('scopes') == ['authed']:
        return crud_orders.get_user_orders(
            user_id=auth['user'].id,
            db=db,
        )
    return crud_orders.get_all_orders(
        db=db,
    )


@router.post(
    '/{order_id}',
    response_class=JSONResponse,
)
def create_order(
    user_id: int,
    order: OrderCreate,
    auth=Security(
        verify_token,
        scopes=[
            'authed',
        ]
    ),
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
    auth=Security(
        verify_token,
        scopes=[
            'pizzeria',
        ]
    ),
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
    auth=Security(
        verify_token,
        scopes=[
            'pizzeria',
        ]
    ),
    db: Session = Depends(get_db),
):
    return crud_orders.del_order(
        db=db,
        order_id=order_id,
    )
