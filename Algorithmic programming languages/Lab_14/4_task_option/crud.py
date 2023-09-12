from sqlalchemy import create_engine
from sqlalchemy.orm import Session

import models


engine = create_engine('sqlite:///sqlite3.db')
session = Session(bind=engine)


def create_all():
    models.Base.metadata.create_all(bind=engine)


def add_color(color_name):
    new_color = models.Color(color_name=color_name)
    session.add(new_color)
    session.commit()


def add_category(category_name):
    new_category = models.Category(category_name=category_name)
    session.add(new_category)
    session.commit()


def add_product(name, price, in_stock, color_id, categories_id):
    # Создание товара
    colors = session.query(models.Color).filter(models.Color.id == color_id)
    assert colors.count(), f"Цвет с ID:<{color_id}> не найден"
    color = colors.first()

    new_product = models.Product(
        product_name=name,
        price=price,
        in_stock=in_stock,
        color_id=color
    )

    color.products.append(new_product)

    # Установка категорий товара
    categories = session.query(models.Category).filter(models.Category.id.in_(categories_id))
    assert categories.count(), f"В переданном списке ID категорий:{categories} не найдено ни одного значения в БД"

    for category in categories.all():
        new_product.categories.append(category)
        session.add(category)

    session.add(new_product)
    session.commit()


def all_products():
    products = session.query(models.Product).all()
    print("Все дисциплины:")
    for product in products:
        color = session.query(models.Color).filter(models.Color.id == product.color_id).first()
        print(f"\t<{product.id}> {product.product_name.title()} ({color.color_name}): цена - {product.price}, в наличии - {product.in_stock}")


def all_colors():
    colors = session.query(models.Color).all()
    print("Все цвета (цвет -> кол-во товаров):")
    for color in colors:
        print(f"\t{color.color_name} -> {len(color.products)}")