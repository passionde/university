import csv

from dbcore import core
from ui import admin_window
from widget import admin_wgts
from PyQt5 import QtWidgets, QtGui, QtCore
from action import add_employee_dlg, add_product_dlg, add_category_dlg, edit_employee_dlg, export_report


class AdminUI(admin_window.Ui_AdminWindow):
    def __init__(self, db: core.Database):
        super(AdminUI, self).__init__()

        self.db = db
        self.window: QtWidgets.QMainWindow | None = None
        self.table_products: admin_wgts.TableProductsWidget | None = None

        self.catalog_data_for_search = self.db.get_catalog_products_info(join_field=True)
        self.catalog_products_info = self.db.get_catalog_products_info_leftovers()

    def setup(self, window: QtWidgets.QMainWindow):
        self.window = window
        self.setupUi(window)
        self.view_products_list()
        self.add_function()

    def add_function(self):
        self.add_employee.triggered.connect(self.show_add_employee_dlg)
        self.add_product.triggered.connect(self.show_add_product_dlg)
        self.add_category.triggered.connect(self.show_add_category_dlg)
        self.edit_status_employee.triggered.connect(self.show_edit_employee_dlg)
        self.export_report.triggered.connect(self.show_export_report_dlg)
        self.search_edit.returnPressed.connect(self.display_search_results)
        self.reload.clicked.connect(self.view_products_list)

    def show_add_employee_dlg(self):
        dlg = QtWidgets.QDialog()
        dlg.setWindowFlags(dlg.windowFlags() & ~QtCore.Qt.WindowContextHelpButtonHint)
        ui_dlg = add_employee_dlg.NewEmployeeDlg(dlg, self.db)

        dlg.show()
        if dlg.exec():
            QtWidgets.QMessageBox.about(self.window, "Успех", f"Новый сотрудник добавлен!\n"
                                                              f"Логин: {ui_dlg.login.text()}\n"
                                                              f"Пароль: {ui_dlg.password.text()}")

    def show_add_product_dlg(self):
        dlg = QtWidgets.QDialog()
        dlg.setWindowFlags(dlg.windowFlags() & ~QtCore.Qt.WindowContextHelpButtonHint)
        ui_dlg = add_product_dlg.NewProductDlg(dlg, self.db)

        dlg.show()
        if dlg.exec():
            QtWidgets.QMessageBox.about(self.window, "Успех", f"Товар \"{ui_dlg.product_name.text()}\" добавлен")

    def show_add_category_dlg(self):
        dlg = QtWidgets.QDialog()
        dlg.setWindowFlags(dlg.windowFlags() & ~QtCore.Qt.WindowContextHelpButtonHint)
        ui_dlg = add_category_dlg.NewCategoryDlg(dlg, self.db)

        dlg.show()
        if dlg.exec():
            QtWidgets.QMessageBox.about(self.window, "Успех", f"Категория \"{ui_dlg.category_name.text()}\" добавлена")

    def show_edit_employee_dlg(self):
        dlg = QtWidgets.QDialog()
        dlg.setWindowFlags(dlg.windowFlags() & ~QtCore.Qt.WindowContextHelpButtonHint)
        ui_dlg = edit_employee_dlg.EditEmployeeDlg(dlg, self.db)

        dlg.show()
        dlg.exec()

    def show_export_report_dlg(self):
        dlg = QtWidgets.QDialog()
        dlg.setWindowFlags(dlg.windowFlags() & ~QtCore.Qt.WindowContextHelpButtonHint)
        ui_dlg = export_report.ExportReportDlg(dlg, self.db)

        dlg.show()
        dlg.exec()

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

        self.table_products = admin_wgts.TableProductsWidget(
            products_matching_request,
            ["Наименование", "Цена", "Категория", "Номер штрихкода", "Остатки на складе", "Изменить"],
            self.db
        )
        self.catalog_frame.addWidget(self.table_products)

    # очистка контейнера каталога
    def clear_catalog_frame(self):
        for i in reversed(range(self.catalog_frame.count())):
            widget_to_remove = self.catalog_frame.itemAt(i).widget()
            self.catalog_frame.removeWidget(widget_to_remove)
            widget_to_remove.setParent(None)

    # отрисовка списков конкретной категории
    def view_products_list(self):
        self.clear_catalog_frame()
        self.table_products = admin_wgts.TableProductsWidget(
            self.catalog_products_info,
            ["Наименование", "Цена", "Категория", "Номер штрихкода", "Остатки на складе", "Изменить"],
            self.db
        )
        self.catalog_frame.addWidget(self.table_products)
