from app.db.base import Base
from app.db.session import engine

# IMPORTANT: import models so SQLAlchemy knows tables
from app.models.product import Product

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()
