import sys

from PyQt5 import QtWidgets

import action.auth
import action.seller
import action.admin
from dbcore import core

if __name__ == "__main__":
    db = core.Database("sqlite:///sqlite3.db")
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()

    seller_ui = action.seller.SellerUI(db)
    admin_ui = action.admin.AdminUI(db)
    auth_ui = action.auth.AuthUi(db, window, seller_ui, admin_ui)

    auth_ui.setup()
    window.show()
    app.exec_()
