from sqlalchemy.orm import Session
from sqlalchemy import or_   # ✅ MISSING IMPORT FIXED

from app.models.product import Product
from app.schemas.product import ProductCreate, ProductUpdate


# =========================
# CREATE PRODUCT
# =========================
def create_product(db: Session, data: ProductCreate):
    product = Product(**data.dict())
    db.add(product)
    db.commit()
    db.refresh(product)
    return product


# =========================
# SEARCH PRODUCTS (LIKE)
# =========================
def search_products(db: Session, keyword: str):
    return (
        db.query(Product)
        .filter(
            or_(
                Product.name.ilike(f"%{keyword}%"),
                Product.description.ilike(f"%{keyword}%")
            )
        )
        .all()
    )


# =========================
# READ ALL PRODUCTS
# =========================
def get_all_products(db: Session):
    return db.query(Product).all()


# =========================
# READ PRODUCT BY ID
# =========================
def get_product_by_id(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()


# =========================
# UPDATE PRODUCT
# =========================
def update_product(db: Session, product_id: int, data: ProductUpdate):
    product = get_product_by_id(db, product_id)
    if not product:
        return None

    for key, value in data.dict(exclude_unset=True).items():
        setattr(product, key, value)

    db.commit()
    db.refresh(product)
    return product


# =========================
# DELETE PRODUCT
# =========================
def delete_product(db: Session, product_id: int):
    product = get_product_by_id(db, product_id)
    if not product:
        return None

    db.delete(product)
    db.commit()
    return product
