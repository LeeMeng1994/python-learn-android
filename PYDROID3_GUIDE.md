# PyDroid3 运行 Python学习助手指南

## 方案概述
在安卓手机上安装 PyDroid3，直接运行 Kivy 代码，无需打包 APK。

## 优点
- ✅ 无需打包，直接运行
- ✅ 支持 Kivy 完整功能
- ✅ 可以安装任意 Python 包
- ✅ 代码可实时修改调试

## 步骤

### 1. 安装 PyDroid3
1. 打开 Google Play 商店
2. 搜索 "PyDroid 3"
3. 安装（免费版即可）

### 2. 安装依赖
打开 PyDroid3，在终端中运行：
```bash
pip install kivy
```

### 3. 复制项目文件
将以下文件传到手机：
- `main.py`（主程序）
- `buildozer.spec`（可选，不需要）

传输方式：
- 微信文件传输
- QQ 文件助手
- 数据线连接电脑复制
- 上传到 GitHub 后手机下载

### 4. 运行程序
1. 在 PyDroid3 中打开 `main.py`
2. 点击运行按钮（▶️）
3. 即可看到 Kivy 界面

## 文件准备

### 简化版 main.py（适合手机运行）
```python
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from kivy.properties import StringProperty, ListProperty, DictProperty
from kivy.animation import Animation
from kivy.uix.progressbar import ProgressBar
import json
import os
from datetime import datetime

# 设置窗口背景色
Window.clearcolor = (0.1, 0.1, 0.2, 1)

class PythonLearningApp(App):
    def build(self):
        self.title = 'Python学习助手'
        return MainScreen()

class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10
        
        # 标题
        title = Label(
            text='Python学习助手',
            font_size='24sp',
            size_hint_y=None,
            height=50,
            color=(0.3, 0.7, 1, 1)
        )
        self.add_widget(title)
        
        # 课程列表
        scroll = ScrollView()
        grid = GridLayout(cols=1, spacing=10, size_hint_y=None)
        grid.bind(minimum_height=grid.setter('height'))
        
        courses = [
            ('第1课：变量与数据类型', '学习Python基础概念'),
            ('第2课：运算符', '算术、比较、逻辑运算符'),
            ('第3课：条件语句', 'if-else 判断'),
            ('第4课：循环语句', 'for 和 while 循环'),
            ('第5课：函数基础', '定义和调用函数'),
            ('第6课：列表与元组', '序列数据类型'),
            ('第7课：字典与集合', '映射和集合类型'),
            ('第8课：字符串操作', '字符串处理方法'),
        ]
        
        for title, desc in courses:
            btn = Button(
                text=f'{title}\n{desc}',
                size_hint_y=None,
                height=80,
                background_color=(0.2, 0.4, 0.8, 1),
                halign='center'
            )
            btn.bind(on_press=self.show_lesson)
            grid.add_widget(btn)
        
        scroll.add_widget(grid)
        self.add_widget(scroll)
        
        # 底部按钮
        bottom = BoxLayout(size_hint_y=None, height=50, spacing=10)
        
        stats_btn = Button(text='学习统计', background_color=(0.3, 0.6, 0.3, 1))
        stats_btn.bind(on_press=self.show_stats)
        
        theme_btn = Button(text='切换主题', background_color=(0.6, 0.3, 0.6, 1))
        theme_btn.bind(on_press=self.toggle_theme)
        
        bottom.add_widget(stats_btn)
        bottom.add_widget(theme_btn)
        self.add_widget(bottom)
    
    def show_lesson(self, instance):
        content = BoxLayout(orientation='vertical', padding=10, spacing=10)
        content.add_widget(Label(text=instance.text, font_size='18sp'))
        content.add_widget(Label(text='课程内容区域\n可以添加代码示例、练习题等', 
                                font_size='14sp', color=(0.7, 0.7, 0.7, 1)))
        
        close_btn = Button(text='关闭', size_hint_y=None, height=50)
        popup = Popup(title='课程详情', content=content, size_hint=(0.9, 0.9))
        close_btn.bind(on_press=popup.dismiss)
        content.add_widget(close_btn)
        popup.open()
    
    def show_stats(self, instance):
        content = BoxLayout(orientation='vertical', padding=10)
        content.add_widget(Label(text='学习统计', font_size='20sp', color=(0.3, 0.7, 1, 1)))
        content.add_widget(Label(text='已完成课程：3/24\n学习时长：2小时\n连续学习：5天', 
                                font_size='16sp'))
        
        close_btn = Button(text='关闭', size_hint_y=None, height=50)
        popup = Popup(title='统计', content=content, size_hint=(0.8, 0.6))
        close_btn.bind(on_press=popup.dismiss)
        content.add_widget(close_btn)
        popup.open()
    
    def toggle_theme(self, instance):
        if Window.clearcolor == [0.1, 0.1, 0.2, 1]:
            Window.clearcolor = (0.95, 0.95, 0.95, 1)
        else:
            Window.clearcolor = (0.1, 0.1, 0.2, 1)

if __name__ == '__main__':
    PythonLearningApp().run()
```

## 手机端操作

### 1. 保存代码
在 PyDroid3 中：
1. 新建文件 → 命名为 `main.py`
2. 粘贴上面的代码
3. 保存

### 2. 安装 Kivy
在 PyDroid3 终端：
```bash
pip install kivy
```

### 3. 运行
点击右上角的 ▶️ 运行按钮

## 进阶：使用完整版代码

如果你的完整 `main.py` 文件较大：

1. 将 `main.py` 传到手机存储
2. 在 PyDroid3 中打开文件
3. 确保安装了所有依赖：
```bash
pip install kivy
```

## 注意事项

1. **性能**：手机运行 Kivy 可能比电脑慢一些
2. **屏幕适配**：Kivy 会自动适配手机屏幕
3. **存储**：学习进度可以保存在手机本地文件
4. **横屏**：建议锁定竖屏或适配横屏布局

## 替代：Pydroid 3 + Kivy Launcher

如果 PyDroid3 运行 Kivy 有问题，可以尝试：
1. 安装 "Kivy Launcher" APK
2. 将项目放在 `/sdcard/kivy/` 目录
3. 在 Kivy Launcher 中选择运行
