#!/bin/bash

echo "Build form.ui"
pyside6-uic ui_files/form.ui --rc-prefix -o main_ui.py
echo "Build btn_new_dialog.ui"
pyside6-uic ui_files/btn_new_dialog.ui --rc-prefix -o btn_new_dialog_ui.py
echo "Done!!!"
