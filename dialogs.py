from PySide6.QtWidgets import QWidget, QTableWidgetItem, QFileDialog, QMessageBox
from btn_new_dialog_ui import Ui_BtnNewDialog
from PySide6.QtCore import Qt


class BtnNewDialog(QWidget):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setFixedSize(500, 200)
        self.ui_btn_new_dialog = Ui_BtnNewDialog()
        self.ui_btn_new_dialog.setupUi(self)
        self._parent = parent

        self.ui_btn_new_dialog.btn_cancel.clicked.connect(self.btn_cancel_slot)
        self.ui_btn_new_dialog.btn_add.clicked.connect(self.btn_add_slot)
        self.ui_btn_new_dialog.btn_browse_dir.clicked.connect(self.btn_browse_dir_slot)
        self.ui_btn_new_dialog.btn_browse_file.clicked.connect(self.btn_browse_file_slot)

    def closeEvent(self, event):
        self._parent.btn_new_dialog = None
        print("Window is closed...")

    @property
    def new_variable(self):
        return self.ui_btn_new_dialog.new_var_entry.text()
    
    @property
    def new_values(self):
        return self.ui_btn_new_dialog.new_values_entry.text()

    @new_values.setter
    def new_values(self, values: str):
        self.ui_btn_new_dialog.new_values_entry.insert(values)

    def btn_cancel_slot(self):
        print("Add new variable is canceled!")
        self.close()

    def btn_add_slot(self):
        print("Add new variable and values...")
        if self.new_variable and self.new_values:
            idx = 0
            for i in range(self._parent.table.rowCount()):
                if self.new_variable == self._parent.table.item(i, 0).text():
                    idx += 1
                    break

            if idx == 0:
                self._parent.table.insertRow(idx)
                self._parent.table.setItem(idx, 0, QTableWidgetItem(self.new_variable))
                self._parent.table.setItem(idx, 1, QTableWidgetItem(self.new_values))
                try:
                    self._parent.app_data["env_file"][self.new_variable] = self.new_values
                    self._parent.app_data["new_confirm"] = True
                except (KeyError, Exception) as exception:
                    print(exception)
            else:
                QMessageBox()
        print("Done!")
        self.close()

    def btn_browse_dir_slot(self):
        file_dialog = QFileDialog()
        dir_name = file_dialog.getExistingDirectory()

        if dir_name:
            self.new_values = dir_name
    
    def btn_browse_file_slot(self):
        file_dialog = QFileDialog()
        file_names, _ = file_dialog.getOpenFileNames()

        if file_names:
            self.new_values = ";".join(file_names)
