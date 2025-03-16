@echo off
echo 提取PDF页面工具
echo ================

REM 检查Python是否已安装
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo 错误: 未安装Python或Python不在PATH环境变量中
    echo 请安装Python并确保将其添加到PATH环境变量中
    pause
    exit /b 1
)

REM 检查是否提供了足够的参数
if "%~4"=="" (
    echo 用法: %~nx0 输入PDF文件 输出PDF文件 起始页码 结束页码
    echo 例如: %~nx0 "2024上半年新版论文集\野人老师论文集2024上半年.pdf" "提取的页面.pdf" 27 30
    pause
    exit /b 1
)

REM 运行Python脚本
python extract_pdf_pages.py "%~1" "%~2" %~3 %~4

pause 