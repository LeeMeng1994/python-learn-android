# HBuilderX 打包 Python学习助手 APK 指南

## 方案概述
使用 HBuilderX 的「原生App-云打包」功能，将 Kivy 应用打包为 APK。

## 准备工作

### 1. 安装 HBuilderX
- 下载地址：https://www.dcloud.io/hbuilderx.html
- 安装并启动

### 2. 注册 DCloud 账号
- 在 HBuilderX 中登录 DCloud 账号
- 完成实名认证（打包需要）

## 项目改造步骤

### 1. 创建 5+ App 项目结构
```
python-learn-android/
├── manifest.json          # App 配置
├── index.html             # 入口页面
├── js/
│   └── main.js            # 调用 Python 的逻辑
├── py/
│   └── main.py            # Kivy 代码（已存在）
└── unpackage/
    └── res/
        └── icons/         # 应用图标
```

### 2. 创建 manifest.json
```json
{
    "name": "Python学习助手",
    "version": {
        "name": "1.0.0",
        "code": "100"
    },
    "description": "Python编程学习应用",
    "launch_path": "index.html",
    "icons": {
        "72": "icon.png"
    },
    "developer": {
        "name": "LeeMeng",
        "email": ""
    },
    "permissions": {
        "Storage": {
            "description": "存储学习进度"
        }
    }
}
```

### 3. 创建 index.html
```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python学习助手</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            background: #1a1a2e;
            color: white;
            font-family: -apple-system, sans-serif;
        }
        #app {
            width: 100vw;
            height: 100vh;
            display: flex;
            flex-direction: column;
        }
        #header {
            padding: 15px;
            background: #16213e;
            text-align: center;
            font-size: 18px;
            font-weight: bold;
        }
        #content {
            flex: 1;
            overflow-y: auto;
            padding: 15px;
        }
        .course-item {
            background: #0f3460;
            padding: 15px;
            margin-bottom: 10px;
            border-radius: 10px;
        }
        .course-title {
            font-size: 16px;
            font-weight: bold;
            margin-bottom: 5px;
        }
        .course-desc {
            font-size: 14px;
            color: #aaa;
        }
    </style>
</head>
<body>
    <div id="app">
        <div id="header">Python学习助手</div>
        <div id="content">
            <div class="course-item">
                <div class="course-title">第1章：Python基础</div>
                <div class="course-desc">变量、数据类型、运算符</div>
            </div>
            <div class="course-item">
                <div class="course-title">第2章：流程控制</div>
                <div class="course-desc">条件语句、循环语句</div>
            </div>
            <div class="course-item">
                <div class="course-title">第3章：函数与模块</div>
                <div class="course-desc">函数定义、参数、模块导入</div>
            </div>
        </div>
    </div>
    
    <script>
        // 这里可以调用 Native.js 或 Plus API
        document.addEventListener('plusready', function() {
            console.log('5+ Runtime ready');
        });
    </script>
</body>
</html>
```

## 打包步骤

### 1. 导入项目
- 打开 HBuilderX
- 文件 → 导入 → 从本地目录导入
- 选择 `python-learn-android` 文件夹

### 2. 配置应用
- 打开 `manifest.json`
- 填写应用名称、版本、描述
- 上传应用图标（1024x1024）
- 配置权限（存储、网络等）

### 3. 云打包
- 点击菜单栏：发行 → 原生App-云打包
- 选择「使用DCloud公测证书」（测试用）
- 或「使用自有证书」（发布用）
- 选择打包类型：Android APK
- 点击「打包」

### 4. 等待打包完成
- 云端打包通常需要 5-15 分钟
- 打包完成后自动下载 APK

## 替代方案：本地打包（需要 Android Studio）

如果云打包排队太久，可以使用本地打包：

### 1. 生成 App 资源
- 发行 → 原生App-本地打包 → 生成本地打包App资源

### 2. 使用 Android Studio
- 下载 Android 离线 SDK：https://nativesupport.dcloud.net.cn/AppDocs/usesdk/android.html
- 将生成的资源复制到 SDK 中
- 使用 Android Studio 编译 APK

## 注意事项

1. **Kivy 兼容性**：HBuilderX 主要支持 WebView，Kivy 需要特殊处理
2. **Python 运行**：在移动端运行 Python 需要 PyDroid3 或类似方案
3. **替代思路**：考虑将 Kivy 改为 Web 版本（HTML/JS），更容易打包

## 推荐方案

由于 Kivy 在 HBuilderX 中支持有限，建议：

1. **使用 PyDroid3**：直接在安卓安装 PyDroid3，运行 Python 代码
2. **Web 版本**：用 HTML/JS 重写界面，通过 HBuilderX 打包
3. **Kivy + Buildozer**：回到 WSL 方案（虽然 exec 超时，但 WSL 本身正常）
