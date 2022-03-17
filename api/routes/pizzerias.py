from fastapi import APIRouter, Depends, Security
from fastapi.responses import JSONResponse
from db.crud import pizzerias as crud_pizzerias
from models.pizzeria import Pizzeria, PizzeriaCreate
from sqlalchemy.orm import Session
from api.dependencies.dependencies import get_db
from api.dependencies.auth import verify_token

router = APIRouter()


@router.get(
    '/{pizzeria_id}',
    response_model=Pizzeria,
)
def get_pizzeria(
    pizzeria_id: int,
    auth: str = Security(
        verify_token,
        scopes=[
            'authed',
        ]
    ),
    db: Session = Depends(get_db),
):
    return crud_pizzerias.get_pizzeria(
        db=db,
        pizzeria_id=pizzeria_id,
    )


@router.post(
    '/',
    response_class=JSONResponse,
)
def create_pizzeria(
    auth: str = Security(
        verify_token,
        scopes=[
            'direction',
        ]
    ),
    db: Session = Depends(get_db),
):
    return crud_pizzerias.create_pizzeria(db=db)


@router.put(
    '/',
    response_class=JSONResponse,
)
def upd_pizzeria(
    pizzeria_id: int,
    pizzeria: PizzeriaCreate,
    auth: str = Security(
        verify_token,
        scopes=[
            'pizzeria',
        ]
    ),
    db: Session = Depends(get_db),
):
    return crud_pizzerias.upd_pizzeria(
        db=db,
        pizzeria=pizzeria,
        pizzeria_id=pizzeria_id,
    )


@router.delete(
    '/{pizzeria_id}',
    response_class=JSONResponse,
)
def del_pizzeria(
    pizzeria_id: int,
    auth: str = Security(
        verify_token,
        scopes=[
            'direction',
        ]
    ),
    db: Session = Depends(get_db),
):
    return crud_pizzerias.del_pizzeria(
        db=db,
        pizzeria_id=pizzeria_id,
    )
