VPATH = ./src/manage_env

target_path = ./src/manage_env

vpath %.ui ./src/manage_env/ui_files/

.PHONY: all build

all: main_ui edit_dialog_ui new_dialog_ui

main_ui : main_form.ui
	pyside6-uic $^ --rc-prefix -o $(target_path)/$@.py

edit_dialog_ui : edit_dialog_form.ui
	pyside6-uic $^ --rc-prefix -o $(target_path)/$@.py

new_dialog_ui : new_dialog_form.ui
	pyside6-uic $^ --rc-prefix -o $(target_path)/$@.py

build: setup.py
	python3 setup.py build
