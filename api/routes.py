from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from db import crud
from models import schemas
from sqlalchemy.orm import Session
from api.dependencies import get_db


router = APIRouter(
    prefix="/orders"
)


# ORDER
@router.get('/{order_id}', response_model=schemas.Order)
def get_order(order_id: int, db: Session = Depends(get_db)):
    return crud.get_order(db=db, order_id=order_id)


@router.post('/{order_id}', response_class=JSONResponse)
def create_order(
        user_id: int, order: schemas.OrderCreate, db: Session = Depends(get_db)
):
    return crud.create_order(db=db, order=order, user_id=user_id)


@router.put('/')
def upd_order():
    pass


@router.delete('/{order_id}', response_class=JSONResponse)
def del_order(order_id: int, db: Session = Depends(get_db)):
    return crud.del_order(db=db, order_id=order_id)

