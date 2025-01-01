# manage-env

Simple GUI program to manage environment variables in linux.

## Installation
Download program from [release page](https://github.com/Noertri/manage-env/releases), then extract the archive to your desired folder. Create symlink of **manage-env-bin** to `$HOME/.local/bin` or `$HOME/bin` depending on your distro, so you can invoke the program directly from terminal.

Append this code below to ```.bashrc``` and ```.profile``` file,

```bash
if [ -f ~/.environment ]; then
	set -a
	source ~/.environment
	set +a
fi
```
then try to logout and login your system. The program has been tested in debian 12 bookworm.

### Build from source

#### Requirements:

1. Python (>= 3.11.10)
2. PyQt5/PyQt6/PySide6 (latest)
3. cx-freeze (latest)
4. make (to automate the convertion of ui files to py files and build executable)

#### Build steps

1. Download the source code from [release page](https://github.com/Noertri/manage-env/releases) then extract it, or clone this repo

	```bash
	git clone git@github.com:Noertri/manage-env.git
	```

2. Create virtual environment and activate it

	```bash
	python3 -m venv path/to/yourenv
	source path/to/yourenv/bin/activate
	```

3. Change directory to source code folder and run command below to install all requirements

	```bash
	pip3 install -r requirements.txt
	```

4. Convert .ui files to .py files, run

	```bash
	make all
	```

5. Build the program, run

	```bash
	make build
	```
	
	or
	
	```bash
	python3 setup.py build
	```

6. Optionally run this command

	```bash
	make clean
	```

	this command will delete unnecessary files/library files in folder build to reduze the size. 

You can also use PyQt6/PySide6 but you need to change some changes of the **Makefile**.
