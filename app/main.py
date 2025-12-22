from fastapi import FastAPI
from app.database.connection import engine
from app.database.base import Base

# Import models (VERY IMPORTANT)
from app.models.customer import Customer
from app.models.customer_product import CustomerProduct

app = FastAPI(title="Products API")

@app.get("/")
def root():
    return {"message": "Products API is running"}

# Create tables
Base.metadata.create_all(bind=engine)
