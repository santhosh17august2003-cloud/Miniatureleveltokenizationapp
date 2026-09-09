@echo off
title Build Standalone Executable (.exe)
cd /d "%~dp0"

echo ==========================================================
echo  Miniature NLP Tokenization App - Standalone EXE Builder
echo ==========================================================
echo.
echo NOTE: Creating a shortcut (run create_desktop_shortcut.bat)
echo is the fastest way to run as a desktop app immediately.
echo.
echo If you want to bundle this into an independent .exe file:
echo 1. Installing PyInstaller...
pip install pyinstaller

echo 2. Packaging with PyInstaller...
pyinstaller --noconfirm --onedir --windowed --icon="assets\app_icon.ico" --add-data="assets;assets" --add-data=".runtime-home;.runtime-home" --name="MiniatureTokenizationApp" main.py

echo.
echo Build complete! The executable is located in the "dist\MiniatureTokenizationApp" folder.
echo.
pause
