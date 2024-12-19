from PySide6.QtWidgets import QWidget
from btn_new_dialog_ui import Ui_BtnNewDialog


class BtnNewDialog(QWidget):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setFixedSize(500, 200)
        self.btn_new_window_ui = Ui_BtnNewDialog()
        self.btn_new_window_ui.setupUi(self)
        self._parent = parent

    def closeEvent(self, event):
        self._parent.btn_new_win_widget = None
        print("Window is closed...")
