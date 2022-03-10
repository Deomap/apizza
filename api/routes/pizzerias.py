from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from db.crud import pizzerias as crud_pizzerias
from models.pizzeria import Pizzeria, PizzeriaCreate
from sqlalchemy.orm import Session
from api.dependencies import get_db

router = APIRouter()


@router.get(
    '/{pizzeria_id}',
    response_model=Pizzeria,
)
def get_pizzeria(
    pizzeria_id: int,
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
        db: Session = Depends(get_db),
):
    return crud_pizzerias.create_pizzeria(db=db)


@router.put('/')
def upd_pizzeria():
    pass


@router.delete(
    '/{pizzeria_id}',
    response_class=JSONResponse,
)
def del_pizzeria(
    pizzeria_id: int,
    db: Session = Depends(get_db),
):
    return crud_pizzerias.del_pizzeria(
        db=db,
        pizzeria_id=pizzeria_id,
    )
