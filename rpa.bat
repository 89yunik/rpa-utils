@echo off
chcp 65001
setlocal enabledelayedexpansion

set "srcDir=%~dp0"
pushd "!srcDir!"
python "./src/rpa.py"

endlocal