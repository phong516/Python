import sys
from cx_Freeze import setup, Executable

# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = "Bai2",
    version = "4.0",
    description = "WriteTable",
    executables = [Executable('btth2.py', base=base)]
)