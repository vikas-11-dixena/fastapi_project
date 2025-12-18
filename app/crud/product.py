from sqlalchemy.orm import Session
from app.models.product import Product
from app.schemas.product import ProductCreate, ProductUpdate
from app.utils.common import paginate

# SEARCH PRODUCTS (LIKE)
def search_product_like(db: Session, keyword: str):
    return (
        db.query(Product)
        .filter(Product.name.ilike(f"%{keyword}%"))
        .all()
    )


def create_product(db: Session, data: ProductCreate):
    product = Product(**data.model_dump())
    db.add(product)
    db.commit()
    db.refresh(product)
    return product


def get_products(db: Session):
    return db.query(Product).all()


def get_product_by_id(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()


def update_product(db: Session, product_id: int, data: ProductUpdate):
    product = get_product_by_id(db, product_id)
    if not product:
        return None

    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(product, key, value)

    db.commit()
    db.refresh(product)
    return product


def delete_product(db: Session, product_id: int):
    product = get_product_by_id(db, product_id)
    if not product:
        return None

    db.delete(product)
    db.commit()
    return product

def get_products_paginated(db, page: int, limit: int):
    query = db.query(Product)
    return paginate(query, page, limit)