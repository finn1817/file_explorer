@echo off
REM Liquid Glass File Explorer Launcher
REM This script launches the file explorer from the python directory

echo.
echo ========================================
echo   Liquid Glass File Explorer
echo ========================================
echo.
echo Starting application...
echo.

REM Ensure Python does not write .pyc files anywhere
set PYTHONDONTWRITEBYTECODE=1

cd python
REM Use -B as an extra safeguard to disable writing .pyc
python -B main.py

pause
