@echo off

:: Set these two paths as required!
:: If you have PYTHONPATH in your environment, you don't need to set a local path.
:: You can leave the script name the same unless you rename or move it.
:: You can also use this batch script to call other python scripts. 
SET LOCAL_PY_PATH=C:\Users\Jay\AppData\Local\Programs\Python\Python38-32\
SET SCRIPT_NAME=toggle.py

:: Don't edit these
IF "%PYTHONPATH%"=="" SET PYTHONPATH=%LOCAL_PY_PATH%
setlocal
cd /d %~dp0

%PYTHONPATH%python.exe %SCRIPT_NAME%