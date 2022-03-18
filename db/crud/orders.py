from sqlalchemy.orm import Session

from models.order import OrderCreate, Order
from db import tables


def get_order(
    db: Session,
    order_id: int,
):
    return db.query(tables.Order)\
        .filter(tables.Order.id == order_id).first()


def get_all_orders(
        db: Session,
):
    return db.query(tables.Order).all()


def get_user_orders(
        user_id: int,
        db: Session,
):
    return db.query(tables.Order)\
        .filter(tables.Order.user_id == user_id).all()


def create_order(
    db: Session,
    order: OrderCreate,
    user_id: int,
):
    db_order = tables.Order(
        user_id=user_id,
        type=order.type,
        status=order.status,
        delivery_adds=order.delivery_adds,
        price=order.price,
    )
    for product in order.products:
        orm_product = tables.OrderProduct(**dict(product))
        db_order.products.append(orm_product)
    try:
        db.add(db_order) 
        db.commit()
    except:
        return {user_id: "error"}
    return {db_order.id: "OK"}


def upd_order(
    db: Session,
    order: OrderCreate,
    order_id: int,
):
    order = dict(order)
    db_query = db.query(tables.Order) \
        .filter(tables.Order.id == order_id)
    db_obj = db_query.first()

    db_obj.products.clear()
    for product in order['products']:
        orm_object = tables.OrderProduct(**dict(product))
        db_obj.products.append(orm_object)
    del order['products']
    db.refresh(db_obj)

    db_query.update(order)

    db.commit()
    return {order_id: "OK"}


def del_order(
    db: Session,
    order_id: int,
):
    db_order = db.query(tables.Order)\
        .filter(tables.Order.id == order_id).first()
    try:
        db.delete(db_order)
        db.commit()
    except:
        return {order_id: "error"}
    return {order_id: "OK"}
