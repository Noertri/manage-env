VPATH = src/manage_env

target_path = src/manage_env

vpath %.ui src/manage_env/ui_files/

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
	if [ -d build ]; then mv -uv build/exe.linux* build/manage-env; fi

clean:
	if [ -d build/manage-env/lib ]; then \
		cd build/manage-env/lib/; \
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
		rm -f *sha*; \
		rm -f *hashlib*; \
		rm -f *math*; \
		rm -f *random*; \
		rm -f *binascii*; \
		rm -f *select*; \
		rm -f *multibytecodec*; \
		rm -f *statistics*; \
		rm -f *md5*; \
		rm -f *heapq*; \
		rm -f *struct*; \
		rm -f *fcntl*; \
		rm -f *bisect*; \
		rm -f *grp*; \
		rm -f *opcode*; \
		rm -f *lzma*; \
		rm -f *bz2*; \
		rm -f _json*; \
		rm -f *typing*; \
		rm -f *context*; \
		rm -rf email; \
		rm -f PyQt5/*Network*; \
		rm -f PyQt5/Qt5/lib/*Network*; \
		rm -f PyQt5/Qt5/lib/*WebSocket*; \
		rm -f PyQt5/Qt5/lib/*Qml*; \
		rm -f PyQt5/Qt5/lib/*OpenGL*; \
		rm -f PyQt5/Qt5/lib/*Quick*; \
		rm -f PyQt5/Qt5/lib/*Egl*; \
		rm -rf PyQt5/Qt5/translations; \
		rm -f PyQt5/Qt5/plugins/imageformats/*pdf*; \
		rm -f PyQt5/Qt5/plugins/imageformats/*gif*; \
		rm -f PyQt5/Qt5/plugins/imageformats/*tga*; \
		rm -f PyQt5/Qt5/plugins/imageformats/*tiff*; \
		rm -f PyQt5/Qt5/plugins/imageformats/*bmp*; \
		rm -f PyQt5/Qt5/plugins/imageformats/*webp*; \
	fi
