# WSL 安装和 Buildozer 配置脚本

Write-Host "=== 安装 WSL ===" -ForegroundColor Green
wsl --install -d Ubuntu --no-launch

Write-Host "`n=== 等待 WSL 安装完成 ===" -ForegroundColor Green
Write-Host "安装完成后请重启电脑，然后再次运行此脚本继续配置" -ForegroundColor Yellow
Write-Host "`n重启后执行: .\setup_wsl.ps1 -Continue" -ForegroundColor Cyan
