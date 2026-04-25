@echo off
title ID Photo Tool - Windows Builder

echo ============================================
echo   ID Photo Tool - Windows Build Script
echo ============================================
echo.

:: Check Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python not found! Please install Python 3.8+
    echo Download: https://www.python.org/downloads/
    echo Remember to check "Add Python to PATH"
    pause
    exit /b 1
)

echo [1/3] Python detected
python --version

:: Install dependencies
echo.
echo [2/3] Installing dependencies...
pip install Pillow pyinstaller -q
if %errorlevel% neq 0 (
    echo [ERROR] Dependency installation failed
    pause
    exit /b 1
)
echo Dependencies installed

:: Build exe
echo.
echo [3/3] Building exe...
pyinstaller --onefile --name "ID_Photo_Tool" --windowed process_photo.py
if %errorlevel% neq 0 (
    echo [ERROR] Build failed
    pause
    exit /b 1
)

echo.
echo ============================================
echo   Build Success!
echo ============================================
echo.
echo Output: dist\ID_Photo_Tool.exe
echo.
echo Usage:
echo   1. Double-click to run, select a photo
echo   2. Or drag & drop photo onto the exe
echo.
pause
