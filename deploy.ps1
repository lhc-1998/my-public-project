# 在线考试系统 Windows 部署脚本

Write-Host "=== 在线考试系统部署脚本 ===" -ForegroundColor Green

# 1. 检查 Python
Write-Host "`n[1/6] 检查 Python..." -ForegroundColor Yellow
python --version
if ($LASTEXITCODE -ne 0) {
    Write-Host "错误: Python 未安装或未添加到 PATH" -ForegroundColor Red
    Write-Host "请先安装 Python: https://www.python.org/downloads/" -ForegroundColor Red
    exit 1
}

# 2. 检查 MySQL
Write-Host "`n[2/6] 检查 MySQL..." -ForegroundColor Yellow
mysql --version
if ($LASTEXITCODE -ne 0) {
    Write-Host "警告: MySQL 命令行工具可能未配置到 PATH" -ForegroundColor Yellow
    Write-Host "请确保 MySQL 服务已启动" -ForegroundColor Yellow
}

# 3. 创建数据库
Write-Host "`n[3/6] 创建数据库..." -ForegroundColor Yellow
$mysqlCmd = "mysql -u root -p"
Write-Host "请在 MySQL 中执行以下命令创建数据库:" -ForegroundColor Cyan
Write-Host "  CREATE DATABASE exam_system CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;" -ForegroundColor Green
Write-Host "  CREATE USER 'exam'@'localhost' IDENTIFIED BY 'exam123';" -ForegroundColor Green
Write-Host "  GRANT ALL PRIVILEGES ON exam_system.* TO 'exam'@'localhost';" -ForegroundColor Green
Write-Host "  FLUSH PRIVILEGES;" -ForegroundColor Green
Write-Host "`n或者直接修改 .env 文件中的数据库配置" -ForegroundColor Cyan

# 4. 安装依赖
Write-Host "`n[4/6] 安装 Python 依赖..." -ForegroundColor Yellow
pip install -r requirements.txt
if ($LASTEXITCODE -ne 0) {
    Write-Host "错误: 依赖安装失败" -ForegroundColor Red
    exit 1
}

# 5. 初始化数据库
Write-Host "`n[5/6] 初始化数据库..." -ForegroundColor Yellow
python init_db.py
if ($LASTEXITCODE -ne 0) {
    Write-Host "警告: 数据库初始化可能有错误，请检查配置" -ForegroundColor Yellow
}

# 6. 启动应用
Write-Host "`n[6/6] 启动应用..." -ForegroundColor Yellow
Write-Host "`n========================================" -ForegroundColor Green
Write-Host "部署完成！" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host "`n请确保腾讯云安全组已开放 8015 端口" -ForegroundColor Cyan
Write-Host "然后运行以下命令启动服务:" -ForegroundColor Cyan
Write-Host "  python -m uvicorn main:app --host 0.0.0.0 --port 8015" -ForegroundColor Green
Write-Host "`n访问地址: http://43.129.21.157:8015" -ForegroundColor Green
Write-Host "API文档:   http://43.129.21.157:8015/docs" -ForegroundColor Green
