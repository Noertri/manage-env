from cx_Freeze import setup, Executable
from pathlib import Path

src_path = Path("./src/manage_env")

build_options = {
    "includes": [],
    "include_path": [str(src_path)],
    "excludes": [],
    "zip_include_packages": ["shiboken6", "tkinter", "encodings", "email", "urllib"],
    "bin_path_excludes": [],
    "optimize": 2
}

setup(
    name="manage-env",
    version="0.0.3",
    description="Simple GUI program to manage environment variables for linux",
    author="Tri Nur Syaifudin",
    author_email="trinuruns@gmail.com",
    options={"build_exe": build_options},
    executables=[Executable(script=str(src_path.joinpath("main.py")), base="gui", target_name="manage-env-bin")]
)
