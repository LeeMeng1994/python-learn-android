# WSL 安装后继续配置 Buildozer

Write-Host "=== 配置 Ubuntu WSL 环境 ===" -ForegroundColor Green

# 在 WSL 中安装依赖
$wslCommands = @"
# 更新系统
sudo apt update && sudo apt upgrade -y

# 安装必要依赖
sudo apt install -y \
    git \
    zip \
    unzip \
    openjdk-17-jdk \
    python3 \
    python3-pip \
    autoconf \
    libtool \
    pkg-config \
    zlib1g-dev \
    libncurses5-dev \
    libncursesw5-dev \
    libtinfo5 \
    cmake \
    libffi-dev \
    libssl-dev \
    automake

# 安装 buildozer
pip3 install --user buildozer cython

# 配置环境变量
echo 'export PATH=\$PATH:~/.local/bin' >> ~/.bashrc

# 创建工作目录
mkdir -p ~/python-learn-android
cd ~/python-learn-android

echo "=== 环境配置完成 ==="
echo "请将项目文件复制到 ~/python-learn-android 目录"
echo "然后运行: buildozer android debug"
"@

# 写入 WSL 脚本
$wslCommands | wsl tee /tmp/setup.sh > $null
wsl bash /tmp/setup.sh

Write-Host "`n=== 配置完成 ===" -ForegroundColor Green
Write-Host "请将 python-learn-android 项目文件复制到 WSL:" -ForegroundColor Yellow
Write-Host "wsl cp -r /mnt/c/Users/Administrator/.qclaw/workspace/python-learn-android/* ~/python-learn-android/" -ForegroundColor Cyan
