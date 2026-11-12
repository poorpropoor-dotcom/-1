@echo off
setlocal
cd /d "%~dp0"

set "PYTHON="
if exist ".venv\Scripts\python.exe" set "PYTHON=%~dp0.venv\Scripts\python.exe"
if not defined PYTHON (
    where py >nul 2>nul
    if not errorlevel 1 (
        set "PYTHON=py -3"
    ) else (
        where python >nul 2>nul
        if not errorlevel 1 set "PYTHON=python"
    )
)

if not defined PYTHON (
    echo Python was not found. Install Python 3 and enable "Add Python to PATH".
    pause
    exit /b 1
)

echo Checking Python dependencies...
%PYTHON% -m pip install -r requirements.txt
if errorlevel 1 (
    echo Dependency installation failed.
    pause
    exit /b 1
)

echo Starting the portfolio server...
%PYTHON% backend\app.py
if errorlevel 1 (
    echo The portfolio server stopped with an error.
    pause
    exit /b 1
)

endlocal
