from sqlalchemy.orm import Session

from models.products import ProductCreate, Product
from db import tables


def get_product(
    db: Session,
    product_id: int,
):
    return db.query(tables.Product)\
        .filter(tables.Product.id == product_id).first()


def create_product(
    db: Session,
    product: ProductCreate,
):
    db_product = tables.Product(
        name=product.name,
        price=product.price,
    )
    try:
        db.add(db_product)
        db.commit()
        db.refresh(db_product)
    except:
        return {"product": "error"}
    return {db_product.id: "OK"}


def upd_product(db: Session, user_id: int):
    pass


def del_product(
    db: Session,
    product_id: int,
):
    db_product = db.query(tables.Product)\
        .filter(tables.Product.id == product_id).first()
    try:
        db.delete(db_product)
        db.commit()
    except:
        return {product_id: "error"}
    return {product_id: "OK"}
