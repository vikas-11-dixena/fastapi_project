from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base import Base

class Customer(Base):
    __tablename__ = "customer"

    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String(100), nullable=False)

    # 🔹 Relationship
    products = relationship(
        "CustomerProduct",
        back_populates="customer",
        cascade="all, delete"
    )
