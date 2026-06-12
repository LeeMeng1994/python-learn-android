# Web 版本打包指南（无需 Google Play）

## 方案概述
使用 HBuilderX 云打包，将 Web 版本打包为 Android APK。

## 优点
- ✅ 无需 Google Play
- ✅ 纯 Web 技术，兼容性好
- ✅ 云打包免费
- ✅ 支持离线存储（localStorage）

## 步骤

### 1. 下载 HBuilderX
- 官网：https://www.dcloud.io/hbuilderx.html
- 下载对应系统版本

### 2. 注册 DCloud 账号
- 打开 HBuilderX
- 点击右上角登录
- 注册并完成实名认证（免费）

### 3. 导入项目
1. 打开 HBuilderX
2. 文件 → 打开目录
3. 选择 `python-learn-android/web-version` 文件夹

### 4. 配置应用
1. 打开 `manifest.json`
2. 填写应用信息：
   - 应用名称：Python学习助手
   - 版本号：1.0.0
   - 应用描述：零基础学Python
3. 上传应用图标（右键点击项目 → 新建 → 图标配置）

### 5. 云打包
1. 点击菜单栏：发行 → 原生App-云打包
2. 选择：
   - Android APK
   - 使用 DCloud 公测证书（测试用）
   - 或上传自有证书（正式发布用）
3. 点击「打包」

### 6. 等待打包完成
- 通常需要 5-15 分钟
- 打包完成后自动下载 APK

## 项目文件说明

```
web-version/
├── index.html      # 主页面（包含所有代码）
├── manifest.json   # 应用配置
└── icon.png        # 应用图标（需自行准备）
```

## 功能特性

### 已实现
- 📚 8 门课程（可扩展）
- ✅ 学习进度标记
- 📊 学习统计
- 🎨 主题切换（深色/浅色）
- 💾 本地存储（localStorage）
- 📱 移动端适配

### 可扩展
- 添加更多课程
- 添加代码运行功能（需要后端）
- 添加练习题目
- 添加成就系统

## 添加更多课程

编辑 `index.html` 中的 `courses` 数组：

```javascript
const courses = [
    {
        id: 9,
        title: '第9课：文件操作',
        desc: '读写文件',
        content: '...',
        code: '...'
    },
    // 添加更多课程...
];
```

## 注意事项

1. **图标**：需要准备 1024x1024 的 PNG 图标
2. **证书**：正式发布需要申请自有证书
3. **权限**：应用使用 localStorage，不需要额外权限
4. **网络**：首次加载需要网络，之后可离线使用

## 替代打包方式

### 方式1：本地打包（需要 Android Studio）
1. 发行 → 原生App-本地打包 → 生成本地打包App资源
2. 下载 Android 离线 SDK
3. 用 Android Studio 编译

### 方式2：在线工具
使用第三方在线打包工具，如：
- Website 2 APK Builder
- Web2Apk

## 发布到应用市场

打包完成后，可以发布到：
- 华为应用市场
- 小米应用商店
- OPPO应用商店
- vivo应用商店
- 应用宝
- 酷安

（不需要 Google Play）
