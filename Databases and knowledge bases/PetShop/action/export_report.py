import csv
from openpyxl import Workbook

from PyQt5 import QtWidgets

from dbcore import core
from dialog import export_report_dialog


class ExportReportDlg(export_report_dialog.Ui_ExportReport):
    def __init__(self, dlg: QtWidgets.QDialog, db: core.Database):
        super().__init__()

        self.dlg = dlg
        self.db = db

        self.setupUi(dlg)

        self.get_path_file.clicked.connect(self.handler_get_path_file)

        self.buttonBox.accepted.disconnect()
        self.buttonBox.accepted.connect(self.accept_handler)

    def handler_get_path_file(self):
        f_name = QtWidgets.QFileDialog.getSaveFileName(self.dlg, 'Сохранение отчета', '')

        if not f_name or not f_name[0]:
            return

        self.path_file.setText(f_name[0])

    def accept_handler(self):
        if not self.path_file.text():
            self.path_file.setPlaceholderText("Не указан путь сохранения")
            return

        path_file = self.path_file.text()

        if self.is_csv.isChecked() and not path_file.endswith(".csv"):
            path_file = f"{path_file}.csv"

        if self.is_xls.isChecked() and not path_file.endswith(".xlsx"):
            path_file = f"{path_file}.xlsx"

        if self.is_sales.isChecked():
            self.save_report_sales(path_file, self.is_csv.isChecked())

        self.dlg.accept()

    def save_report_sales(self, path_file: str, is_csv=True):
        data = self.db.get_report_data()

        try:
            if is_csv:
                with open(f"{path_file}", "w") as f:
                    if self.is_csv:
                        writer = csv.writer(f)
                        for row in data:
                            writer.writerow(row)
            else:
                wb = Workbook()
                ws = wb.active
                for row in data:
                    print(row)
                    ws.append(row)
                wb.save(path_file)

            QtWidgets.QMessageBox.about(self.dlg, "Успех", f"Отчет сохранен\n{path_file}")
        except:
            QtWidgets.QMessageBox.about(self.dlg, "Ошибка", "Не удалось сохранить отчет")