# Python学习助手 - APK 打包指南

## 方案一：WSL + Buildozer（推荐）

### 1. 安装 WSL
```powershell
# 以管理员身份运行 PowerShell
wsl --install -d Ubuntu-22.04
# 重启电脑
```

### 2. 配置 Ubuntu 环境
```bash
# 进入 WSL
wsl

# 更新系统
sudo apt update && sudo apt upgrade -y

# 安装依赖
sudo apt install -y \
    git zip unzip openjdk-17-jdk python3 python3-pip \
    autoconf libtool pkg-config zlib1g-dev \
    libncurses5-dev libncursesw5-dev libtinfo5 \
    cmake libffi-dev libssl-dev automake

# 安装 buildozer
pip3 install --user buildozer cython

# 添加环境变量
echo 'export PATH=$PATH:~/.local/bin' >> ~/.bashrc
source ~/.bashrc
```

### 3. 复制项目文件
```bash
# 创建项目目录
mkdir -p ~/python-learn-android
cd ~/python-learn-android

# 从 Windows 复制文件（在 WSL 中执行）
cp -r /mnt/c/Users/Administrator/.qclaw/workspace/python-learn-android/* .
```

### 4. 打包 APK
```bash
# 初始化 buildozer（如果还没有 buildozer.spec）
buildozer init

# 编辑 buildozer.spec 配置文件
# 修改以下关键配置：
# title = Python学习助手
# package.name = pythonlearn
# package.domain = com.mengge.pythonlearn
# requirements = python3,kivy
# android.archs = arm64-v8a, armeabi-v7a

# 开始打包（首次会自动下载 Android SDK/NDK，需要梯子）
buildozer android debug

# 打包完成后，APK 在 ./bin 目录
```

## 方案二：Docker + Buildozer

### 1. 安装 Docker Desktop
下载地址：https://www.docker.com/products/docker-desktop

### 2. 使用 Buildozer Docker 镜像
```bash
# 拉取镜像
docker pull kivy/buildozer

# 运行容器（挂载项目目录）
docker run -it --rm \
    -v "$(pwd):/home/user/app" \
    -v "~/.buildozer:/home/user/.buildozer" \
    kivy/buildozer android debug
```

## 方案三：GitHub Actions 自动打包

### 1. 创建 GitHub 仓库
```bash
cd python-learn-android
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/LeeMeng1994/python-learn-android.git
git push -u origin main
```

### 2. 创建 GitHub Actions 工作流
创建文件 `.github/workflows/build-apk.yml`：

```yaml
name: Build APK

on:
  push:
    branches: [ main ]
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'
    
    - name: Install dependencies
      run: |
        sudo apt update
        sudo apt install -y git zip unzip openjdk-17-jdk
        pip install buildozer cython
    
    - name: Build APK
      run: |
        buildozer android debug
    
    - name: Upload APK
      uses: actions/upload-artifact@v3
      with:
        name: apk
        path: bin/*.apk
```

### 3. 触发构建
- 推送代码到 GitHub
- 在 Actions 标签页查看构建进度
- 下载生成的 APK

## 方案四：使用 Kivy Launcher（快速测试）

### 1. 下载 Kivy Launcher
https://github.com/kivy/kivy-launcher/releases

### 2. 安装并运行
- 安装 Kivy Launcher APK
- 将项目文件放入手机存储的 `/kivy/python-learn-android` 目录
- 在 Kivy Launcher 中选择运行

## 当前项目状态

- ✅ Kivy 应用代码完成（main.py）
- ✅ 24门课程数据
- ✅ 成就系统
- ✅ 学习统计
- ✅ 代码运行功能
- ⏳ 需要打包成 APK

## 推荐路径

1. **快速测试**：使用 Kivy Launcher
2. **正式发布**：使用 WSL + Buildozer 或 GitHub Actions
