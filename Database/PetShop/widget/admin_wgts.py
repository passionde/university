import decimal

from PyQt5 import QtCore, QtGui, QtWidgets

import dbcore.core
from action import edit_product_dlg


class ListEmployeeWidget:
    def __init__(self, list_wgt: QtWidgets.QListWidget, employees_list):
        super().__init__()

        font = QtGui.QFont()
        font.setPointSize(10)
        list_wgt.setFont(font)

        for login, name, is_work in employees_list:

            layout = QtWidgets.QHBoxLayout()
            layout.setContentsMargins(0, 0, 0, 0)

            layout.addWidget(QtWidgets.QLabel(f"{name} ({login})"))
            combo_list = QtWidgets.QComboBox()

            if is_work:
                combo_list.addItem("Активный аккаунт", f"{login} 1")
                combo_list.addItem("Аккаунт приостановлен", f"{login} 0")
            else:
                combo_list.addItem("Аккаунт приостановлен", f"{login} 0")
                combo_list.addItem("Активный аккаунт", f"{login} 1")

            layout.addWidget(combo_list)

            layout.setStretch(0, 3)
            layout.setStretch(1, 1)

            wgt = QtWidgets.QWidget()
            wgt.setLayout(layout)

            item_wgt = QtWidgets.QListWidgetItem(list_wgt)

            list_wgt.setItemWidget(item_wgt, wgt)


class TableProductsWidget(QtWidgets.QTableWidget):
    def __init__(self, products_data: dict, labels: list, db: dbcore.core.Database):
        super().__init__()

        self.db = db
        self.setColumnCount(len(labels))
        self.setRowCount(len(products_data))

        self.setHorizontalHeaderLabels(labels)

        for row_idx, row in enumerate(products_data.values(), start=0):
            for cell_idx, cell in enumerate(row[1:], start=0):
                text = f"{cell}"
                if isinstance(cell, decimal.Decimal):
                    text = f"{float(cell):.2f}"
                elif cell is None:
                    text = "-"

                item = QtWidgets.QTableWidgetItem(text)
                if isinstance(cell, int) and cell < 0:
                    item.setBackground(QtGui.QColor(255, 0, 0, 100))
                self.setItem(row_idx, cell_idx, item)

            btn_add = QtWidgets.QPushButton("✎")
            btn_add.setCursor(QtCore.Qt.PointingHandCursor)
            btn_add.clicked.connect(self.show_edit_product)

            id_cell = QtWidgets.QLineEdit(f"{row[0]}")
            id_cell.hide()

            layout = QtWidgets.QHBoxLayout()
            layout.setContentsMargins(0, 0, 0, 0)

            layout.addWidget(btn_add)
            layout.addWidget(id_cell)

            wgt = QtWidgets.QWidget()
            wgt.setLayout(layout)
            self.setCellWidget(row_idx, len(labels) - 1, wgt)

        self.setSortingEnabled(True)
        self.resizeColumnsToContents()
        self.horizontalHeader().setStretchLastSection(True)
        self.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

    def show_edit_product(self):
        id_product = self.sender().parent().findChild(QtWidgets.QLineEdit)

        dlg = QtWidgets.QDialog()
        dlg.setWindowFlags(dlg.windowFlags() & ~QtCore.Qt.WindowContextHelpButtonHint)
        ui_dlg = edit_product_dlg.EditProductDlg(dlg, self.db, int(id_product.text()))

        dlg.show()
        dlg.exec()
