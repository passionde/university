from dbcore import core
from ui import seller_window
from widget import seller_wgts
from PyQt5 import QtWidgets, QtCore


class SellerUI(seller_window.Ui_SellerWindow):
    def __init__(self, db: core.Database):
        super().__init__()

        self.order: seller_wgts.TableOrderWidget | None = None
        self.table_products: seller_wgts.TableProductsWidget | None = None
        self.window: QtWidgets.QMainWindow | None = None
        self.login: str | None = None

        self.db = db

        self.catalog_data = self.db.get_catalog_tree()
        self.catalog_products_info = self.db.get_catalog_products_info()
        self.catalog_data_for_search = self.db.get_catalog_products_info(join_field=True)

        self.categories_list = seller_wgts.ListCategoryWidget(self.db.get_categories_list())

    def setup(self, window: QtWidgets.QMainWindow):
        self.window = window
        self.setupUi(window)

        self.catalog_frame.addWidget(self.categories_list)
        self.order = seller_wgts.TableOrderWidget(
            self.order_table, self.catalog_products_info, ["id", "Название", "Цена", "Кол-во"]
        )

        self.add_functions()

    # связывание событий и их обработчиков
    def add_functions(self):
        self.back.clicked.connect(self.back_to_categories)
        self.categories_list.itemDoubleClicked.connect(self.go_to_products_list)
        self.cancel_btn.clicked.connect(self.clear_order_table)
        self.pay_btn.clicked.connect(self.create_order)
        self.search_btn.clicked.connect(self.display_search_results)
        self.search_edit.returnPressed.connect(self.display_search_results)
        self.order.table.itemChanged.connect(self.calc_total)

    # добавление продукта в таблицу заказа
    def handler_add_product(self):
        id_product = self.window.sender().parent().findChild(QtWidgets.QLineEdit)
        self.order.insert_product(id_product.text())
        self.calc_total()

    # обновление надписи total
    def calc_total(self):
        self.total.setText(f"Итого: {self.order.calc_total()}")

    # создание ордера
    def create_order(self):
        order_list = self.order.get_order_list()

        if not order_list:
            QtWidgets.QMessageBox.about(self.window, "Отказ", "Пустой список товаров")
            return

        order_id = self.db.new_order(self.login, order_list)
        QtWidgets.QMessageBox.about(self.window, "Успех", f"Чек №{order_id} добавлен, общая стоимость "
                                                          f"{self.total.text()[7:]} ₽")
        self.clear_order_table()

    # установка логина
    def set_login_seller(self, login: str):
        self.login = login

    # очистка контейнера каталога
    def clear_catalog_frame(self):
        for i in reversed(range(self.catalog_frame.count())):
            widget_to_remove = self.catalog_frame.itemAt(i).widget()
            self.catalog_frame.removeWidget(widget_to_remove)
            widget_to_remove.setParent(None)

    # очистка таблицы заказа
    def clear_order_table(self):
        self.order.clear()
        self.total.setText("Итого: 0")

    # возврат к списку с категориями
    def back_to_categories(self):
        self.clear_catalog_frame()
        self.catalog_frame.addWidget(self.categories_list)

    # отрисовка списков конкретной категории
    def go_to_products_list(self, item: QtWidgets.QListWidgetItem):
        self.clear_catalog_frame()
        self.table_products = seller_wgts.TableProductsWidget(
            self.catalog_data.get(item.text(), []),
            ["Наименование", "Цена", "Категория", "Номер штрихкода", "Добавить"],
            self.handler_add_product
        )
        self.catalog_frame.addWidget(self.table_products)

    # отображение результатов поиска
    def display_search_results(self):
        search_query = self.search_edit.text().replace(" ", "").replace("\t", "").replace("\n", "").lower()

        if len(search_query) == 0:
            return

        products_matching_request = {}

        for id_product, data_str in self.catalog_data_for_search.items():
            if data_str.find(search_query) != -1:
                product_data = self.catalog_products_info.get(id_product)
                if product_data:
                    products_matching_request[id_product] = product_data

        self.clear_catalog_frame()
        if not products_matching_request:
            label = QtWidgets.QLabel(f'По запросу "{self.search_edit.text()}" ничего не найдено')
            label.setAlignment(QtCore.Qt.AlignCenter)
            self.catalog_frame.addWidget(label)
            return

        self.table_products = seller_wgts.TableProductsWidget(
            products_matching_request,
            ["Наименование", "Цена", "Категория", "Номер штрихкода", "Добавить"],
            self.handler_add_product
        )
        self.catalog_frame.addWidget(self.table_products)


