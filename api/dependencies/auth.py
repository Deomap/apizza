import hashlib, uuid
import hmac
import os

from fastapi import Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")
oauth2_reg = OAuth2PasswordBearer(tokenUrl="auth/register")


def hash_password(password: str):
    salt = os.urandom(16)
    pw_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return salt, pw_hash


def is_correct_password(salt: bytes, pw_hash: bytes, password: str) -> bool:
    return hmac.compare_digest(
        pw_hash,
        hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    )


def verify_token(token: str = Depends(oauth2_scheme)):
    return token


def register(token: str = Depends(oauth2_reg)):
    return token
