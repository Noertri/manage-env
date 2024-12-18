# This Python file uses the following encoding: utf-8
import sys
import os

from PySide6.QtWidgets import QApplication, QWidget, QHeaderView
from PySide6.QtCore import Qt
from PySide6 import QtCore

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py

from main_ui import Ui_MainWindow


class TableModel(QtCore.QAbstractTableModel):

    def __init__(self, data, parent = None):
        super().__init__(parent)
        self._data = data or []

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]
        
    def rowCount(self, parent = None):
        return len(self._data)
    
    def columnCount(self, parent = None):
        return 2


class MainWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.model = TableModel(list(os.environ.items()))
        self.ui.table.setModel(self.model)
        self.ui.btn_close.clicked.connect(lambda : self.close())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWidget()
    widget.show()
    sys.exit(app.exec())
