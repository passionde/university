from PyQt5 import QtWidgets

from dbcore import core
from dialog import edit_employee_dialog
from widget.admin_wgts import ListEmployeeWidget


class EditEmployeeDlg(edit_employee_dialog.Ui_EditEmployee):
    def __init__(self, dlg: QtWidgets.QDialog, db: core.Database):
        super().__init__()

        self.dlg = dlg
        self.db = db

        self.setupUi(dlg)

        self.list_seller_wgt = ListEmployeeWidget(self.list_seller, self.db.get_employee_list())

        self.buttonBox.accepted.disconnect()
        self.buttonBox.accepted.connect(self.accept_handler)

    def accept_handler(self):
        items = self.list_seller.findChildren(QtWidgets.QComboBox)
        if items:
            for item in items:
                data = str(item.currentData()).rsplit(maxsplit=1)
                self.db.change_seller_active(data[0], bool(int(data[1])))

        self.dlg.accept()
