from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.product import ProductCreate, ProductUpdate, ProductOut
from app.services import product_service

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

# 🔍 SEARCH PRODUCTS (LIKE)
@router.get("/search", response_model=list[ProductOut]) # Search products by keyword
def search_product( 
    q: str = Query(..., description="Search keyword"),
    db: Session = Depends(get_db)
): # Dependency injection for DB session
    return product_service.search_products(db, q) # Call service to search products

# ---------------------------
# CREATE PRODUCT
# ---------------------------
@router.post("/", response_model=ProductOut)
def create_product(
    data: ProductCreate,
    db: Session = Depends(get_db)
):
    return product_service.create_product(db, data)


# ---------------------------
# READ ALL PRODUCTS
# ---------------------------
@router.get("/", response_model=list[ProductOut])
def get_all_products(db: Session = Depends(get_db)):
    return product_service.get_all_products(db)


# ---------------------------
# READ PRODUCT BY ID
# ---------------------------
@router.get("/{id}", response_model=ProductOut)
def get_product_by_id(
    product_id: int,
    db: Session = Depends(get_db)
):
    return product_service.get_product(db, product_id)


# ---------------------------
# UPDATE PRODUCT
# ---------------------------
@router.put("/{id}", response_model=ProductOut)
def update_product(
    product_id: int,
    data: ProductUpdate,
    db: Session = Depends(get_db)
):
    return product_service.update_product(db, product_id, data)


# ---------------------------
# DELETE PRODUCT
# ---------------------------
@router.delete("/{id}")
def delete_product(
    product_id: int,
    db: Session = Depends(get_db)
):
    return product_service.delete_product(db, product_id)
