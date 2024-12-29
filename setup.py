from cx_Freeze import setup, Executable
from pathlib import Path

src_path = Path("./src/manage_env")

build_options = {
    "includes": ["dialoguis"],
    "include_path": [str(src_path)],
    "excludes": ["tkinter"],
    "zip_include_packages": ["encodings", "PySide6", "shiboken6", "email", "urllib"],
    "bin_path_excludes": [""],
    "optimize": 1
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
