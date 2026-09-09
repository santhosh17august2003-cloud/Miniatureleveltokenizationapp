@echo off
title Miniature Tokenization App Launcher
cd /d "%~dp0"

echo Launching Miniature NLP Tokenization Desktop App...

:: Check if pythonw is available to run without console
where pythonw >nul 2>nul
if %errorlevel% equ 0 (
    start "" pythonw main.py
    exit /b
)

:: Fallback to standard python
where python >nul 2>nul
if %errorlevel% equ 0 (
    start "" python main.py
    exit /b
)

echo ERROR: Python is not found in PATH!
pause
