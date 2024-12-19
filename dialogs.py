from PySide6.QtWidgets import QWidget
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

    def btn_add_slot(self, *args, **kwargs):
        new_var = self.ui_btn_new_dialog.new_var_entry.text()
        new_values = self.ui_btn_new_dialog.new_values_entry.text()
        table_model = self._parent._parent.model
        table_model.setData(table_model.createIndex(0, 0), value=new_var, role=Qt.EditRole)
        self.close()
