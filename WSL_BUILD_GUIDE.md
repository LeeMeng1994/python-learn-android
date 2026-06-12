# WSL 手动打包指南

## 前提条件
WSL2 + Ubuntu-22.04 已安装（已确认）

## 步骤

### 1. 打开 WSL 终端
在 PowerShell 中运行：
```powershell
wsl -d Ubuntu-22.04
```

### 2. 更新系统
```bash
sudo apt update && sudo apt upgrade -y
```

### 3. 安装依赖
```bash
sudo apt install -y \
    git zip unzip openjdk-17-jdk python3 python3-pip \
    autoconf libtool pkg-config zlib1g-dev \
    libncurses5-dev libncursesw5-dev libtinfo5 \
    cmake libffi-dev libssl-dev automake
```

### 4. 安装 Buildozer
```bash
pip3 install --user buildozer cython

# 添加环境变量
echo 'export PATH=$PATH:~/.local/bin' >> ~/.bashrc
source ~/.bashrc
```

### 5. 复制项目文件
```bash
# 创建项目目录
mkdir -p ~/python-learn-android
cd ~/python-learn-android

# 从 Windows 复制文件
cp -r /mnt/c/Users/Administrator/.qclaw/workspace/python-learn-android/* .
```

### 6. 打包 APK
```bash
# 首次运行会自动下载 Android SDK/NDK（需要网络）
buildozer android debug

# 打包完成后，APK 在 ./bin 目录
```

### 7. 复制 APK 到 Windows
```bash
cp bin/*.apk /mnt/c/Users/Administrator/Desktop/
```

## 常见问题

1. **下载慢/失败**：需要配置代理或更换镜像源
2. **内存不足**：WSL2 默认内存可能不够，创建 `.wslconfig` 文件增加内存
3. **磁盘空间**：确保 WSL 磁盘有 10GB+ 空间

## 替代方案

如果 WSL 打包困难，可以使用：
1. **GitHub Actions** - 已配置工作流，推送代码自动打包
2. **Kivy Launcher** - 快速测试，无需打包
