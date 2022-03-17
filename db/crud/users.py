from sqlalchemy.orm import Session

from models.user import User, UserInAuth
from db import tables


def get_user(
    db: Session,
    user_id: int,
):
    return db.query(tables.User)\
        .filter(tables.User.id == user_id).first()


def get_user_by_email(
    db: Session,
    email: str,
):
    return db.query(tables.User)\
        .filter(tables.User.email == email).first()


def create_user(
        user: UserInAuth,
        db: Session,
):
    db_user = tables.User(
        forename=user.forename,
        type=user.type,
        hashed_password=user.hashed_password,
        hpw_salt=user.salt,
        email=user.email,
    )
    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    except:
        return {"user": "error"}
    return {
        "response": "OK",
        "user_id": db_user.id,
    }


def upd_user(
        db: Session,
        user_id: int,
        user: User,
):
    try:
        user = dict(user)
        db.query(tables.User) \
            .filter(tables.User.id == user_id).update(user)
        db.commit()
    except:
        return {
            "response": "error",
            "user_id": user_id,
        }
    return {
        "response": "OK",
        "user_id": user_id,
    }


def del_user(
    db: Session,
    user_id: int,
):
    db_user = db.query(tables.User)\
        .filter(tables.User.id == user_id).first()
    try:
        db.delete(db_user)
        db.commit()
    except:
        return {
            "response": "error",
            "user_id": user_id,
        }
    return {
        "response": "OK",
        "user_id": user_id,
    }