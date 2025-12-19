from fastapi import FastAPI
from app.router.product import router as product_router

app = FastAPI(title="Products API")

@app.get("/")
def root():
    return {"message": "Products API is running"}

app.include_router(product_router)
