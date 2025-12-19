from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from app.services import product_service
from app.services.product_service import search_product_service
from app.schemas.product import ProductCreate, ProductUpdate, ProductResponse

router = APIRouter(prefix="/products", tags=["Products"])


# =========================
# SEARCH PRODUCTS (LIKE)
# =========================
@router.get("/search", response_model=List[ProductResponse])
def search_products(
    keyword: str = Query(..., min_length=1),
    db: Session = Depends(get_db)
):
    return search_product_service(db, keyword)


# =========================
# CREATE PRODUCT
# =========================
@router.post("/", response_model=ProductResponse)
def create(data: ProductCreate, db: Session = Depends(get_db)):
    return product_service.create_product(db, data)


# =========================
# READ ALL PRODUCTS
# =========================
@router.get("/", response_model=List[ProductResponse])
def get_all(db: Session = Depends(get_db)):
    return product_service.get_products(db)


# =========================
# READ PRODUCT BY ID
# =========================
@router.get("/{id}", response_model=ProductResponse)
def get(product_id: int, db: Session = Depends(get_db)):
    return product_service.get_product(db, product_id)


# =========================
# UPDATE PRODUCT
# =========================
@router.put("/{id}", response_model=ProductResponse)
def update(product_id: int, data: ProductUpdate, db: Session = Depends(get_db)):
    return product_service.update_product(db, product_id, data)


# =========================
# DELETE PRODUCT
# =========================
@router.delete("/{id}")
def delete(product_id: int, db: Session = Depends(get_db)):
    return product_service.delete_product(db, product_id)
