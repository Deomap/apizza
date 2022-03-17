from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from db.crud import users as crud_users
from models.user import User, UserInAuth
from sqlalchemy.orm import Session
from api.dependencies.dependencies import get_db
from api.dependencies.auth import verify_token, hash_password
from fastapi.security import OAuth2PasswordRequestForm

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
    return crud_users.get_user(
        db=db,
        user_id=user_id,
    )


@router.post(
    '/',
    response_class=JSONResponse,
)
def create_user(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    email = form_data.username
    db_user = crud_users.get_user_by_email(
        db=db,
        email=email,
    )
    if db_user:
        raise HTTPException(
            status_code=409,
            detail="Email already exists",
        )

    hashed_password = hash_password(form_data.password)
    user = UserInAuth(
        email=email,
        hashed_password=hashed_password,
    )
    crud_response = crud_users.create_user(
        user=user,
        db=db,
    )
    return crud_response


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
