from PySide6.QtWidgets import QWidget
from btn_new_dialog_ui import Ui_BtnNewDialog


class BtnNewDialog(QWidget):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setFixedSize(500, 200)
        self.ui_btn_new_dialog = Ui_BtnNewDialog()
        self.ui_btn_new_dialog.setupUi(self)
        self._parent = parent

    def closeEvent(self, event):
        self._parent.btn_new_win_widget = None
        print("Window is closed...")
