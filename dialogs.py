from typing import List
import copy

from PySide6.QtWidgets import QWidget, QTableWidgetItem, QFileDialog, QMessageBox, QListWidgetItem
from dialoguis.btn_new_dialog_ui import Ui_BtnNewDialog
from dialoguis.btn_edit_dialog_ui import Ui_BtnEditDialog
from PySide6.QtCore import Qt, QSize


class BtnNewDialog(QWidget):

    def __init__(self, parent, *args, **kwargs):
        from main import MainWidget

        super().__init__(*args, **kwargs)
        self.setFixedSize(500, 200)
        self.ui = Ui_BtnNewDialog()
        self.ui.setupUi(self)
        self._parent: MainWidget = parent

        self.ui.btn_cancel.clicked.connect(self.btn_cancel_slot)
        self.ui.btn_add.clicked.connect(self.btn_add_slot)
        self.ui.btn_browse_dir.clicked.connect(self.btn_browse_dir_slot)
        self.ui.btn_browse_file.clicked.connect(self.btn_browse_file_slot)

    def closeEvent(self, event):
        self._parent.btn_new_dialog = None
        print("Button New dialog is closed...")

    @property
    def new_variable(self):
        return self.ui.new_var_entry.text()
    
    @property
    def new_values(self):
        return self.ui.new_values_entry.text()

    @new_values.setter
    def new_values(self, values: str):
        self.ui.new_values_entry.insert(values)

    def btn_cancel_slot(self):
        print("Task is canceled!")
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
                
                self._parent.update_env_file(self.new_variable, self.new_values)
                self._parent.set_app_data("new_btn_confirm", True)

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
            self.new_values = ":".join(file_names)


class ListWidgetItem(QListWidgetItem):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setSizeHint(QSize(400, 25))
        

class BtnEditDialog(QWidget):

    def __init__(self, parent, *args, **kwargs):
        from main import MainWidget

        super().__init__(*args, **kwargs)
        self.setFixedSize(650, 500)
        self.ui = Ui_BtnEditDialog()
        self.ui.setupUi(self)
        self._parent: MainWidget = parent
        
        self._selected_values = []
        self._row = 0
        self._selected_items: List[QTableWidgetItem] = self._parent.table.selectedItems()
        
        self._load_selected_items()

        # cancel button
        self.ui.btn_cancel2.clicked.connect(self.btn_cancel_slot)

        # ok button
        self.ui.btn_ok2.clicked.connect(self.btn_ok_slot)

        # new button
        self.ui.btn_new2.clicked.connect(self.btn_new_slot)

        # edit button
        self.ui.btn_edit2.clicked.connect(self.btn_edit_slot)

        # delete button
        self.ui.btn_delete2.clicked.connect(self.btn_delete_slot)

    @property
    def values_list(self):
        return self.ui.values_list

    def _load_selected_items(self):
        self.ui.var_entry.insert(self._selected_items[0].text())
        self._row = self._selected_items[0].row()

        for t in self._selected_items[1].text().split(":"):
            self._selected_values.append(t)
            item = ListWidgetItem()
            item.setFlags(item.flags()|Qt.ItemFlag.ItemIsSelectable)
            item.setText(t)
            self.values_list.addItem(item)

    def closeEvent(self, event):
        self._parent.btn_edit_dialog = None
        print("Button Edit dialog is closed...")

    def btn_cancel_slot(self):
        print("Task is canceled...")
        self.close()

    def btn_ok_slot(self):
        new_var = self.ui.var_entry.text()
        new_values = []

        for i in range(self.values_list.count()):
            if t := self.values_list.item(i).text().strip():
                new_values.append(t)

        # update table
        self._parent.table.setItem(self._row, 0, QTableWidgetItem(new_var))
        self._parent.table.setItem(self._row, 1, QTableWidgetItem(":".join(new_values)))

        _new_values = ""

        if len(new_values) > len(self._selected_values):
            diff_values = list(set(new_values)-set(self._selected_values))
            if diff_values and new_var in self._parent.app_configs["defaults"]:
                _new_values = "{0}:${1}".format(":".join(diff_values), new_var)
            elif diff_values and new_var not in self._parent.app_configs["defaults"]:
                _new_values = ":".join(new_values)
        
        if len(new_values) <= len(self._selected_values) and new_var not in self._parent.app_configs["defaults"]:
            _new_values = ":".join(new_values)

        if new_var and _new_values:
            self._parent.update_env_file(new_var, _new_values)
            self._parent.set_app_data("edit_btn_confirm", True)

        self.close()
        
    def btn_new_slot(self):
        new_item = ListWidgetItem()
        new_item.setText("New value")
        new_item.setFlags(Qt.ItemFlag.ItemIsEditable|new_item.flags())
        
        self.values_list.addItem(new_item)
        self.values_list.setCurrentItem(new_item)
        self.values_list.editItem(self.values_list.currentItem())

    def btn_edit_slot(self):
        current_item = self.values_list.currentItem()
        current_item.setFlags(current_item.flags()|Qt.ItemFlag.ItemIsEditable)
        self.values_list.editItem(current_item)
    
    def btn_delete_slot(self):
        current_row = self.values_list.currentRow()
        self.values_list.takeItem(current_row)

    def btn_browse_dir_slot(self):
        pass

    def btn_browse_file_slot(self):
        pass
