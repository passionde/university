from PyQt5 import QtWidgets

from dbcore import core
from dialog import new_category_dialog


class NewCategoryDlg(new_category_dialog.Ui_NewCategory):
    def __init__(self, dlg: QtWidgets.QDialog, db: core.Database):
        super().__init__()

        self.dlg = dlg
        self.db = db

        self.setupUi(dlg)
        self.buttonBox.accepted.disconnect()
        self.buttonBox.accepted.connect(self.accept_handler)

    def accept_handler(self):
        is_valid = True

        if not self.category_name.text():
            self.category_name.setPlaceholderText("Не указано название")
            is_valid = False

        if self.category_name.text() and self.db.is_exists_category(self.category_name.text()):
            self.category_name.setText("")
            self.category_name.setPlaceholderText("Категория уже существует")
            is_valid = False

        if is_valid:
            self.db.new_category(self.category_name.text())
            self.dlg.accept()