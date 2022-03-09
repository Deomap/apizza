from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship
from typing import Optional

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    is_active = Column(Boolean, default=True)

    orders = relationship("Order", back_populates="user_ref")


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    date = Column(DateTime)
    delivery_adds = Column(String)
    type = Column(String)

    products = relationship("Product", back_populates="order_ref")
    user_ref = relationship("User", back_populates="orders")


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    name = Column(String)
    price = Column(Float)

    order_ref = relationship("Order", back_populates="products")
