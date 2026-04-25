@echo off
chcp 65001 >nul
title 证件照处理工具 - Windows打包工具

echo ============================================
echo   证件照处理工具 - Windows 打包脚本
echo ============================================
echo.

:: 检查 Python 是否安装
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [错误] 未检测到 Python，请先安装 Python 3.8+
    echo 下载地址: https://www.python.org/downloads/
    echo 安装时请勾选 "Add Python to PATH"
    pause
    exit /b 1
)

echo [1/3] 检测到 Python 环境
python --version

:: 安装依赖
echo.
echo [2/3] 正在安装依赖...
pip install Pillow pyinstaller -q
if %errorlevel% neq 0 (
    echo [错误] 依赖安装失败
    pause
    exit /b 1
)
echo 依赖安装完成

:: 打包 exe
echo.
echo [3/3] 正在打包为 exe...
pyinstaller --onefile --name "证件照处理工具" --windowed --add-data "process_photo.py;." process_photo.py
if %errorlevel% neq 0 (
    echo [错误] 打包失败
    pause
    exit /b 1
)

echo.
echo ============================================
echo   ✅ 打包成功！
echo ============================================
echo.
echo 可执行文件位置: dist\证件照处理工具.exe
echo.
echo 使用方法：
echo   1. 直接双击运行，选择图片文件
echo   2. 或将图片拖放到 exe 图标上
echo.
pause
