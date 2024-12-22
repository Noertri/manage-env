#!/bin/bash


echo "Build form.ui"
pyside6-uic ui_files/form.ui --rc-prefix -o dialoguis/main_ui.py
echo "Build btn_new_dialog.ui"
pyside6-uic ui_files/btn_new_dialog.ui --rc-prefix -o dialoguis/btn_new_dialog_ui.py
echo "Build btn_edit_dialog.ui"
pyside6-uic ui_files/btn_edit_dialog.ui --rc-prefix -o dialoguis/btn_edit_dialog_ui.py
echo "Done!!!"
