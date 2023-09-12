from PyQt5 import QtWidgets, QtCore, QtGui

from dbcore import core
from dialog import new_product_dialog


class NewProductDlg(new_product_dialog.Ui_NewProduct):
    def __init__(self, dlg: QtWidgets.QDialog, db: core.Database):
        super().__init__()

        self.dlg = dlg
        self.db = db

        self.setupUi(dlg)

        self.price.setValidator(QtGui.QDoubleValidator(0, 9_999_999_999, 2, self.price))
        self.set_items_category()

        self.buttonBox.accepted.disconnect()
        self.buttonBox.accepted.connect(self.accept_handler)

    def set_items_category(self):
        categories = self.db.get_categories_dict()
        if not categories:
            return

        for category, id_category in categories.items():
            self.category.addItem(category, id_category)

    def accept_handler(self):
        is_valid = True

        if not self.product_name.text():
            self.product_name.setPlaceholderText("Не указано название товара")
            is_valid = False

        if not self.price.text():
            self.price.setPlaceholderText("Не указана цена")
            is_valid = False

        if is_valid:
            self.db.new_product({
                "product_name": self.product_name.text(),
                "price": float(self.price.text().replace(",", ".")),
                "category_id": self.category.currentData(),
                "barcode_number": None if not self.barcode.text() else self.barcode.text()
            })

            self.dlg.accept()