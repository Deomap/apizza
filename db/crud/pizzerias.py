from sqlalchemy.orm import Session

from models.pizzeria import Pizzeria, PizzeriaCreate
from db import tables


def get_pizzeria(
    db: Session,
    pizzeria_id: int,
):
    return db.query(tables.Pizzeria)\
        .filter(tables.Pizzeria.id == pizzeria_id).first()


def create_pizzeria(db: Session):
    db_pizzeria = tables.Pizzeria()
    try:
        db.add(db_pizzeria)
        db.commit()
        db.refresh(db_pizzeria)
    except Exception as e:
        return {"pizzeria": e.args}
    return {db_pizzeria.id: "OK"}


def upd_pizzeria(
        db: Session,
        pizzeria,
        pizzeria_id,
):
    pizzeria = dict(pizzeria)
    db_query = db.query(tables.Pizzeria)\
        .filter(tables.Pizzeria.id == pizzeria_id)
    db_obj = db_query.first()

    db_obj.products.clear()
    for product in pizzeria['products']:
        orm_object = tables.PizzeriaProduct(**dict(product))
        db_obj.products.append(orm_object)
    del pizzeria['products']
    db.refresh(db_obj)

    db_query.update(pizzeria)

    db.commit()
    return {pizzeria_id: "OK"}


def del_pizzeria(
    db: Session,
    pizzeria_id: int,
):
    db_pizzeria = db.query(tables.Pizzeria)\
        .filter(tables.Pizzeria.id == pizzeria_id).first()
    try:
        db.delete(db_pizzeria)
        db.commit()
    except:
        return {pizzeria_id: "error"}
    return {pizzeria_id: "OK"}
