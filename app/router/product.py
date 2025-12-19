from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services import product_service
from app.schemas.product import ProductCreate, ProductUpdate, ProductResponse
from typing import List

router = APIRouter(prefix="/products", tags=["Products"])

@router.post("/", response_model=ProductResponse)
def create(data: ProductCreate, db: Session = Depends(get_db)):
    return product_service.create_product(db, data)

@router.get("/", response_model=List[ProductResponse])
def get_all(db: Session = Depends(get_db)):
    return product_service.get_products(db)

@router.get("/{product_id}", response_model=ProductResponse)
def get(product_id: int, db: Session = Depends(get_db)):
    return product_service.get_product(db, product_id)

@router.put("/{product_id}", response_model=ProductResponse)
def update(product_id: int, data: ProductUpdate, db: Session = Depends(get_db)):
    return product_service.update_product(db, product_id, data)

@router.delete("/{product_id}")
def delete(product_id: int, db: Session = Depends(get_db)):
    return product_service.delete_product(db, product_id)
