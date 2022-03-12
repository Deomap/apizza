from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from db.crud import users as crud_users
from models.user import UserCreate, User
from sqlalchemy.orm import Session
from api.dependencies import get_db

router = APIRouter()


@router.get(
    '/{user_id}',
    response_model=User,
)
def get_user(
    user_id: int,
    db: Session = Depends(get_db),
):
    return crud_users.get_user(
        db=db,
        user_id=user_id,
    )


@router.post(
    '/',
    response_class=JSONResponse,
)
def create_user(
        db: Session = Depends(get_db),
):
    return crud_users.create_user(db=db)


@router.put(
    '/',
    response_class=JSONResponse,
)
def upd_user(
        user_id: int,
        user: User,
        db: Session = Depends(get_db),
):
    return crud_users.upd_user(
        db=db,
        user_id=user_id,
        user=user,
    )


@router.delete(
    '/{user_id}',
    response_class=JSONResponse,
)
def del_user(
    user_id: int,
    db: Session = Depends(get_db),
):
    return crud_users.del_user(
        db=db,
        user_id=user_id,
    )
