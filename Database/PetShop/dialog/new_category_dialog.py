# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog/new_category_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NewCategory(object):
    def setupUi(self, NewCategory):
        NewCategory.setObjectName("NewCategory")
        NewCategory.resize(433, 157)
        self.buttonBox = QtWidgets.QDialogButtonBox(NewCategory)
        self.buttonBox.setGeometry(QtCore.QRect(190, 100, 211, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.category_name = QtWidgets.QLineEdit(NewCategory)
        self.category_name.setGeometry(QtCore.QRect(30, 40, 371, 31))
        self.category_name.setObjectName("category_name")

        self.retranslateUi(NewCategory)
        self.buttonBox.accepted.connect(NewCategory.accept) # type: ignore
        self.buttonBox.rejected.connect(NewCategory.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(NewCategory)

    def retranslateUi(self, NewCategory):
        _translate = QtCore.QCoreApplication.translate
        NewCategory.setWindowTitle(_translate("NewCategory", "Новая категория"))
        self.category_name.setPlaceholderText(_translate("NewCategory", "Название"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NewCategory = QtWidgets.QDialog()
    ui = Ui_NewCategory()
    ui.setupUi(NewCategory)
    NewCategory.show()
    sys.exit(app.exec_())
