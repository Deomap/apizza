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
    except:
        return {"pizzeria": "error"}
    return {db_pizzeria.id: "OK"}


def upd_pizzeria():
    pass


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
