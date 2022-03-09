from sqlalchemy.orm import Session

from models import schemas
from db import models


# ORDER
def get_order(db: Session, order_id: int):
    return db.query(models.Order).filter(models.Order.id == order_id).first()


def create_order(db: Session, order: schemas.OrderCreate, user_id: int):
    db_order = models.Order(user_id=user_id, type=order.type, delivery_adds=order.delivery_adds)
    try:
        db.add(db_order)
        db.commit()
        db.refresh(db_order)
    except:
        return {user_id: "error"}
    return {user_id: "OK"}


def upd_order(db: Session, user_id: int):
    pass


def del_order(db: Session, order_id: int):
    db_order = db.query(models.Order).filter(models.Order.id == order_id).first()
    try:
        db.delete(db_order)
        db.commit()
    except:
        return {order_id: "error"}
    return {order_id: "OK"}
