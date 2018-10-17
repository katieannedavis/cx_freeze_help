import sys
import os
from cx_Freeze import setup, Executable


# single files in the same folder can have just their names, to include everything in a folder give folder name
# cx_freeze will create a folder in the program of the same name
includefiles = ['example.py', 'example.ico', 'examples/', 'example.jpg']

# 'atexit' is required for PyQt5 programs
includes = ['atexit']

# don't package bulky packages that aren't needed
excludes = ['']

# If you don't include 'idna' cx_freeze will send an ImportError: cannot import name 'idnadata'
# Including PyQt5 in packages will send an ImportError: cannot find pyqt5.qt. It's there but it won't be found.
# cx-freeze auto detects PyQt5 files
packages = ['idna']

# Include when you don't want a console window to appear, delete this if you do
base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

# zip_include_packages helps to make program smaller, include_msvcr - include runtime DLLs
options = {
    'build_exe': {
        'includes': includes,
        'excludes': excludes,
        'packages': packages,
        'include_files': includefiles,
        'include_msvcr': True,
        'zip_include_packages': "."
    }
}

# targetName will change the name of the executable, it must be named with an .exe. Otherwise it will throw an error.
executables = [
    Executable('main.py', base=base,
               icon='icon.ico',
               shortcutName='example',
               targetName='example.exe')
]

# The solution to the cx_freeze: keyerror tcl library, hard code the location of tcl
os.environ['TCL_LIBRARY'] = r'C:\Users\katie\AppData\Local\Programs\Python\Python36\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\katie\AppData\Local\Programs\Python\Python36\tcl\tk8.6'

# author will appear on installation page, description will appear when user hovers over application
setup(name='Example',
      version='0.1',
      description='An example',
      author='Katie Davis',
      author_email='',
      executables=executables,
      options=options)


def find_data_file(filename):
    """
    Make sure that the installation uses files included
    :param filename:
    :return:
    """
    if getattr(sys, 'frozen', False):
        # The application is frozen
        datadir = os.path.dirname(sys.executable)
    else:
        # The application is not frozen
        # Change this bit to match where you store your data files:
        datadir = os.path.dirname(__file__)

    return os.path.join(datadir, filename)
