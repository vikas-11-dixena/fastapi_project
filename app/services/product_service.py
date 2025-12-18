from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.crud import product as product_crud
from app.schemas.product import ProductCreate, ProductUpdate
from app.logger.logger import get_logger

# Logger (console + file handler already configured)
logger = get_logger(__name__)

# Search bar for products (LIKE)
def search_products(db: Session, keyword: str): # Search products by keyword
    products = product_crud.search_product_like(db, keyword) # Call CRUD to search products

    if not products:
        logger.warning(f"No products found for keyword: {keyword}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No products found"
        ) # Raise 404 if no products found

    return products # Return found products

# =========================
# CREATE PRODUCT
# =========================
def create_product(db: Session, data: ProductCreate):
    logger.info("Creating new product")
    return product_crud.create_product(db, data)


# =========================
# READ ALL PRODUCTS
# =========================
def get_all_products(db: Session):
    logger.info("Fetching all products")
    return product_crud.get_products(db)


# =========================
# READ PRODUCT BY ID
# =========================
def get_product(db: Session, product_id: int):
    logger.info(f"Fetching product with id={product_id}")

    product = product_crud.get_product_by_id(db, product_id)
    if not product:
        logger.warning(f"Product not found: id={product_id}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found",
        )

    return product


# =========================
# UPDATE PRODUCT
# =========================
def update_product(db: Session, product_id: int, data: ProductUpdate):
    logger.info(f"Updating product with id={product_id}")

    product = product_crud.update_product(db, product_id, data)
    if not product:
        logger.warning(f"Product not found for update: id={product_id}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found",
        )

    return product


# =========================
# DELETE PRODUCT
# =========================
def delete_product(db: Session, product_id: int):
    logger.info(f"Deleting product with id={product_id}")

    product = product_crud.delete_product(db, product_id)
    if not product:
        logger.warning(f"Product not found for delete: id={product_id}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found",
        )

    return {"message": "Product deleted successfully"}
