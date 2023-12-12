# PythonPackageInstaller
A Python script used for automating the installation of pip packages. 

## Prerequisites
- Python 3.x
- Pip 

## Usage
- Download `packageInstall.py`.
- Place a `requirements.txt` file in the same directory.
- Run `python ./packageInstall.py` (use --help for list of arguments)
- Refer to `errors.txt` for list of packages which may not have installed correctly.

## Generating a Requirements File
If packages are being ported over from an existing environment, the package name and versions can be placed into a requirements.txt file with the following steps:
1. Verify Python is Installed
```
python --version
```
2. Generate Requirements file
```
pip freeze > requirements.txt
```

This file can then be used as the input for `packageInstall.py`. 
