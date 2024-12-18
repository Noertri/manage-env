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
    
    def headerData(self, section, orientation, role):
        if section == 0 and orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return "Variable"
        elif section == 1 and orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return "Values"


class UiMainWindow(Ui_MainWindow):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(parent)
        self._parent = parent

        # customize table header
        table_h_header = self.table.horizontalHeader()
        table_h_header.setSectionResizeMode(QHeaderView.ResizeMode.Fixed)
        table_h_header.setSectionsClickable(False)

        # close button
        self.btn_close.clicked.connect(lambda : self._parent.close())


class MainWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.main_ui = UiMainWindow(self)

        # load model
        os_vars = list(sorted(os.environ.items(), key=lambda x: x[0]))
        self.model = TableModel(os_vars)
        self.main_ui.table.setModel(self.model)

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWidget()
    widget.show()
    sys.exit(app.exec())
