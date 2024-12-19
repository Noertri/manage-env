from PySide6.QtWidgets import QWidget, QTableWidgetItem
from btn_new_dialog_ui import Ui_BtnNewDialog
from PySide6.QtCore import Qt


class BtnNewDialog(QWidget):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setFixedSize(500, 200)
        self.ui_btn_new_dialog = Ui_BtnNewDialog()
        self.ui_btn_new_dialog.setupUi(self)
        self._parent = parent

        self.ui_btn_new_dialog.btn_cancel.clicked.connect(lambda : self.close())
        self.ui_btn_new_dialog.btn_add.clicked.connect(self.btn_add_slot)

    def closeEvent(self, event):
        self._parent.btn_new_dialog = None
        print("Window is closed...")

    @property
    def new_variable(self):
        return self.ui_btn_new_dialog.new_var_entry.text()
    
    @property
    def new_values(self):
        return self.ui_btn_new_dialog.new_values_entry.text()

    def btn_add_slot(self, *args, **kwargs):
        print("Add new variable and values...")
        self._parent.table.insertRow(0)
        self._parent.table.setItem(0, 0, QTableWidgetItem(self.new_variable))
        self._parent.table.setItem(0, 1, QTableWidgetItem(self.new_values))
        try:
            self._parent.app_data["env_file"][self.new_variable] = self.new_values
            self._parent.app_data["new_confirm"] = True
        except (KeyError, Exception) as exception:
            print(exception)
        print("Done!")
        self.close()
