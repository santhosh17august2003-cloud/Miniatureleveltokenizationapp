@echo off
title Create Desktop Shortcut
cd /d "%~dp0"

echo Creating Desktop Shortcut with Icon...
powershell -ExecutionPolicy Bypass -File "%~dp0create_shortcut.ps1"

echo.
echo ========================================================
echo  Shortcut created successfully on your Windows Desktop!
echo ========================================================
echo.
pause
