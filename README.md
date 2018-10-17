# cx_freeze_help
The items and information needed to make cx_freeze build an application from python 3 code.
My system:
* Python3.6
* Windows 10
* cx-freeze: 5.1.1 

## Steps for building a distributable product
Most of this is summary of the documentation for cx_freeze
https://cx-freeze.readthedocs.io/en/latest/distutils.html

1. Install cx_freeze
* In command prompt install cx_freeze: python -m pip install cx_Freeze

2. Copy setup.py into the project folder, and fill it out
* Make sure to include all the data files (such as pictures and other .py files that aren't modules)

3. Choose what how you want to package your product
### Steps for packaging
1. Go to the project location in the command prompt
* The options are a build folder that includes an .exe file, which is good for debugging
--- Type: python setup.py build
* Create an installer
--- Type: python setup.py bdist_msi
