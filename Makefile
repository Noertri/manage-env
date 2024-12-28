VPATH = ./src/manage_env/dialoguis:./src/manage_env/ui_files

target_path = ./src/manage_env/dialoguis

vpath %.ui ./src/manage_env/ui_files/


.PHONY: build

main_ui : main_form.ui
	pyside6-uic $^ --rc-prefix -o $(target_path)/$@.py

btn_edit_dialog_ui : btn_edit_dialog_form.ui
	pyside6-uic $^ --rc-prefix -o $(target_path)/$@.py

btn_new_dialog_ui : btn_new_dialog_form.ui
	pyside6-uic $^ --rc-prefix -o $(target_path)/$@.py
