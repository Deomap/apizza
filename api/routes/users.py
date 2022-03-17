from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from db.crud import users as crud_users
from models.user import User
from sqlalchemy.orm import Session
from api.dependencies.dependencies import get_db
from api.dependencies.auth import verify_token, register

router = APIRouter()


@router.get(
    '/{user_id}',
    response_model=User,
)
def get_user(
    user_id: int,
    auth: str = Depends(verify_token),
    db: Session = Depends(get_db),
):
    print(auth)
    return crud_users.get_user(
        db=db,
        user_id=user_id,
    )


@router.post(
    '/',
    response_class=JSONResponse,
)
def create_user(
        auth: str = Depends(register),
):
    return auth


@router.put(
    '/',
    response_class=JSONResponse,
)
def upd_user(
        user_id: int,
        user: User,
        auth: str = Depends(verify_token),
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
    auth: str = Depends(verify_token),
    db: Session = Depends(get_db),
):
    return crud_users.del_user(
        db=db,
        user_id=user_id,
    )
