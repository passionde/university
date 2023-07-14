from sqlalchemy import Column, ForeignKey, Integer, String, create_engine, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()

product_category = Table(
    'category_product', Base.metadata,
    Column("product_id", Integer(), ForeignKey("products.id")),
    Column("category_id", Integer(), ForeignKey("categories.id"))
)


class Color(Base):
    __tablename__ = "colors"

    id = Column(Integer, primary_key=True, autoincrement=True)
    color_name = Column(String())

    products = relationship("Product")


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, autoincrement=True)
    product_name = Column(String())
    price = Column(Integer())
    in_stock = Column(Integer())

    color_id = Column(Integer(), ForeignKey('colors.id'))
    categories = relationship("Category", secondary=product_category, backref=backref("products"))


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, autoincrement=True)
    category_name = Column(String())


