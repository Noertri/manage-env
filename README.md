# manage-env

Simple GUI program to manage environment variables for linux.

## Installation
Download program from [here](https://github.com/Noertri/manage-env/releases), then extract the archive to your desired folder or extract it to ```$HOME/.local/bin``` or ```$HOME/bin``` depend on your distro, so you can invoke the program directly from terminal.

Append this code below to ```.bashrc``` and ```.profile``` file,

```bash
if [ -f ~/.environment ]; then
	set -a
	source ~/.environment
	set +a
fi
```
then try to logout and login your system. Tested in debian 12 bookworm.

### Build from source
Download the source code from this repo, then extract it. This program is built using python and PyQt5 (Qt5).

Requirements:

1. Python (>= 3.11.10)
2. PyQt5/PyQt6/PySide6 (latest)
3. cx-freeze (latest)
4. make (to automate the convertion of ui files to py files and build executable, use package provided by your distro)

Create virtual environment, activate it, then change directory to extracted source code folder and run command below to install all requirements.

```bash
pip3 install -r requirements.txt
```

To convert .ui files to .py files, go to extracted source code folder then run,

```bash
make all
```

To build, run,

```bash
make build
```

or

```bash
python3 setup.py build
```

Optionally run,

```bash
make clean
```

this command will delete unnecessary files in folder build. You can also use PyQt6/PySide6 but you need to change some configurations.
