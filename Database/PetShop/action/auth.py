from action import seller, admin
from dbcore import core
from ui import auth
from PyQt5 import QtWidgets


class AuthUi(auth.Ui_AuthWindow):
    def __init__(self, db: core.Database, window: QtWidgets.QMainWindow, seller_ui: seller.SellerUI, admin_ui: admin.AdminUI):
        self.window = window
        self.db = db
        self.seller_ui = seller_ui
        self.admin_ui = admin_ui

    def setup(self):
        self.setupUi(self.window)
        self.add_functions()

    def add_functions(self):
        self.auth_btn.clicked.connect(self.click_btn_auth)

    def click_btn_auth(self):
        is_auth, is_admin = self.db.auth(self.login_edit.text(), self.password_edit.text())

        if not is_auth:
            self.password_edit.setText("")
            self.password_edit.setPlaceholderText("Неверный пароль")
            return

        if not is_admin:
            self.seller_ui.set_login_seller(self.login_edit.text())
            self.seller_ui.setup(self.window)
        else:
            self.admin_ui.setup(self.window)

