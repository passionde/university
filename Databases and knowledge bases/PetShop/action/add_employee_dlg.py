from PyQt5 import QtWidgets

from dbcore import core
from dialog import new_employee_dialog


class NewEmployeeDlg(new_employee_dialog.Ui_NewEmployee):
    def __init__(self, dlg: QtWidgets.QDialog, db: core.Database):
        super().__init__()

        self.dlg = dlg
        self.db = db

        self.setupUi(dlg)
        self.buttonBox.accepted.disconnect()
        self.buttonBox.accepted.connect(self.accept_handler)

    def accept_handler(self):
        is_valid = True

        if len(self.password.text()) < 5:
            self.password.setText("")
            self.password.setPlaceholderText("Слабый пароль")
            is_valid = False

        if not self.full_name.text():
            self.full_name.setPlaceholderText("Не указаны ФИО")
            is_valid = False

        if not self.login.text():
            self.login.setPlaceholderText("Не указан логин")
            is_valid = False

        if self.login.text() and self.db.is_exists_seller(self.login.text()):
            self.login.setText("")
            self.login.setPlaceholderText("Логин занят")
            is_valid = False

        if is_valid:
            self.db.new_seller(self.login.text(), self.full_name.text(), self.password.text())
            self.dlg.accept()