from enum import Enum
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, DateTime, LargeBinary
from sqlalchemy.orm import relationship
import datetime

from .database import Base


class UserTypes(Enum):
    DIRECTION = "direction"
    PIZZERIA = "pizzeria"
    AUTHED_USER = "authed_user"
    INACTIVE = "inactive"
    GUEST = "guest"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    pizzeria_ref = Column(Integer, ForeignKey("pizzerias.id"))

    type = Column(String, default="authed_user")
    forename = Column(String)  # first name
    email = Column(String)

    hashed_password = Column(String)

    orders = relationship("Order", back_populates="user_ref")


class Pizzeria(Base):
    __tablename__ = "pizzerias"

    id = Column(Integer, primary_key=True, index=True)
    is_open = Column(Boolean)
    is_delivery_avbl = Column(Boolean)

    orders = relationship("Order", back_populates="pizzeria_ref")
    products = relationship("PizzeriaProduct", back_populates="pizzeria_ref")


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    pizzeria_id = Column(Integer, ForeignKey("pizzerias.id"))

    date = Column(DateTime, default=datetime.datetime.now())
    delivery_adds = Column(String)
    type = Column(String)
    status = Column(String)

    products = relationship("OrderProduct", back_populates="order_ref")
    pizzeria_ref = relationship("Pizzeria", back_populates="orders")
    user_ref = relationship("User", back_populates="orders")


class Product(Base):
    __abstract__ = True

    name = Column(String)
    price = Column(Float)


class OrderProduct(Product):
    __tablename__ = "order_products"

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey("orders.id"))

    order_ref = relationship("Order", back_populates="products")


class PizzeriaProduct(Product):
    __tablename__ = "pizzeria_products"

    id = Column(Integer, primary_key=True)
    pizzeria_id = Column(Integer, ForeignKey("pizzerias.id"))

    pizzeria_ref = relationship("Pizzeria", back_populates="products")
