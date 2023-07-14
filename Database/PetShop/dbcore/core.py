from PyQt5 import QtGui
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from . import models


class Database:
    def __init__(self, str_connect):
        self.engine = create_engine(str_connect)
        self.s = Session(bind=self.engine)

    def init_tables(self):
        models.Base.metadata.create_all(self.engine)

        self.new_type_change("Продажа", False)
        self.new_type_change("Списание/утилизация", False)
        self.new_type_change("Поставка", True)
        self.new_seller("admin", "Администратор", "admin1234", is_admin=True)
        self.new_seller("seller", "Пользователь по умолчанию", "seller")
        self.new_category("Прочее")

    def auth(self, login: str, password: str) -> (bool, bool):
        seller = self.s.query(models.Seller).filter(
            models.Seller.login == login, models.Seller.hash_password == password
        ).first()

        if seller is None:
            return False, False

        if not seller.is_works:
            return False, False

        return True, seller.is_admin

    def test(self):
        self.new_category("Корм")

        self.new_product({
            "product_name": "Корм 1",
            "price": 999,
            "category_id": 2
        })
        self.new_product({
            "product_name": "Корм 2",
            "price": 9994,
            "category_id": 2
        })
        self.new_product({
            "product_name": "Корм 3",
            "price": 9999,
            "category_id": 2
        })
        self.new_product({
            "product_name": "Корм 4",
            "price": 199,
            "category_id": 2
        })
        self.new_product({
            "product_name": "Корм 5",
            "price": 999,
            "category_id": 2
        })
        self.new_product({
            "product_name": "Корм 6",
            "price": 969,
            "category_id": 2
        })

        self.new_category("Наполнители")
        self.new_product({
            "product_name": "Наполнитель 1",
            "price": 999,
            "category_id": 3
        })
        self.new_product({
            "product_name": "Наполнитель 2",
            "price": 99.5,
            "category_id": 3
        })
        self.new_product({
            "product_name": "Наполнитель 3",
            "price": 99.5,
            "category_id": 3
        })
        self.new_product({
            "product_name": "Наполнитель 4",
            "price": 99.5,
            "category_id": 3,
            "barcode_number": 1872368192379
        })
        self.new_product({
            "product_name": "Наполнитель 5",
            "price": 99.5,
            "category_id": 3,
            "barcode_number": 187236823492379
        })
        self.new_product({
            "product_name": "Прочий товар 1",
            "price": 99.5,
            "category_id": 1,
            "barcode_number": 187232379
        })

    def new_seller(self, login: str, name: str, password: str, is_admin=False):
        seller = models.Seller(
            name=name,
            login=login,
            hash_password=password,
            is_admin=is_admin,
            is_works=True
        )

        self.s.add(seller)
        self.s.commit()

    def new_change_quantity_goods(self, data: dict):
        quantity = data.get("quantity")
        comment = data.get("comment")
        product_id = data.get("product_id")
        type_id = data.get("type_id")

        assert type_id is not None, "empty type_id"
        assert product_id is not None, "empty product_id"
        assert quantity is not None, "empty quantity"

        type_change = self.s.query(models.TypeChange).get(type_id)
        assert type_change is not None, "type_change not found"

        change = models.ChangeQuantityGoods(
            quantity=quantity if type_change.is_increase else -quantity,
            comment=comment,
            product_id=product_id,
            type_id=type_id
        )

        self.s.add(change)
        self.s.commit()

    def new_order(self, login: str, product_list: list[tuple[int, int]]):
        seller = self.s.query(models.Seller).get(login)

        assert seller is not None, "login not found"

        order = models.Order(
            seller_login=seller.login
        )

        self.s.add(order)
        self.s.commit()

        # todo при необходимости добавить валидацию
        for product_id, quantity in product_list:
            if quantity == 0:
                continue

            item = models.ProductInOrder(
                quantity=quantity,
                product_id=product_id,
                order_id=order.order_id
            )
            self.s.add(item)

            self.new_change_quantity_goods({
                "quantity": quantity,
                "comment": f"Добавлено автоматически. Чек №{order.order_id} от {order.order_date}, продавец {order.seller_login}",
                "product_id": product_id,
                "type_id": 1  # todo должен добавляться автоматически
            })

        self.s.commit()
        return order.order_id

    def new_category(self, category_name: str):
        category = models.Category(
            category_name=category_name,
            is_active=True
        )

        self.s.add(category)
        self.s.commit()

    def new_type_change(self, title: str, is_increase: bool):
        type_change = models.TypeChange(
            title=title,
            is_increase=is_increase
        )

        self.s.add(type_change)
        self.s.commit()

    def new_product(self, data: dict):
        product_name = data.get("product_name")
        price = data.get("price")
        barcode_number = data.get("barcode_number")
        category_id = data.get("category_id")

        assert product_name is not None or price is not None, "empty price or name"
        if category_id is None:
            assert "empty subcategory_id and category_id"

        product = models.Product(
            product_name=product_name,
            price=price,
            barcode_number=barcode_number,
            category_id=category_id
        )

        self.s.add(product)
        self.s.commit()

    def change_seller_active(self, login: str, is_active: bool):
        seller = self.s.query(models.Seller).get(login)

        if seller is None:
            return

        seller.is_works = is_active
        self.s.add(seller)
        self.s.commit()

    def change_sale_mode(self, product_id: int, on_sale: bool):
        product = self.s.query(models.Category).get(product_id)
        if product is None:
            return

        product.on_sale = on_sale
        self.s.add(product)
        self.s.commit()

    def change_active_category(self, category_id, is_active):
        category = self.s.query(models.Category).get(category_id)
        if category is None:
            return

        category.is_active = is_active
        self.s.add(category)
        self.s.commit()

    def get_employee_list(self):
        employee_list = []

        for employee in self.s.query(models.Seller).all():
            if employee.is_admin:
                continue

            employee_list.append([
                employee.login, employee.name, employee.is_works
            ])

        return employee_list

    def get_catalog_tree(self):
        catalog_list = {}
        cache_cat = {}

        products = self.s.query(models.Product).all()
        for product in products:
            category_name = cache_cat.get(product.category_id)

            if not category_name:
                category = self.s.query(models.Category).get(product.category_id)
                if category is not None:
                    category_name = category.category_name

                catalog_list[category_name] = {}
                cache_cat[product.category_id] = category_name

            catalog_list[category_name][product.product_id] = [
                product.product_id,
                product.product_name,
                product.price,
                category_name,
                product.barcode_number
            ]

        return catalog_list

    def get_categories_list(self):
        categories_list = []

        for category in self.s.query(models.Category).all():
            categories_list.append(category.category_name)

        categories_list.sort()
        return categories_list

    def get_catalog_products_info(self, join_field=False):
        catalog_products_info = {}

        for product in self.s.query(models.Product).all():
            category = self.s.query(models.Category).get(product.category_id)

            if not join_field:
                catalog_products_info[product.product_id] = [
                    product.product_id,
                    product.product_name,
                    product.price,
                    None if not category else category.category_name,
                    product.barcode_number
                ]
                continue

            catalog_products_info[product.product_id] = "".join([
                # f"{product.product_id}",
                product.product_name.replace(" ", "").replace("\t", "").replace("\n", "").lower(),
                f"{product.price}",
                "" if not category else category.category_name.replace(" ", "").replace("\t", "").replace("\n",
                                                                                                          "").lower(),
                f"{product.barcode_number}"
            ])

        return catalog_products_info

    def get_catalog_products_info_leftovers(self, join_field=False):
        catalog_products_info = {}

        for product in self.s.query(models.Product).all():
            category = self.s.query(models.Category).get(product.category_id)

            changes = self.s.query(models.ChangeQuantityGoods.quantity).filter(
                models.ChangeQuantityGoods.product_id == product.product_id
            ).all()

            leftovers = 0
            for change in changes:
                leftovers += change[0]

            catalog_products_info[product.product_id] = [
                product.product_id,
                product.product_name,
                product.price,
                None if not category else category.category_name,
                product.barcode_number,
                leftovers
            ]

        return catalog_products_info

    def get_categories_dict(self):
        categories_dict = {}

        for category in self.s.query(models.Category).all():
            categories_dict[category.category_name] = category.category_id

        return dict(sorted(categories_dict.items()))

    def get_report_data(self):
        report_data = [["Номер чека", "Дата", "Логин продавца", "Наименование", "Категория", "Цена", "Количество"]]

        for order in self.s.query(models.Order).all():
            for product in order.products:
                row = [order.order_id, str(order.order_date), order.seller_login]
                product_info = self.s.query(models.Product).get(product.product_id)

                row.append(product_info.product_name)

                category = self.s.query(models.Category).get(product_info.category_id)
                category_name = "-"
                if category is not None:
                    category_name = category.category_name
                row.append(category_name)

                row.append(float(product_info.price))
                row.append(product.quantity)

                report_data.append(row)

        return report_data

    def is_exists_seller(self, login: str):
        if self.s.query(models.Seller).get(login):
            return True

        return False

    def is_exists_category(self, category_name: str):
        if self.s.query(models.Category).filter(models.Category.category_name == category_name).all():
            return True

        return False

    def get_product(self, product_id) -> models.Product:
        return self.s.query(models.Product).get(product_id)

    def get_types_change(self):
        return self.s.query(models.TypeChange).all()

