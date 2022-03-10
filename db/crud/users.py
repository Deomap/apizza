from sqlalchemy.orm import Session

from models.users import User, UserCreate, UserBase
from db import tables


def get_user(db: Session,
             user_id: int):
    return db.query(tables.User).filter(tables.User.id == user_id).first()


def create_user(db: Session):
    db_user = tables.User()
    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    except:
        return {"user": "error"}
    return {"user": "OK"}


def upd_user(db: Session,
             id: int):
    pass


def del_user(db: Session,
             user_id: int):
    db_user = db.query(tables.User).filter(tables.User.id == user_id).first()
    try:
        db.delete(db_user)
        db.commit()
    except:
        return {user_id: "error"}
    return {user_id: "OK"}