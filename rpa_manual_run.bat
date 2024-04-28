@echo off
chcp 65001
setlocal enabledelayedexpansion

set "srcDir=%~dp0"
pushd "!srcDir!"

set /p "count=Enter the number of variables: "
set "args="

for /l %%i in (1, 1, %count%) do (
    set /p "arg=Enter variable %%i: "
    set "args=!args! !arg!"
)

python "./src/rpa.py" %args%

endlocal
pause