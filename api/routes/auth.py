from fastapi import APIRouter, Depends, HTTPException, Security
from datetime import timedelta
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from api.dependencies.dependencies import get_db
from api.dependencies.auth import verify_password, create_access_token
from db.crud import users as crud_users
from models.user import Token

router = APIRouter()

ACCESS_TOKEN_EXPIRE_MINUTES = 30


# USERNAME is EMAIL
@router.post(
    "/token",
    response_model=Token,
)
def login(
        db: Session = Depends(get_db),
        form_data: OAuth2PasswordRequestForm = Depends(),
):
    db_user = crud_users.get_user_by_email(
        db=db,
        email=form_data.username,
    )
    if not db_user:
        raise HTTPException(
            status_code=400,
            detail="Incorrect username or password",
        )

    if not verify_password(
        plain_password=form_data.password,
        hashed_password=db_user.hashed_password,
    ):
        raise HTTPException(
            status_code=400,
            detail="Incorrect username or password",
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={
            "sub": str(db_user.id),
            "scopes": form_data.scopes,
        },
        expires_delta=access_token_expires,
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
    }
