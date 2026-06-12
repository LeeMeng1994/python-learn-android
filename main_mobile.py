"""
Python学习助手 - 手机简化版
适合在 PyDroid3 上运行
"""
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty
import json
import os

# 设置窗口背景色（深色主题）
Window.clearcolor = (0.1, 0.1, 0.2, 1)

# 课程数据
COURSES = [
    {
        'id': 1,
        'title': '第1课：变量与数据类型',
        'desc': '学习Python基础概念',
        'content': '''
变量是存储数据的容器。

示例：
name = "小明"      # 字符串
age = 18          # 整数
height = 1.75     # 浮点数
is_student = True # 布尔值

练习：
创建一个变量存储你的年龄，并打印出来。
        ''',
        'code_example': 'age = 18\nprint("我的年龄是:", age)'
    },
    {
        'id': 2,
        'title': '第2课：运算符',
        'desc': '算术、比较、逻辑运算符',
        'content': '''
算术运算符：+  -  *  /  //  %  **
比较运算符：==  !=  >  <  >=  <=
逻辑运算符：and  or  not

示例：
a = 10
b = 3
print(a + b)   # 13
print(a // b)  # 3
print(a > b)   # True
        ''',
        'code_example': 'a = 10\nb = 3\nprint(a + b)'
    },
    {
        'id': 3,
        'title': '第3课：条件语句',
        'desc': 'if-else 判断',
        'content': '''
条件语句让程序可以做出选择。

示例：
age = 18
if age >= 18:
    print("成年人")
else:
    print("未成年人")

练习：
写一个程序，判断一个数是正数、负数还是零。
        ''',
        'code_example': 'age = 18\nif age >= 18:\n    print("成年人")'
    },
    {
        'id': 4,
        'title': '第4课：循环语句',
        'desc': 'for 和 while 循环',
        'content': '''
循环让程序可以重复执行代码。

for 循环：
for i in range(5):
    print(i)

while 循环：
count = 0
while count < 5:
    print(count)
    count += 1

练习：
用循环打印 1 到 10 的所有偶数。
        ''',
        'code_example': 'for i in range(5):\n    print(i)'
    },
    {
        'id': 5,
        'title': '第5课：函数基础',
        'desc': '定义和调用函数',
        'content': '''
函数是可重复使用的代码块。

示例：
def greet(name):
    return "你好, " + name

message = greet("小明")
print(message)

练习：
写一个函数，计算两个数的和。
        ''',
        'code_example': 'def greet(name):\n    return "你好, " + name\nprint(greet("小明"))'
    },
    {
        'id': 6,
        'title': '第6课：列表与元组',
        'desc': '序列数据类型',
        'content': '''
列表（List）：可变序列
fruits = ["苹果", "香蕉", "橙子"]
fruits.append("葡萄")

元组（Tuple）：不可变序列
coordinates = (10, 20)

练习：
创建一个列表，添加三个元素，然后打印第二个元素。
        ''',
        'code_example': 'fruits = ["苹果", "香蕉"]\nfruits.append("橙子")\nprint(fruits)'
    },
    {
        'id': 7,
        'title': '第7课：字典与集合',
        'desc': '映射和集合类型',
        'content': '''
字典（Dict）：键值对存储
student = {
    "name": "小明",
    "age": 18
}
print(student["name"])

集合（Set）：无序不重复
numbers = {1, 2, 3, 3, 3}
print(numbers)  # {1, 2, 3}

练习：
创建一个字典存储你的信息，并打印出来。
        ''',
        'code_example': 'student = {"name": "小明", "age": 18}\nprint(student["name"])'
    },
    {
        'id': 8,
        'title': '第8课：字符串操作',
        'desc': '字符串处理方法',
        'content': '''
字符串是Python中常用的数据类型。

text = "  Hello World  "
print(text.strip())      # 去除空格
print(text.lower())      # 转小写
print(text.upper())      # 转大写
print(text.replace("Hello", "Hi"))

格式化：
name = "小明"
age = 18
print(f"{name}今年{age}岁")

练习：
将一个字符串反转并打印。
        ''',
        'code_example': 'name = "小明"\nprint(f"你好, {name}")'
    },
]

class PythonLearningApp(App):
    def build(self):
        self.title = 'Python学习助手'
        self.progress = self.load_progress()
        return MainScreen(self)
    
    def load_progress(self):
        """加载学习进度"""
        try:
            if os.path.exists('progress.json'):
                with open('progress.json', 'r', encoding='utf-8') as f:
                    return json.load(f)
        except:
            pass
        return {'completed': [], 'current_course': 1}
    
    def save_progress(self):
        """保存学习进度"""
        try:
            with open('progress.json', 'w', encoding='utf-8') as f:
                json.dump(self.progress, f, ensure_ascii=False)
        except:
            pass

class MainScreen(BoxLayout):
    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10
        
        # 标题栏
        title_box = BoxLayout(size_hint_y=None, height=60, spacing=10)
        title = Label(
            text='Python学习助手',
            font_size='22sp',
            color=(0.3, 0.7, 1, 1),
            bold=True
        )
        title_box.add_widget(title)
        self.add_widget(title_box)
        
        # 进度条
        completed = len(app.progress['completed'])
        total = len(COURSES)
        progress_label = Label(
            text=f'学习进度: {completed}/{total} 课',
            font_size='14sp',
            color=(0.7, 0.7, 0.7, 1),
            size_hint_y=None,
            height=30
        )
        self.add_widget(progress_label)
        
        # 课程列表
        scroll = ScrollView()
        grid = GridLayout(cols=1, spacing=8, size_hint_y=None, padding=[0, 5])
        grid.bind(minimum_height=grid.setter('height'))
        
        for course in COURSES:
            is_completed = course['id'] in app.progress['completed']
            btn = Button(
                text=f"{'✅ ' if is_completed else ''}{course['title']}\n{course['desc']}",
                size_hint_y=None,
                height=70,
                background_color=(0.2, 0.5, 0.3, 1) if is_completed else (0.2, 0.4, 0.8, 1),
                halign='center',
                valign='middle',
                font_size='14sp'
            )
            btn.course = course
            btn.bind(on_press=self.show_lesson)
            grid.add_widget(btn)
        
        scroll.add_widget(grid)
        self.add_widget(scroll)
        
        # 底部按钮
        bottom = BoxLayout(size_hint_y=None, height=50, spacing=10)
        
        stats_btn = Button(
            text='📊 统计',
            background_color=(0.3, 0.6, 0.3, 1),
            font_size='14sp'
        )
        stats_btn.bind(on_press=self.show_stats)
        
        theme_btn = Button(
            text='🎨 主题',
            background_color=(0.6, 0.3, 0.6, 1),
            font_size='14sp'
        )
        theme_btn.bind(on_press=self.toggle_theme)
        
        reset_btn = Button(
            text='🔄 重置',
            background_color=(0.8, 0.3, 0.3, 1),
            font_size='14sp'
        )
        reset_btn.bind(on_press=self.reset_progress)
        
        bottom.add_widget(stats_btn)
        bottom.add_widget(theme_btn)
        bottom.add_widget(reset_btn)
        self.add_widget(bottom)
    
    def show_lesson(self, instance):
        course = instance.course
        
        content = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # 课程标题
        content.add_widget(Label(
            text=course['title'],
            font_size='18sp',
            color=(0.3, 0.7, 1, 1),
            size_hint_y=None,
            height=40,
            bold=True
        ))
        
        # 课程内容（可滚动）
        scroll = ScrollView()
        text = Label(
            text=course['content'],
            font_size='13sp',
            color=(0.9, 0.9, 0.9, 1),
            size_hint_y=None,
            text_size=(Window.width * 0.8, None),
            halign='left',
            valign='top'
        )
        text.bind(texture_size=text.setter('size'))
        scroll.add_widget(text)
        content.add_widget(scroll)
        
        # 代码示例
        if course.get('code_example'):
            content.add_widget(Label(
                text='代码示例:',
                font_size='14sp',
                color=(0.5, 0.8, 0.5, 1),
                size_hint_y=None,
                height=25,
                halign='left'
            ))
            code_input = TextInput(
                text=course['code_example'],
                multiline=True,
                readonly=True,
                size_hint_y=None,
                height=100,
                background_color=(0.15, 0.15, 0.15, 1),
                foreground_color=(0.5, 0.8, 0.5, 1),
                font_size='12sp'
            )
            content.add_widget(code_input)
        
        # 按钮区域
        btn_box = BoxLayout(size_hint_y=None, height=50, spacing=10)
        
        # 标记完成按钮
        is_completed = course['id'] in self.app.progress['completed']
        complete_btn = Button(
            text='✅ 标记完成' if not is_completed else '✅ 已完成',
            background_color=(0.3, 0.6, 0.3, 1) if not is_completed else (0.5, 0.5, 0.5, 1),
            disabled=is_completed
        )
        complete_btn.bind(on_press=lambda x: self.mark_complete(course['id'], popup))
        
        close_btn = Button(
            text='关闭',
            background_color=(0.5, 0.5, 0.5, 1)
        )
        
        btn_box.add_widget(complete_btn)
        btn_box.add_widget(close_btn)
        content.add_widget(btn_box)
        
        popup = Popup(
            title='课程详情',
            content=content,
            size_hint=(0.95, 0.9),
            auto_dismiss=False
        )
        close_btn.bind(on_press=popup.dismiss)
        popup.open()
    
    def mark_complete(self, course_id, popup):
        if course_id not in self.app.progress['completed']:
            self.app.progress['completed'].append(course_id)
            self.app.save_progress()
            popup.dismiss()
            # 刷新界面
            self.clear_widgets()
            self.__init__(self.app)
    
    def show_stats(self, instance):
        completed = len(self.app.progress['completed'])
        total = len(COURSES)
        percentage = (completed / total * 100) if total > 0 else 0
        
        content = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        content.add_widget(Label(
            text='📊 学习统计',
            font_size='22sp',
            color=(0.3, 0.7, 1, 1),
            size_hint_y=None,
            height=40
        ))
        
        stats_text = f'''
总课程数: {total}
已完成: {completed}
完成率: {percentage:.1f}%

继续加油！💪
        '''
        
        content.add_widget(Label(
            text=stats_text,
            font_size='16sp',
            color=(0.9, 0.9, 0.9, 1)
        ))
        
        close_btn = Button(
            text='关闭',
            size_hint_y=None,
            height=50,
            background_color=(0.5, 0.5, 0.5, 1)
        )
        
        popup = Popup(title='统计', content=content, size_hint=(0.8, 0.6))
        close_btn.bind(on_press=popup.dismiss)
        content.add_widget(close_btn)
        popup.open()
    
    def toggle_theme(self, instance):
        if Window.clearcolor == [0.1, 0.1, 0.2, 1]:
            Window.clearcolor = (0.95, 0.95, 0.95, 1)
        else:
            Window.clearcolor = (0.1, 0.1, 0.2, 1)
    
    def reset_progress(self, instance):
        content = BoxLayout(orientation='vertical', padding=20, spacing=15)
        content.add_widget(Label(
            text='确定要重置所有学习进度吗？',
            font_size='16sp',
            color=(0.9, 0.9, 0.9, 1)
        ))
        
        btn_box = BoxLayout(size_hint_y=None, height=50, spacing=10)
        
        yes_btn = Button(text='确定', background_color=(0.8, 0.3, 0.3, 1))
        no_btn = Button(text='取消', background_color=(0.5, 0.5, 0.5, 1))
        
        btn_box.add_widget(yes_btn)
        btn_box.add_widget(no_btn)
        content.add_widget(btn_box)
        
        popup = Popup(title='确认重置', content=content, size_hint=(0.8, 0.4))
        
        def confirm_reset(x):
            self.app.progress = {'completed': [], 'current_course': 1}
            self.app.save_progress()
            popup.dismiss()
            self.clear_widgets()
            self.__init__(self.app)
        
        yes_btn.bind(on_press=confirm_reset)
        no_btn.bind(on_press=popup.dismiss)
        popup.open()

if __name__ == '__main__':
    PythonLearningApp().run()
