# This Python file uses the following encoding: utf-8
import json
import re
import sys
import os
from pathlib import Path

from PySide6.QtWidgets import QApplication, QWidget, QHeaderView, QTableWidgetItem
from PySide6.QtCore import Qt

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py

from dialoguis.main_ui import Ui_MainWindow
from dialogs import BtnNewDialog, BtnEditDialog

  
class MainWidget(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # initialization
        self.init_app()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(600, 500)

        self.btn_new_dialog: BtnNewDialog = None
        self.btn_edit_dialog: BtnEditDialog = None

        # customize table header
        table_hor_header = self.ui.table.horizontalHeader()
        table_hor_header.setSectionResizeMode(QHeaderView.ResizeMode.Fixed)
        table_hor_header.setSectionsClickable(False)

        self._load_env_vars()

        # close button
        self.ui.btn_close.clicked.connect(self.btn_close_slot)

        # new button
        self.ui.btn_new.clicked.connect(self.btn_new_slot)

        # edit button
        self.ui.btn_edit.clicked.connect(self.btn_edit_slot)

        # ok button
        self.ui.btn_ok.clicked.connect(self.btn_ok_slot)

    @property
    def table(self):
        return self.ui.table

    def init_app(self):
        self.app_workdir = Path.cwd()
        self.app_configs = {
                    "commons": [
                        "HOME",
                        "PATH",
                        "PWD",
                        "USER",
                        "SHELL",
                        "UID",
                        "HOSTNAME",
                        "LANG",
                        "MAIL",
                        "EDITOR",
                        "TEMP",
                        "PS1"
                    ],
                    "excludes": [
                        ".*CURRENT_DESKTOP",
                        ".*RUNTIME.*",
                        ".*SESSION.*",
                        ".*MENU_PREFIX",
                        "PYSIDE.*",
                        "GIO.*",
                        "GDM_LANG",
                        "WINDOWPATH",
                        "QT.*",
                        "LC.*",
                        "KDE.*",
                        "GTK.*",
                        "PAM.*",
                        "^_.*",
                        "SESSION_MANAGER",
                        ".*TERM.*",
                        "SSH_AUTH_SOCK", 
                        "XMODIFIERS", 
                        "DESKTOP_SESSION",
                        "SSH_AGENT_PID", 
                        "XCURSOR_SIZE",
                        "GPG_AGENT_INFO", 
                        "SYSTEMD_EXEC_PID", 
                        "XAUTHORITY", 
                        "VSCODE_GIT_ASKPASS_NODE", 
                        "IM_CONFIG_PHASE",
                        "LS_COLORS", 
                        "VIRTUAL_ENV", 
                        "GIT_ASKPASS",
                        "INVOCATION_ID", 
                        "MANAGERPID", 
                        "CHROME_DESKTOP", 
                        "CLUTTER_IM_MODULE", 
                        "VSCODE_GIT_ASKPASS_EXTRA_ARGS", 
                        "LESS.*",
                        "VSCODE_GIT_IPC_HANDLE",
                        "DISPLAY",
                        "SHLVL", 
                        "VIRTUAL_ENV_PROMPT",
                        "VSCODE_GIT_ASKPASS_MAIN",
                        "JOURNAL_STREAM", 
                        "XCURSOR_THEME", 
                        "GDK_BACKEND",
                        ".*BUS.*",
                        ".*DEBUG.*",
                        ".*ENCODING.*",
                        ".*BUFFERED.*",
                        "PYDEVD.*",
                        "LD.*",
                        "TK.*",
                        "TCL.*"
                    ]
                }
        
        self.env_file_path = Path("{0}/.environment".format(Path.home()))
        self.app_data = dict()

        # if not self.app_workdir.exists():
        #     self.app_workdir.mkdir(parents=True)

        if not self.app_workdir.joinpath("config.json").exists():
            self._create_configs(self.app_workdir.joinpath("config.json"))
        else:
            self._load_configs(self.app_workdir.joinpath("config.json"))

        bashrc_path = Path("{0}/.bashrc".format(Path.home()))
        dotfile_path = Path("{0}/.profile".format(Path.home()))
        
        script = 'if [ -f ~/.environment ]; then\n\tset -a\n\tsource ~/.environment\n\tset +a\nfi'

        if not self.env_file_path.exists():
            self.env_file_path.touch()

            # with bashrc_path.open("a", encoding="utf-8") as f:
            #     f.write("\n"+script.strip()+"\n")
            #     f.close()

            # with dotfile_path.open("a", encoding="utf-8") as f:
            #     f.write("\n"+script.strip()+"\n")
            #     f.close()

        env_os = dict(os.environ)
        env_os = dict(filter(self._filter_vars, env_os.items()))
        env_os.update(self.load_env_file())

        self.app_data = {
            "env_file": self.load_env_file(),
            "env_os": dict(sorted(env_os.items(), key=lambda x: x[0]))
        }

    def _load_env_vars(self):
        env_vars = list(self.app_data.get("env_os", {}).items())
        self.table.setRowCount(len(env_vars))

        for i in range(self.ui.table.rowCount()):
            var_item = QTableWidgetItem(env_vars[i][0])
            values_item = QTableWidgetItem(env_vars[i][1])
            self.ui.table.setItem(i, 0, var_item)
            self.ui.table.setItem(i, 1, values_item)

    def _create_configs(self, config_path: Path):
        with config_path.open("w", encoding="utf-8") as iobj:
            json.dump(self.app_configs, iobj)
            iobj.close()

    def _load_configs(self, config_path: Path):
        with config_path.open("r", encoding="utf-8") as iobj:
            self.app_configs = json.load(iobj)
            iobj.close()

    def _filter_vars(self, x):
        exclude_patterns = re.compile(r"|".join(self.app_configs["excludes"]))

        if x in self.app_configs["commons"]:
            return True
        elif exclude_patterns.match(x[0]):
            return False
        else:
            return x

    def load_env_file(self):
        pattern = re.compile(r'([_A-Za-z0-9]+?)="(.*)"|([_A-Za-z0-9]+?)=(.*)')

        env = dict()

        if self.env_file_path.exists():
            with self.env_file_path.open("r", encoding="utf-8") as f:
                for line in f.readlines():
                    if line.startswith("#"):
                        continue
                    matched = pattern.search(line.strip())
                    env[matched.group(1).strip()] = matched.group(2).strip()
                f.close()

        return env

    def _save_to_file(self):
        with self.env_file_path.open("w", encoding="utf-8") as f:
            if self.app_data.get("env_file", None):
                for k, v in self.app_data["env_file"].items():
                    f.write(f'{k}="{v}"\n')

            f.close()

    def closeEvent(self, event):
        if self.btn_new_dialog or self.btn_edit_dialog:
            event.ignore()
        else:
            event.accept()
            print("Quit!!!")

    def btn_new_slot(self):
        if not self.btn_new_dialog and not self.btn_edit_dialog:
            self.btn_new_dialog = BtnNewDialog(parent=self)
            self.btn_new_dialog.show()

    def btn_edit_slot(self):
        if not self.btn_edit_dialog and not self.btn_new_dialog and self.table.selectedItems():
            self.btn_edit_dialog = BtnEditDialog(parent=self)
            self.btn_edit_dialog.show()

    def btn_ok_slot(self):
        print("Write data to file...")
        if self.app_data.get("new_confirm", False):
            self._save_to_file()

        print("Done!")

    def btn_close_slot(self):
        self.close()

   
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWidget()
    widget.show()
    sys.exit(app.exec())
