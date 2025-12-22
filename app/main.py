from fastapi import FastAPI
from app.db.session import engine
from app.db.base import Base

# Import models (VERY IMPORTANT)
from app.models.customer import Customer
from app.models.customer_product import CustomerProduct

app = FastAPI(title="Products API")

@app.get("/")
def root():
    return {"message": "Products API is running"}

# Create tables
Base.metadata.create_all(bind=engine)
