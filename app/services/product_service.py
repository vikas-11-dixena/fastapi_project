from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.crud import product as crud
from app.schemas.product import ProductCreate, ProductUpdate

def create_product(db: Session, data: ProductCreate):
    return crud.create_product(db, data)

def get_products(db: Session):
    return crud.get_all_products(db)

def get_product(db: Session, product_id: int):
    product = crud.get_product_by_id(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

def update_product(db: Session, product_id: int, data: ProductUpdate):
    product = crud.update_product(db, product_id, data)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

def delete_product(db: Session, product_id: int):
    product = crud.delete_product(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted successfully"}
