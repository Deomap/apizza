from sqlalchemy.orm import Session

from models.orders import OrderBase, OrderCreate, Order
from db import tables


def get_order(db: Session,
              order_id: int):
    return db.query(tables.Order).filter(tables.Order.id == order_id).first()


def create_order(db: Session,
                 order: OrderCreate,
                 user_id: int):
    db_order = tables.Order(user_id=user_id,
                            type=order.type,
                            delivery_adds=order.delivery_adds,
                            status=order.status)
    try:
        db.add(db_order)
        db.commit()
        db.refresh(db_order)
    except:
        return {user_id: "error"}
    return {user_id: "OK"}


def upd_order(db: Session, user_id: int):
    pass


def del_order(db: Session,
              order_id: int):
    db_order = db.query(tables.Order).filter(tables.Order.id == order_id).first()
    try:
        db.delete(db_order)
        db.commit()
    except:
        return {order_id: "error"}
    return {order_id: "OK"}
