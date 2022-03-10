from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from db.crud import products as crud_products
from models.products import ProductCreate, Product
from sqlalchemy.orm import Session
from api.dependencies import get_db

router = APIRouter()


@router.get(
    '/{product_id}',
    response_model=Product,
)
def get_product(
    product_id: int,
    db: Session = Depends(get_db),
):
    return crud_products.get_product(
        db=db,
        product_id=product_id,
    )


@router.post(
    '/',
    response_class=JSONResponse,
)
def create_product(
    product: ProductCreate,
    db: Session = Depends(get_db),
):
    return crud_products.create_product(
        db=db,
        product=product,
    )


@router.put('/')
def upd_product():
    pass


@router.delete(
    '/{product_id}',
    response_class=JSONResponse,
)
def del_product(
        product_id: int,
        db: Session = Depends(get_db),
):
    return crud_products.del_product(
        db=db,
        product_id=product_id,
    )
