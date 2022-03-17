from fastapi import APIRouter, Depends, HTTPException, Security
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from api.dependencies.dependencies import get_db
from api.dependencies.auth import is_correct_password
from db.crud import users as crud_users
from models.user import UserInAuth

router = APIRouter()


# USERNAME is EMAIL
@router.get(
    "/token",
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

    user = UserInAuth(**db_user)
    if not is_correct_password(
        salt=user.salt,
        pw_hash=user.hashed_password,
        password=form_data.password,
    ):
        raise HTTPException(
            status_code=400,
            detail="Incorrect username or password",
        )

    return {
        "user_id": user.id,
        "token_type": "bearer"
    }
