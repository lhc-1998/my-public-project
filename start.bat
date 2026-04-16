@echo off
title 在线考试系统
cd /d "%~dp0"
echo ========================================
echo    在线考试系统启动中...
echo ========================================
echo.
python -m uvicorn main:app --host 0.0.0.0 --port 8000
pause
