import os
import sys

from cx_Freeze import setup, Executable

PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')


basic = None
if (sys.platform == "win32"):
    basic = "Win32GUI"    # Tells the build script to hide the console.

executables = [Executable("picture_classifier.py", base=basic)]

packages = ["idna"]
options = {
    'build_exe': {
    	'include_files':[
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),
        ],
        'packages':packages,
    },    
}

setup(
    name = "picture_classifier",
    options = options,
    version = "1.0.0",
    author = "miterv",
    description = 'picture_classifier.py',
    executables = executables
)