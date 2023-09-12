from sqlalchemy import Integer, String, Column, DateTime, ForeignKey, Numeric, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

from sqlalchemy.orm import relationship

Base = declarative_base()


class Seller(Base):
    __tablename__ = "Seller"
    login = Column(String(40), primary_key=True, nullable=False, unique=True)
    name = Column(String(100), nullable=False)
    hash_password = Column(Text(), nullable=False)

    is_admin = Column(Boolean(), default=False)
    is_works = Column(Boolean(), default=True)


class ProductInOrder(Base):
    __tablename__ = "ProductInOrder"
    product_in_order_id = Column(Integer(), primary_key=True, autoincrement=True)
    quantity = Column(Integer(), default=1)

    order_id = Column(Integer(), ForeignKey("Order.order_id"))
    product_id = Column(Integer(), ForeignKey("Product.product_id"))


class Order(Base):
    __tablename__ = "Order"
    order_id = Column(Integer(), primary_key=True, autoincrement=True)
    order_date = Column(DateTime(), default=datetime.now)
    seller_login = Column(Integer(), ForeignKey("Seller.login"))

    products = relationship("ProductInOrder", backref='order')


class Product(Base):
    __tablename__ = "Product"
    product_id = Column(Integer(), primary_key=True, autoincrement=True)
    product_name = Column(Text(), nullable=False)
    price = Column(Numeric(None, 2), nullable=False)
    barcode_number = Column(Integer())
    date_added = Column(DateTime(), default=datetime.now)
    on_sale = Column(Boolean(), default=True)
    category_id = Column(Integer(), ForeignKey("Category.category_id"))


class Category(Base):
    __tablename__ = "Category"
    category_id = Column(Integer(), primary_key=True, autoincrement=True)
    category_name = Column(String(200), nullable=False, unique=True)

    is_active = Column(Boolean(), default=True)
    products = relationship("Product")


class ChangeQuantityGoods(Base):
    __tablename__ = "ChangeQuantityGoods"
    change_id = Column(Integer(), primary_key=True, autoincrement=True)
    quantity = Column(Integer())
    change_date = Column(DateTime(), default=datetime.now)
    comment = Column(Text())

    product_id = Column(Integer(), ForeignKey("Product.product_id"))
    type_id = Column(Integer(), ForeignKey("TypeChange.type_id"))


class TypeChange(Base):
    __tablename__ = "TypeChange"
    type_id = Column(Integer(), primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    is_increase = Column(Boolean(), default=False)
