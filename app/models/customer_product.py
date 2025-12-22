from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class CustomerProduct(Base):
    __tablename__ = "customer_product"

    id = Column(Integer, primary_key=True, index=True)

    # 🔹 Foreign Key (JOIN point)
    customer_id = Column(
        Integer,
        ForeignKey("customer.id"),
        nullable=False
    )

    name = Column(String(100), nullable=False)          # product name
    description = Column(String(255))
    price = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False)

    # 🔹 Relationship
    customer = relationship("Customer", back_populates="products")
