from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.crud import product as crud
from app.schemas.product import ProductCreate, ProductUpdate


# =========================
# CREATE PRODUCT
# =========================
def create_product(db: Session, data: ProductCreate):
    return crud.create_product(db, data)


# =========================
# SEARCH PRODUCT (LIKE)
# =========================
def search_product_service(db: Session, keyword: str):
    products = crud.search_products(db, keyword)

    if not products:
        raise HTTPException(
            status_code=404,
            detail="No products found"
        )

    return products


# =========================
# READ ALL PRODUCTS
# =========================
def get_products(db: Session):
    return crud.get_all_products(db)


# =========================
# READ PRODUCT BY ID
# =========================
def get_product(db: Session, id: int):
    product = crud.get_product_by_id(db, id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


# =========================
# UPDATE PRODUCT
# =========================
def update_product(db: Session, id: int, data: ProductUpdate):
    product = crud.update_product(db, id, data)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


# =========================
# DELETE PRODUCT
# =========================
def delete_product(db: Session, id: int):
    product = crud.delete_product(db, id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted successfully"}
