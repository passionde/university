from PyQt5 import QtWidgets, QtCore, QtGui

from dbcore import core
from dialog import edit_product_dialog


class EditProductDlg(edit_product_dialog.Ui_EditProduct):
    def __init__(self, dlg: QtWidgets.QDialog, db: core.Database, id_product: int):
        super().__init__()

        self.dlg = dlg
        self.db = db
        self.id_product = id_product

        self.setupUi(dlg)

        self.buttonBox.accepted.disconnect()
        self.buttonBox.accepted.connect(self.accept_handler)

        product = self.db.get_product(id_product)

        self.lineEdit.setValidator(QtGui.QIntValidator(1, 999_999_999))
        self.title.setText(product.product_name)
        self.on_sale.setChecked(product.on_sale)

        for change in self.db.get_types_change():
            self.type_change.addItem(change.title, change.type_id)

    def accept_handler(self):
        if self.lineEdit.text() and int(self.lineEdit.text()) != 0:
            self.db.new_change_quantity_goods({
                "quantity": int(self.lineEdit.text()),
                "comment": self.comment.toPlainText(),
                "product_id": self.id_product,
                "type_id": self.type_change.currentData()
            })

        self.db.change_sale_mode(self.id_product, self.on_sale.isChecked())
        self.dlg.accept()
