VPATH = ./src/manage_env

target_path = ./src/manage_env

vpath %.ui ./src/manage_env/ui_files/

.PHONY: all build clean

all: main_ui edit_dialog_ui new_dialog_ui

main_ui : main_form.ui
	pyuic5 $^ -o $(target_path)/$@.py

edit_dialog_ui : edit_dialog_form.ui
	pyuic5 $^ -o $(target_path)/$@.py

new_dialog_ui : new_dialog_form.ui
	pyuic5 $^ -o $(target_path)/$@.py

build: setup.py
	python3 setup.py build

clean:
	if [ -d build ]; then \
		cd build/exe.linux*/lib/; \
		rm -f _blake2*; \
		rm -f _codecs*; \
		rm -f _csv*; \
		rm -f _datetime*; \
		rm -f libcrypto*; \
		rm -f _socket*; \
		rm -f _pickle*; \
		rm -f _posixsubprocess*; \
		rm -f array*; \
		rm -f unicodedata*; \
		rm -f _decimal*; \
		rm -f PySide6/*Network*; \
		rm -f PySide6/Qt/lib/*Network*; \
		rm -f PySide6/Qt/lib/*Qml*; \
		rm -f PySide6/Qt/lib/*OpenGL*; \
		rm -f PySide6/Qt/lib/*Quick*; \
		rm -f PySide6/Qt/lib/*Egl*; \
		rm -rf PySide6/Qt/translations; \
		rm -rf PySide6/Qt/plugins/egldeviceintegrations; \
		rm -rf PySide6/Qt/plugins/networkinformation; \
		rm -rf PySide6/Qt/plugins/tls; \
		rm -rf PySide6/Qt/plugins/imageformats; \
	fi
