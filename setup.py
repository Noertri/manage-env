from cx_Freeze import setup, Executable
from pathlib import Path
import json

src_path = Path("./src/manage_env")

if (opts_path := Path("build_options.json")) and opts_path.exists():
    with opts_path.open("r", encoding="utf-8") as fobj:
        build_options = json.load(fobj)
        fobj.close()
        
setup(
    name="manage-env",
    version="0.0.3",
    description="Simple GUI program to manage environment variables for linux",
    author="Tri Nur Syaifudin",
    author_email="trinuruns@gmail.com",
    options={"build_exe": build_options},
    executables=[Executable(script=str(src_path.joinpath("main.py")), base="gui", target_name="manage-env-bin")]
)
