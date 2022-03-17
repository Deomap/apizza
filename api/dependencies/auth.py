from db.crud import users as crud_users
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, SecurityScopes
from api.dependencies.dependencies import get_db
from jose import JWTError, jwt
from passlib.context import CryptContext
from models.user import TokenData
from pydantic import ValidationError

SECRET_KEY = "dc485ef19c4e0c977bbb10d4bd031957e368cfb15f5f17198da7038ac3e41c54"
ALGORITHM = "HS256"

# Hierarchy:
# Direction includes pizzeria and authed
# pizzeria does not include authed
# inactive has no permissions
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="auth/token",
    scopes={
        "direction": "",
        "pizzeria": "",
        "authed": "",
        "guest": "",
        "inactive": "",
    }
)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str):
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(
    data: dict,
    expires_delta: timedelta | None = None,
):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# USERNAME is ID
def verify_token(
        security_scopes: SecurityScopes,
        db: Session = Depends(get_db),
        token: str = Depends(oauth2_scheme),
):
    if security_scopes.scopes:
        authenticate_value = f'Bearer scope="{security_scopes.scope_str}"'
    else:
        authenticate_value = f"Bearer"
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": authenticate_value},
    )

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM],
        )
        username = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_scopes = payload.get("scopes", [])
        token_data = TokenData(
            username=username,
            scopes=token_scopes,
        )
    except (JWTError, ValidationError):
        raise credentials_exception

    user = crud_users.get_user(
        db=db,
        user_id=token_data.username,
    )
    if user is None:
        raise credentials_exception
    for scope in security_scopes.scopes:
        if scope not in token_data.scopes:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Not enough permissions",
                headers={"WWW-Authenticate": authenticate_value},
            )

    return user
