from sqlalchemy.orm import Session
from app.models.customer import Customer

def get_customers_with_products(db: Session):
    return db.query(Customer).all()
