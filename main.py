from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.utils import platform
import json
import os
import sys
import io

# 设置窗口大小（模拟手机屏幕）
Window.size = (400, 700)

# 主题配置
THEMES = {
    'light': {
        'bg': (0.95, 0.95, 0.95, 1),
        'card': (1, 1, 1, 1),
        'text': (0.1, 0.1, 0.1, 1),
        'primary': (0.2, 0.6, 0.9, 1),
        'success': (0.3, 0.8, 0.3, 1),
        'warning': (0.9, 0.7, 0.2, 1),
        'danger': (0.9, 0.3, 0.3, 1),
        'code_bg': (0.1, 0.1, 0.1, 1),
        'code_text': (0.9, 0.9, 0.9, 1),
    },
    'dark': {
        'bg': (0.1, 0.1, 0.12, 1),
        'card': (0.18, 0.18, 0.22, 1),
        'text': (0.9, 0.9, 0.9, 1),
        'primary': (0.3, 0.7, 1, 1),
        'success': (0.4, 0.9, 0.4, 1),
        'warning': (1, 0.8, 0.3, 1),
        'danger': (1, 0.4, 0.4, 1),
        'code_bg': (0.05, 0.05, 0.05, 1),
        'code_text': (0.8, 0.9, 0.8, 1),
    }
}

# 课程数据
COURSES = [
    # 第一章：Python基础
    {"id": 1, "title": "Hello World", "chapter": 1, 
     "theory": "Python是最流行的编程语言之一。print()函数用于输出内容到屏幕。这是你的第一个Python程序！", 
     "code": "print('Hello, World!')\nprint('你好，Python！')", 
     "hint": "使用print函数输出Hello, World!"},
    {"id": 2, "title": "变量与数据类型", "chapter": 1, 
     "theory": "变量是存储数据的容器。Python有整数(int)、浮点数(float)、字符串(str)、布尔值(bool)等数据类型。", 
     "code": "name = 'Python'\nage = 30\npi = 3.14159\nis_cool = True\n\nprint(f'{name}已经{age}岁了')\nprint(f'圆周率: {pi}')\nprint(f'很酷吗: {is_cool}')", 
     "hint": "创建不同类型的变量并打印"},
    {"id": 3, "title": "运算符", "chapter": 1, 
     "theory": "Python支持算术运算符(+,-,*,/,//,%,**)、比较运算符(==,!=,>,<,>=,<=)和逻辑运算符(and,or,not)。", 
     "code": "a = 10\nb = 3\n\nprint(f'加法: {a + b}')\nprint(f'除法: {a / b:.2f}')\nprint(f'整除: {a // b}')\nprint(f'取余: {a % b}')\nprint(f'幂运算: {a ** b}')\nprint(f'相等: {a == b}')", 
     "hint": "使用各种运算符进行计算"},
    {"id": 4, "title": "条件语句", "chapter": 1, 
     "theory": "if-elif-else用于条件判断，根据条件执行不同代码块。缩进在Python中非常重要！", 
     "code": "score = 85\n\nif score >= 90:\n    print('优秀！')\nelif score >= 80:\n    print('良好！')\nelif score >= 60:\n    print('及格')\nelse:\n    print('需要加油')\n\nprint('判断完成')", 
     "hint": "使用if-elif-else判断成绩等级"},
    {"id": 5, "title": "循环语句", "chapter": 1, 
     "theory": "for循环用于遍历序列，while循环用于条件循环。break跳出循环，continue跳过当前迭代。", 
     "code": "# for循环\nfor i in range(5):\n    print(f'第{i+1}次循环')\n\nprint('---')\n\n# while循环\ncount = 0\nwhile count < 3:\n    print(f'while: {count}')\n    count += 1\n\nprint('循环结束')", 
     "hint": "使用for和while循环"},
    {"id": 6, "title": "列表", "chapter": 1, 
     "theory": "列表是Python最常用的数据结构，可以存储多个元素。支持索引、切片、增删改查等操作。", 
     "code": "fruits = ['苹果', '香蕉', '橙子']\nprint(f'原始列表: {fruits}')\n\nfruits.append('葡萄')\nprint(f'添加后: {fruits}')\n\nprint(f'第一个水果: {fruits[0]}')\nprint(f'最后两个: {fruits[-2:]}')\nprint(f'列表长度: {len(fruits)}')", 
     "hint": "创建列表并进行各种操作"},
    {"id": 7, "title": "字典", "chapter": 1, 
     "theory": "字典是键值对集合，用{}定义。键必须唯一且不可变，值可以是任何类型。", 
     "code": "student = {\n    'name': '小明',\n    'age': 18,\n    'grade': 'A'\n}\n\nprint(f'学生姓名: {student[\"name\"]}')\nprint(f'年龄: {student[\"age\"]}')\n\nstudent['score'] = 95\nstudent['city'] = '北京'\n\nprint(f'完整信息: {student}')\nprint(f'所有键: {list(student.keys())}')", 
     "hint": "创建字典并添加键值对"},
    {"id": 8, "title": "函数基础", "chapter": 1, 
     "theory": "函数是可重用的代码块，用def定义。可以接收参数、设置默认值、返回值。", 
     "code": "def greet(name, greeting='你好'):\n    return f'{greeting}, {name}!'\n\n# 调用函数\nmsg1 = greet('Python')\nmsg2 = greet('世界', 'Hello')\n\nprint(msg1)\nprint(msg2)\n\n# 计算函数\ndef add(a, b):\n    return a + b\n\nprint(f'5 + 3 = {add(5, 3)}')", 
     "hint": "定义并调用带参数的函数"},
    
    # 第二章：进阶编程
    {"id": 9, "title": "文件操作", "chapter": 2, 
     "theory": "Python可以读写文件。使用with语句可以自动关闭文件，是最佳实践。", 
     "code": "# 写入文件\nwith open('test.txt', 'w', encoding='utf-8') as f:\n    f.write('Hello Python!\\n')\n    f.write('第二行内容\\n')\n\nprint('文件写入完成')\n\n# 读取文件\nwith open('test.txt', 'r', encoding='utf-8') as f:\n    content = f.read()\n    print('文件内容:')\n    print(content)", 
     "hint": "使用with语句写入并读取文件"},
    {"id": 10, "title": "异常处理", "chapter": 2, 
     "theory": "try-except用于捕获和处理异常，防止程序崩溃。finally块无论是否异常都会执行。", 
     "code": "try:\n    result = 10 / 0\n    print(f'结果: {result}')\nexcept ZeroDivisionError:\n    print('错误：不能除以零！')\nexcept Exception as e:\n    print(f'其他错误: {e}')\nfinally:\n    print('程序继续执行...')\n\nprint('异常处理完成')", 
     "hint": "捕获除零异常并处理"},
    {"id": 11, "title": "列表推导式", "chapter": 2, 
     "theory": "列表推导式是创建列表的简洁方式。语法：[表达式 for 变量 in 可迭代对象 if 条件]", 
     "code": "# 基本列表推导式\nsquares = [x**2 for x in range(10)]\nprint(f'0-9的平方: {squares}')\n\n# 带条件的列表推导式\nevens = [x for x in range(20) if x % 2 == 0]\nprint(f'偶数: {evens}')\n\n# 字符串处理\nwords = ['hello', 'world', 'python']\nupper_words = [w.upper() for w in words]\nprint(f'大写: {upper_words}')", 
     "hint": "使用列表推导式创建列表"},
    {"id": 12, "title": "生成器", "chapter": 2, 
     "theory": "生成器使用yield关键字，可以惰性生成数据，节省内存。适合处理大数据。", 
     "code": "def fibonacci(n):\n    a, b = 0, 1\n    for _ in range(n):\n        yield a\n        a, b = b, a + b\n\nprint('斐波那契数列:')\nfor num in fibonacci(10):\n    print(num, end=' ')\nprint()\n\n# 生成器表达式\ngen = (x**2 for x in range(1000000))\nprint(f'前3个: {next(gen)}, {next(gen)}, {next(gen)}')", 
     "hint": "创建斐波那契生成器"},
    {"id": 13, "title": "装饰器", "chapter": 2, 
     "theory": "装饰器是修改函数行为的高级特性，使用@语法糖。常用于日志、计时、权限检查等。", 
     "code": "import time\n\ndef timer(func):\n    def wrapper(*args, **kwargs):\n        start = time.time()\n        result = func(*args, **kwargs)\n        elapsed = time.time() - start\n        print(f'{func.__name__} 执行时间: {elapsed:.4f}秒')\n        return result\n    return wrapper\n\n@timer\ndef slow_function():\n    time.sleep(0.1)\n    print('函数执行完成')\n\nslow_function()", 
     "hint": "创建计时装饰器"},
    {"id": 14, "title": "类与对象", "chapter": 2, 
     "theory": "类是面向对象编程的基础。使用class定义，__init__是构造方法，self代表实例本身。", 
     "code": "class Dog:\n    def __init__(self, name, age):\n        self.name = name\n        self.age = age\n    \n    def bark(self):\n        return f'{self.name}说: 汪汪!'\n    \n    def info(self):\n        return f'{self.name}今年{self.age}岁'\n\ndog = Dog('旺财', 3)\nprint(dog.info())\nprint(dog.bark())", 
     "hint": "定义Dog类并创建实例"},
    {"id": 15, "title": "继承与多态", "chapter": 2, 
     "theory": "继承允许子类继承父类的属性和方法。多态允许不同类对同一方法做出不同响应。", 
     "code": "class Animal:\n    def __init__(self, name):\n        self.name = name\n    \n    def speak(self):\n        return '...'\n\nclass Cat(Animal):\n    def speak(self):\n        return f'{self.name}: 喵喵'\n\nclass Dog(Animal):\n    def speak(self):\n        return f'{self.name}: 汪汪'\n\nanimals = [Cat('小花'), Dog('旺财')]\nfor animal in animals:\n    print(animal.speak())", 
     "hint": "实现继承和多态"},
    {"id": 16, "title": "模块与包", "chapter": 2, 
     "theory": "模块是Python文件，包是模块的集合。使用import导入，可以简化代码组织。", 
     "code": "import math\nimport random\nfrom datetime import datetime\n\nprint(f'圆周率: {math.pi:.4f}')\nprint(f'平方根: {math.sqrt(16)}')\nprint(f'随机数: {random.randint(1, 100)}')\nprint(f'当前时间: {datetime.now().strftime(\"%H:%M:%S\")}')", 
     "hint": "导入并使用标准库模块"},
    
    # 第三章：实战应用
    {"id": 17, "title": "正则表达式", "chapter": 3, 
     "theory": "re模块提供正则表达式功能，用于字符串匹配、查找、替换。是文本处理的利器。", 
     "code": "import re\n\ntext = '我的邮箱是 test@example.com，电话是 138-1234-5678'\n\n# 匹配邮箱\nemail = re.search(r'[\\w.]+@[\\w.]+', text)\nif email:\n    print(f'找到邮箱: {email.group()}')\n\n# 匹配电话\nphone = re.search(r'\\d{3}-\\d{4}-\\d{4}', text)\nif phone:\n    print(f'找到电话: {phone.group()}')\n\n# 替换\nnew_text = re.sub(r'\\d{3}-\\d{4}-\\d{4}', '***-****-****', text)\nprint(f'替换后: {new_text}')", 
     "hint": "使用正则表达式匹配邮箱和电话"},
    {"id": 18, "title": "网络请求", "chapter": 3, 
     "theory": "requests库用于HTTP请求。可以获取网页数据、调用API接口、下载文件等。", 
     "code": "import requests\n\ntry:\n    response = requests.get('https://api.github.com', timeout=5)\n    print(f'状态码: {response.status_code}')\n    print(f'内容类型: {response.headers.get(\"content-type\")}')\n    \n    # 解析JSON\n    data = response.json()\n    print(f'API文档: {data.get(\"documentation_url\")}')\nexcept requests.RequestException as e:\n    print(f'请求失败: {e}')\nexcept Exception as e:\n    print(f'其他错误: {e}')", 
     "hint": "发送HTTP GET请求并处理响应"},
    {"id": 19, "title": "JSON处理", "chapter": 3, 
     "theory": "json模块用于JSON数据的解析和生成。JSON是数据交换的标准格式，广泛用于Web API。", 
     "code": "import json\n\ndata = {\n    'name': 'Python',\n    'version': 3.12,\n    'features': ['简单', '强大', '优雅'],\n    'popular': True\n}\n\n# 序列化\njson_str = json.dumps(data, ensure_ascii=False, indent=2)\nprint('JSON字符串:')\nprint(json_str)\n\n# 反序列化\nparsed = json.loads(json_str)\nprint(f'\\n解析后:')\nprint(f'名称: {parsed[\"name\"]}')\nprint(f'特性: {parsed[\"features\"]}')", 
     "hint": "JSON序列化和反序列化"},
    {"id": 20, "title": "SQLite数据库", "chapter": 3, 
     "theory": "sqlite3是Python内置的数据库模块。无需额外安装，适合嵌入式应用和原型开发。", 
     "code": "import sqlite3\n\n# 连接内存数据库\nconn = sqlite3.connect(':memory:')\ncursor = conn.cursor()\n\n# 创建表\ncursor.execute('''\n    CREATE TABLE users (\n        id INTEGER PRIMARY KEY,\n        name TEXT NOT NULL,\n        age INTEGER\n    )\n''')\n\n# 插入数据\ncursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', ('Alice', 25))\ncursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', ('Bob', 30))\nconn.commit()\n\n# 查询数据\ncursor.execute('SELECT * FROM users')\nprint('用户数据:')\nfor row in cursor.fetchall():\n    print(f'  ID:{row[0]} 姓名:{row[1]} 年龄:{row[2]}')\n\nconn.close()", 
     "hint": "创建表并插入数据"},
    {"id": 21, "title": "多线程", "chapter": 3, 
     "theory": "threading模块实现多线程。适合IO密集型任务（网络请求、文件读写），不适合CPU密集型任务。", 
     "code": "import threading\nimport time\n\ndef task(name, duration):\n    print(f'[{name}] 开始执行')\n    time.sleep(duration)\n    print(f'[{name}] 执行完成')\n\n# 创建线程\nthreads = []\nfor i in range(3):\n    t = threading.Thread(target=task, args=(f'任务{i+1}', 0.5))\n    threads.append(t)\n    t.start()\n\nprint('主线程继续执行...')\n\n# 等待所有线程完成\nfor t in threads:\n    t.join()\n\nprint('所有任务完成！')", 
     "hint": "创建并运行多线程"},
    {"id": 22, "title": "日期时间", "chapter": 3, 
     "theory": "datetime模块处理日期和时间。支持格式化、计算、时区转换等操作。", 
     "code": "from datetime import datetime, timedelta\n\nnow = datetime.now()\nprint(f'当前时间: {now.strftime(\"%Y-%m-%d %H:%M:%S\")}')\n\n# 时间计算\nfuture = now + timedelta(days=7)\npast = now - timedelta(hours=3)\n\nprint(f'一周后: {future.strftime(\"%Y-%m-%d\")}')\nprint(f'三小时前: {past.strftime(\"%H:%M\")}')\n\n# 解析时间\ntime_str = '2024-01-01 12:00:00'\nparsed = datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')\nprint(f'解析: {parsed}')", 
     "hint": "处理日期时间"},
    {"id": 23, "title": "文件路径", "chapter": 3, 
     "theory": "pathlib提供面向对象的文件路径操作，替代传统的os.path。代码更简洁、跨平台。", 
     "code": "from pathlib import Path\n\n# 当前目录\ncurrent = Path('.')\nprint(f'当前目录: {current.absolute()}')\n\n# 路径拼接\nnew_path = current / 'data' / 'test.txt'\nprint(f'新路径: {new_path}')\n\n# 路径属性\nprint(f'父目录: {new_path.parent}')\nprint(f'文件名: {new_path.name}')\nprint(f'后缀: {new_path.suffix}')\n\n# 查找文件\npy_files = list(current.glob('*.py'))\nprint(f'Python文件: {len(py_files)}个')", 
     "hint": "使用pathlib操作路径"},
    {"id": 24, "title": "虚拟环境", "chapter": 3, 
     "theory": "venv模块创建隔离的Python环境。避免包冲突，是Python开发的最佳实践。", 
     "code": "# 虚拟环境操作（命令行）\ncommands = [\n    'python -m venv myenv',\n    'myenv\\\\Scripts\\\\activate',  # Windows\n    '# source myenv/bin/activate',    # Linux/Mac\n    'pip install requests',\n    'pip list',\n    'deactivate'\n]\n\nprint('虚拟环境常用命令:')\nfor cmd in commands:\n    print(f'  $ {cmd}')\n\nprint('\\n虚拟环境的好处:')\nprint('  1. 隔离项目依赖')\nprint('  2. 避免包版本冲突')\nprint('  3. 便于项目部署')", 
     "hint": "了解虚拟环境命令"},
]

# 成就系统
ACHIEVEMENTS = [
    {"id": "first_step", "name": "第一步", "desc": "完成第1课", "icon": "🎯"},
    {"id": "chapter1_complete", "name": "基础入门", "desc": "完成第一章", "icon": "📚"},
    {"id": "chapter2_complete", "name": "进阶之路", "desc": "完成第二章", "icon": "🚀"},
    {"id": "chapter3_complete", "name": "实战高手", "desc": "完成第三章", "icon": "🏆"},
    {"id": "half_way", "name": "半程马拉松", "desc": "完成12课", "icon": "🎖️"},
    {"id": "all_complete", "name": "Python大师", "desc": "完成全部24课", "icon": "👑"},
    {"id": "coder", "name": "代码达人", "desc": "运行代码10次", "icon": "💻"},
    {"id": "explorer", "name": "探索者", "desc": "浏览20课", "icon": "🔍"},
]

class ThemedWidget:
    """主题支持混入类"""
    def get_theme_color(self, color_name):
        app = App.get_running_app()
        theme = THEMES.get(app.theme, THEMES['light'])
        return theme.get(color_name, (0.5, 0.5, 0.5, 1))

class CourseButton(Button, ThemedWidget):
    """课程按钮"""
    def __init__(self, course, completed=False, **kwargs):
        super().__init__(**kwargs)
        self.course = course
        self.completed = completed
        self.update_style()
        self.size_hint_y = None
        self.height = 70
    
    def update_style(self):
        if self.completed:
            self.text = f"✅ {self.course['id']}. {self.course['title']}"
            self.background_color = self.get_theme_color('success')
        else:
            self.text = f"📖 {self.course['id']}. {self.course['title']}"
            self.background_color = self.get_theme_color('primary')

class CourseScreen(Screen, ThemedWidget):
    """课程学习界面"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.current_course = None
        self.build_ui()
    
    def build_ui(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # 标题栏
        title_box = BoxLayout(size_hint_y=None, height=50, spacing=10)
        self.back_btn = Button(text='◀ 返回', size_hint_x=None, width=80)
        self.back_btn.bind(on_press=self.go_back)
        self.title_label = Label(text='课程学习', font_size=18, bold=True)
        title_box.add_widget(self.back_btn)
        title_box.add_widget(self.title_label)
        layout.add_widget(title_box)
        
        # 课程内容区域
        scroll = ScrollView()
        content = BoxLayout(orientation='vertical', size_hint_y=None, padding=10, spacing=10)
        content.bind(minimum_height=content.setter('height'))
        
        # 理论部分
        theory_label = Label(
            text='📖 理论讲解',
            size_hint_y=None,
            height=30,
            bold=True,
            color=self.get_theme_color('primary')
        )
        content.add_widget(theory_label)
        
        self.theory_text = Label(
            text='',
            size_hint_y=None,
            text_size=(Window.width - 40, None),
            halign='left',
            valign='top',
            color=self.get_theme_color('text')
        )
        self.theory_text.bind(texture_size=self.theory_text.setter('size'))
        content.add_widget(self.theory_text)
        
        # 代码部分
        code_label = Label(
            text='💻 示例代码',
            size_hint_y=None,
            height=30,
            bold=True,
            color=self.get_theme_color('warning')
        )
        content.add_widget(code_label)
        
        self.code_input = TextInput(
            multiline=True,
            size_hint_y=None,
            height=250,
            font_size=13,
            background_color=self.get_theme_color('code_bg'),
            foreground_color=self.get_theme_color('code_text'),
            padding=10
        )
        content.add_widget(self.code_input)
        
        # 按钮区域
        btn_box = BoxLayout(size_hint_y=None, height=50, spacing=10)
        self.run_btn = Button(text='▶ 运行', background_color=self.get_theme_color('success'))
        self.run_btn.bind(on_press=self.run_code)
        self.reset_btn = Button(text='↺ 重置', background_color=self.get_theme_color('warning'))
        self.reset_btn.bind(on_press=self.reset_code)
        self.complete_btn = Button(text='✓ 完成', background_color=self.get_theme_color('primary'))
        self.complete_btn.bind(on_press=self.complete_course)
        
        btn_box.add_widget(self.run_btn)
        btn_box.add_widget(self.reset_btn)
        btn_box.add_widget(self.complete_btn)
        content.add_widget(btn_box)
        
        # 输出区域
        output_label = Label(
            text='📤 运行结果',
            size_hint_y=None,
            height=30,
            bold=True,
            color=self.get_theme_color('success')
        )
        content.add_widget(output_label)
        
        self.output_text = TextInput(
            multiline=True,
            size_hint_y=None,
            height=150,
            readonly=True,
            background_color=self.get_theme_color('code_bg'),
            foreground_color=self.get_theme_color('code_text'),
            font_size=12
        )
        content.add_widget(self.output_text)
        
        scroll.add_widget(content)
        layout.add_widget(scroll)
        
        self.add_widget(layout)
    
    def load_course(self, course):
        self.current_course = course
        self.title_label.text = f"第{course['id']}课"
        self.theory_text.text = course['theory']
        self.code_input.text = course['code']
        self.output_text.text = ''
        
        # 增加浏览计数
        app = App.get_running_app()
        app.view_count += 1
        app.check_achievements()
        app.save_progress()
    
    def go_back(self, instance):
        self.manager.current = 'menu'
    
    def run_code(self, instance):
        code = self.code_input.text
        output = []
        
        try:
            # 捕获print输出
            old_stdout = sys.stdout
            sys.stdout = io.StringIO()
            
            # 执行代码
            exec(code, {"__builtins__": __builtins__})
            
            # 获取输出
            result = sys.stdout.getvalue()
            sys.stdout = old_stdout
            
            self.output_text.text = result or '✅ 代码执行成功（无输出）'
            
            # 增加运行计数
            app = App.get_running_app()
            app.run_count += 1
            app.check_achievements()
            app.save_progress()
            
        except Exception as e:
            sys.stdout = old_stdout
            self.output_text.text = f'❌ 错误: {str(e)}'
    
    def reset_code(self, instance):
        if self.current_course:
            self.code_input.text = self.current_course['code']
            self.output_text.text = ''
    
    def complete_course(self, instance):
        if self.current_course:
            app = App.get_running_app()
            app.complete_course(self.current_course['id'])
            self.output_text.text = '🎉 恭喜完成本课程！'
            
            # 检查是否解锁新成就
            new_achievements = app.check_achievements()
            if new_achievements:
                self.output_text.text += f'\n🏆 解锁成就: {new_achievements[0]["name"]}'

class MenuScreen(Screen, ThemedWidget):
    """主菜单界面"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.build_ui()
    
    def build_ui(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # 标题
        title = Label(
            text='🐍 Python学习助手',
            font_size=26,
            bold=True,
            size_hint_y=None,
            height=50,
            color=self.get_theme_color('primary')
        )
        layout.add_widget(title)
        
        # 统计信息
        self.stats_label = Label(
            text='',
            size_hint_y=None,
            height=30,
            font_size=14,
            color=self.get_theme_color('text')
        )
        layout.add_widget(self.stats_label)
        
        # 章节标签页
        self.chapter_tabs = BoxLayout(size_hint_y=None, height=40, spacing=5)
        chapters = ['全部', '第一章', '第二章', '第三章']
        for i, name in enumerate(chapters):
            btn = Button(
                text=name,
                background_color=self.get_theme_color('primary')
            )
            btn.bind(on_press=lambda x, c=i: self.filter_chapter(c))
            self.chapter_tabs.add_widget(btn)
        layout.add_widget(self.chapter_tabs)
        
        # 课程列表
        scroll = ScrollView()
        self.course_list = GridLayout(cols=1, spacing=5, size_hint_y=None, padding=10)
        self.course_list.bind(minimum_height=self.course_list.setter('height'))
        scroll.add_widget(self.course_list)
        layout.add_widget(scroll)
        
        # 底部按钮
        bottom_box = BoxLayout(size_hint_y=None, height=50, spacing=10)
        achievements_btn = Button(text='🏆 成就', background_color=self.get_theme_color('warning'))
        achievements_btn.bind(on_press=self.show_achievements)
        stats_btn = Button(text='📊 统计', background_color=self.get_theme_color('success'))
        stats_btn.bind(on_press=self.show_stats)
        theme_btn = Button(text='🌓 主题', background_color=self.get_theme_color('primary'))
        theme_btn.bind(on_press=self.toggle_theme)
        
        bottom_box.add_widget(achievements_btn)
        bottom_box.add_widget(stats_btn)
        bottom_box.add_widget(theme_btn)
        layout.add_widget(bottom_box)
        
        self.add_widget(layout)
        self.load_courses()
    
    def load_courses(self, chapter=0):
        self.course_list.clear_widgets()
        app = App.get_running_app()
        
        for course in COURSES:
            if chapter == 0 or course['chapter'] == chapter:
                completed = course['id'] in app.completed_courses
                btn = CourseButton(course, completed)
                btn.bind(on_press=lambda x, c=course: self.open_course(c))
                self.course_list.add_widget(btn)
        
        self.update_stats()
    
    def filter_chapter(self, chapter):
        self.load_courses(chapter)
    
    def open_course(self, course):
        course_screen = self.manager.get_screen('course')
        course_screen.load_course(course)
        self.manager.current = 'course'
    
    def update_stats(self):
        app = App.get_running_app()
        total = len(COURSES)
        completed = len(app.completed_courses)
        progress = (completed / total) * 100
        self.stats_label.text = f'进度: {completed}/{total} 课 ({progress:.1f}%)'
    
    def toggle_theme(self, instance):
        app = App.get_running_app()
        app.theme = 'dark' if app.theme == 'light' else 'light'
        app.save_progress()
        
        # 刷新界面
        self.load_courses()
        
        # 显示提示
        popup = Popup(
            title='主题切换',
            content=Label(text=f'已切换到{"深色" if app.theme == "dark" else "浅色"}主题'),
            size_hint=(0.6, 0.2)
        )
        popup.open()
        Clock.schedule_once(lambda dt: popup.dismiss(), 1)
    
    def show_achievements(self, instance):
        app = App.get_running_app()
        content = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        scroll = ScrollView()
        achievements_list = GridLayout(cols=1, spacing=5, size_hint_y=None, padding=10)
        achievements_list.bind(minimum_height=achievements_list.setter('height'))
        
        for ach in ACHIEVEMENTS:
            unlocked = ach['id'] in app.achievements
            color = self.get_theme_color('success') if unlocked else (0.5, 0.5, 0.5, 1)
            btn = Button(
                text=f"{ach['icon']} {ach['name']}\n{ach['desc']}{' ✅' if unlocked else ' 🔒'}",
                size_hint_y=None,
                height=60,
                background_color=color
            )
            achievements_list.add_widget(btn)
        
        scroll.add_widget(achievements_list)
        content.add_widget(scroll)
        
        close_btn = Button(text='关闭', size_hint_y=None, height=40)
        content.add_widget(close_btn)
        
        popup = Popup(title='🏆 成就系统', content=content, size_hint=(0.9, 0.8))
        close_btn.bind(on_press=popup.dismiss)
        popup.open()
    
    def show_stats(self, instance):
        app = App.get_running_app()
        content = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        stats_text = f"""
📊 学习统计

已完成课程: {len(app.completed_courses)}/24
完成率: {len(app.completed_courses)/24*100:.1f}%

代码运行次数: {app.run_count}
课程浏览次数: {app.view_count}

已获得成就: {len(app.achievements)}/8

当前主题: {'深色' if app.theme == 'dark' else '浅色'}
        """
        
        label = Label(
            text=stats_text,
            font_size=16,
            color=self.get_theme_color('text')
        )
        content.add_widget(label)
        
        close_btn = Button(text='关闭', size_hint_y=None, height=40)
        content.add_widget(close_btn)
        
        popup = Popup(title='学习统计', content=content, size_hint=(0.8, 0.6))
        close_btn.bind(on_press=popup.dismiss)
        popup.open()
    
    def on_enter(self):
        self.load_courses()

class PythonLearnApp(App):
    """主应用"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.completed_courses = set()
        self.achievements = set()
        self.run_count = 0
        self.view_count = 0
        self.theme = 'light'
        self.load_progress()
    
    def build(self):
        # 设置主题背景
        Window.clearcolor = THEMES[self.theme]['bg']
        
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(CourseScreen(name='course'))
        return sm
    
    def complete_course(self, course_id):
        self.completed_courses.add(course_id)
        self.check_achievements()
        self.save_progress()
    
    def check_achievements(self):
        new_achievements = []
        
        # 检查各个成就
        checks = [
            ('first_step', lambda: 1 in self.completed_courses),
            ('chapter1_complete', lambda: all(c['id'] in self.completed_courses for c in COURSES if c['chapter'] == 1)),
            ('chapter2_complete', lambda: all(c['id'] in self.completed_courses for c in COURSES if c['chapter'] == 2)),
            ('chapter3_complete', lambda: all(c['id'] in self.completed_courses for c in COURSES if c['chapter'] == 3)),
            ('half_way', lambda: len(self.completed_courses) >= 12),
            ('all_complete', lambda: len(self.completed_courses) >= 24),
            ('coder', lambda: self.run_count >= 10),
            ('explorer', lambda: self.view_count >= 20),
        ]
        
        for ach_id, check_func in checks:
            if ach_id not in self.achievements and check_func():
                self.achievements.add(ach_id)
                # 找到成就信息
                for ach in ACHIEVEMENTS:
                    if ach['id'] == ach_id:
                        new_achievements.append(ach)
                        break
        
        return new_achievements
    
    def save_progress(self):
        data = {
            'completed_courses': list(self.completed_courses),
            'achievements': list(self.achievements),
            'run_count': self.run_count,
            'view_count': self.view_count,
            'theme': self.theme
        }
        try:
            # 使用应用数据目录
            if platform == 'android':
                from android.storage import app_storage_path
                storage_dir = app_storage_path()
            else:
                storage_dir = os.path.dirname(os.path.abspath(__file__))
            
            filepath = os.path.join(storage_dir, 'progress.json')
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False)
        except:
            pass
    
    def load_progress(self):
        try:
            if platform == 'android':
                from android.storage import app_storage_path
                storage_dir = app_storage_path()
            else:
                storage_dir = os.path.dirname(os.path.abspath(__file__))
            
            filepath = os.path.join(storage_dir, 'progress.json')
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.completed_courses = set(data.get('completed_courses', []))
                self.achievements = set(data.get('achievements', []))
                self.run_count = data.get('run_count', 0)
                self.view_count = data.get('view_count', 0)
                self.theme = data.get('theme', 'light')
        except:
            pass

if __name__ == '__main__':
    PythonLearnApp().run()
