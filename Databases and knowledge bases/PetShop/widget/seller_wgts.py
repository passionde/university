import decimal

from PyQt5 import QtCore, QtGui, QtWidgets


class ListCategoryWidget(QtWidgets.QListWidget):
    def __init__(self, categories):
        super(ListCategoryWidget, self).__init__()

        font = QtGui.QFont()
        font.setPointSize(10)
        self.setFont(font)

        for category in categories:
            self.addItem(category)


class TableProductsWidget(QtWidgets.QTableWidget):
    def __init__(self, tree_data: dict, labels: list, handler):
        super().__init__()
        self.setColumnCount(len(labels))
        self.setRowCount(len(tree_data))
        self.handler = handler

        self.setHorizontalHeaderLabels(labels)
        for row_idx, row in enumerate(tree_data.values(), start=0):
            for cell_idx, cell in enumerate(row[1:], start=0):
                text = f"{cell}"
                if isinstance(cell, decimal.Decimal):
                    text = f"{float(cell):.2f}"
                elif cell is None:
                    text = "-"

                self.setItem(row_idx, cell_idx, QtWidgets.QTableWidgetItem(text))

            btn_add = QtWidgets.QPushButton("➕")
            btn_add.setCursor(QtCore.Qt.PointingHandCursor)
            btn_add.clicked.connect(handler)

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


class TableOrderWidget:
    def __init__(self, table: QtWidgets.QTableWidget, tree_data: dict, labels: list):
        self.table = table
        self.tree_data = tree_data  # todo id: data
        self.labels = labels
        self.current_products = {}

        self.table.setColumnCount(len(labels))
        self.table.setRowCount(0)

        self.table.setHorizontalHeaderLabels(labels)
        self.table.setColumnHidden(0, True)

        self.table.resizeColumnsToContents()
        self.table.horizontalHeader().resizeSection(1, 150)
        self.table.horizontalHeader().resizeSection(2, 90)
        self.table.horizontalHeader().setStretchLastSection(True)

    def insert_product(self, product_id: str):
        if not product_id.isdigit():
            return

        product_id = int(product_id)

        # Инкремент, если товар есть в ордере
        if self.current_products.get(product_id):
            for row_idx in range(self.table.rowCount()):
                if self.table.item(row_idx, 0).text() == f"{product_id}":
                    item = self.table.item(row_idx, 3)
                    if item and item.text().isdigit():
                        self.table.setItem(row_idx, 3, QtWidgets.QTableWidgetItem(f"{int(item.text()) + 1}"))
                    break
            return

        if not self.tree_data.get(product_id):
            return

        self.table.insertRow(self.table.rowCount())
        self.current_products[product_id] = True

        product_data = self.tree_data.get(product_id)

        item = QtWidgets.QTableWidgetItem(str(product_id))
        item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
        self.table.setItem(self.table.rowCount() - 1, 0, item)

        item = QtWidgets.QTableWidgetItem(product_data[1])
        item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
        self.table.setItem(self.table.rowCount() - 1, 1, item)

        item = QtWidgets.QTableWidgetItem(f"{float(product_data[2]):.2f}")
        item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
        self.table.setItem(self.table.rowCount() - 1, 2, item)

        self.table.setItem(self.table.rowCount() - 1, 3, QtWidgets.QTableWidgetItem("1"))

    def clear(self):
        self.table.clear()
        self.__init__(self.table, self.tree_data, self.labels)

    def calc_total(self):
        total = 0

        for row_idx in range(self.table.rowCount()):
            count = self.table.item(row_idx, 3)
            price = self.table.item(row_idx, 2)
            if count and price:
                try:
                    count = float(count.text())
                    price = float(price.text())
                except ValueError:
                    continue
                total += count * price

        return total

    def get_order_list(self):
        order_list = []
        for row_idx in range(self.table.rowCount()):
            product_id = self.table.item(row_idx, 0)
            count = self.table.item(row_idx, 3)
            if count and product_id:
                try:
                    count = int(count.text())
                    product_id = int(product_id.text())
                except ValueError:
                    continue

                order_list.append([product_id, count])

        return order_list
