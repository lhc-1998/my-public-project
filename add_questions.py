# -*- coding: utf-8 -*-
from database import SessionLocal
from models import Question
import json

db = SessionLocal()

# ============ 从讲义中提取的题目 ============

# ----- Python基础题目 -----
python_questions = [
    # Day01 Python基础
    {'category': 'Python', 'type': 'single', 'content': 'Python中用于输出到控制台的函数是？', 'options': json.dumps(['A. echo()', 'B. print()', 'C. printf()', 'D. console()']), 'answer': 'B', 'analysis': 'print()是Python的标准输出函数', 'difficulty': 1},
    {'category': 'Python', 'type': 'single', 'content': 'Python的基本数据类型不包括以下哪个？', 'options': json.dumps(['A. int（整数）', 'B. float（浮点数）', 'C. array（数组）', 'D. str（字符串）']), 'answer': 'C', 'analysis': 'Python基本数据类型包括int、float、str、bool；array需要导入numpy等库才能使用', 'difficulty': 1},
    {'category': 'Python', 'type': 'single', 'content': 'Python列表的索引从哪个数字开始？', 'options': json.dumps(['A. 0', 'B. 1', 'C. -1', 'D. 由开发者指定']), 'answer': 'A', 'analysis': 'Python列表的索引从0开始，第一个元素索引为0', 'difficulty': 1},
    {'category': 'Python', 'type': 'single', 'content': 'Python中以下哪个是不可变数据类型？', 'options': json.dumps(['A. list', 'B. dict', 'C. tuple', 'D. set']), 'answer': 'C', 'analysis': 'tuple是元组，创建后不能修改；list、dict、set都是可变的', 'difficulty': 1},
    {'category': 'Python', 'type': 'single', 'content': '用于检测数据类型的方法是？', 'options': json.dumps(['A. typeof()', 'B. type()', 'C. datatype()', 'D. check()']), 'answer': 'B', 'analysis': '使用type(数据)可以检测数据类型', 'difficulty': 1},
    {'category': 'Python', 'type': 'single', 'content': 'input()函数获取的输入默认是什么类型？', 'options': json.dumps(['A. int', 'B. float', 'C. str（字符串）', 'D. bool']), 'answer': 'C', 'analysis': 'input()函数获取的所有输入默认都是字符串类型，需要转换才能进行数值计算', 'difficulty': 1},
    {'category': 'Python', 'type': 'single', 'content': 'Python中=和==的区别是？', 'options': json.dumps(['A. =是赋值，==是相等判断', 'B. 两者没有区别', 'C. =是判断，==是赋值', 'D. =用于字符串，==用于数字']), 'answer': 'A', 'analysis': '=用于赋值，==用于判断是否相等', 'difficulty': 1},
    {'category': 'Python', 'type': 'single', 'content': 'Python中字符串使用+号的作用是？', 'options': json.dumps(['A. 数字相加和字符串拼接', 'B. 只能拼接字符串', 'C. 只能做数字加法', 'D. 做减法']), 'answer': 'A', 'analysis': '+运算符的作用取决于数据类型：数字相加，字符串拼接', 'difficulty': 1},
    {'category': 'Python', 'type': 'single', 'content': 'Python变量的命名规则不包括？', 'options': json.dumps(['A. 不能使用关键字', 'B. 只能以字母、数字、下划线组成', 'C. 数字不能开头', 'D. 可以使用$符号']), 'answer': 'D', 'analysis': '变量名只能包含字母、数字、下划线，$不是合法字符', 'difficulty': 1},
    {'category': 'Python', 'type': 'single', 'content': 'Python中常量的命名约定是？', 'options': json.dumps(['A. 全部大写', 'B. 全部小写', 'C. 首字母大写', 'D. 无约定']), 'answer': 'A', 'analysis': 'Python使用全大写字母和下划线命名表示常量，这是约定俗成的惯例', 'difficulty': 1},
    {'category': 'Python', 'type': 'single', 'content': 'f-string格式化的语法是？', 'options': json.dumps(["A. '格式{变量名}'", "B. f'格式{变量名}'", "C. format('格式{变量名}')", "D. print('{变量名}')"]), 'answer': 'B', 'analysis': 'f-string在字符串前加f或F，用{变量名}嵌入变量或表达式', 'difficulty': 1},
    {'category': 'Python', 'type': 'single', 'content': '转义字符\\n表示什么？', 'options': json.dumps(['A. 换行符', 'B. 制表符', 'C. 退格符', 'D. 回车符']), 'answer': 'A', 'analysis': '\\n是换行符，让后续内容从新的一行开始', 'difficulty': 1},
    {'category': 'Python', 'type': 'single', 'content': 'Python中10 // 3的结果是？', 'options': json.dumps(['A. 3.33', 'B. 3', 'C. 4', 'D. 3.0']), 'answer': 'B', 'analysis': '//是整数除法，结果取整，10//3=3', 'difficulty': 1},
    {'category': 'Python', 'type': 'single', 'content': 'Python中10 % 3的结果是？', 'options': json.dumps(['A. 3', 'B. 1', 'C. 0', 'D. 3.33']), 'answer': 'B', 'analysis': '%是取余运算符，10%3=1（10除以3余1）', 'difficulty': 1},
    {'category': 'Python', 'type': 'judge', 'content': 'Python使用缩进来划分代码块。', 'answer': 'TRUE', 'analysis': 'Python强制使用缩进（通常4个空格）来表示代码层级关系', 'difficulty': 1},

    # Day02 流程控制
    {'category': 'Python', 'type': 'single', 'content': 'Python中and运算符的特点是？', 'options': json.dumps(['A. 两边都为True结果才为True', 'B. 一边为True结果就为True', 'C. 两边都为False结果才为True', 'D. 相反结果']), 'answer': 'A', 'analysis': 'and是与运算，两边都为True结果才为True（一假则假）', 'difficulty': 1},
    {'category': 'Python', 'type': 'single', 'content': 'Python中or运算符的特点是？', 'options': json.dumps(['A. 一边为True结果就为True', 'B. 两边都为True结果才为True', 'C. 两边都为False结果才为True', 'D. 取反结果']), 'answer': 'A', 'analysis': 'or是或运算，一边为True结果就为True（一真则真）', 'difficulty': 1},
    {'category': 'Python', 'type': 'single', 'content': 'Python中not运算符的作用是？', 'options': json.dumps(['A. 取反，True变False，False变True', 'B. 保持不变', 'C. 求和', 'D. 乘以-1']), 'answer': 'A', 'analysis': 'not是非运算，对布尔值取反', 'difficulty': 1},
    {'category': 'Python', 'type': 'single', 'content': 'if-elif-else结构中，哪个条件满足会执行对应代码块后跳出？', 'options': json.dumps(['A. 第一个满足的条件', 'B. 最后一个条件', 'C. 所有条件', 'D. 没有条件']), 'answer': 'A', 'analysis': '程序从上往下判断，满足某个条件执行完代码块后会跳出整个if结构', 'difficulty': 1},
    {'category': 'Python', 'type': 'single', 'content': 'while循环的特点是？', 'options': json.dumps(['A. 只要条件成立，就一直重复执行', 'B. 只执行一次', 'C. 执行固定次数', 'D. 从后往前执行']), 'answer': 'A', 'analysis': 'while循环在条件为True时重复执行，需要防止死循环', 'difficulty': 1},
    {'category': 'Python', 'type': 'single', 'content': 'range(5)生成的序列是？', 'options': json.dumps(['A. 0,1,2,3,4', 'B. 1,2,3,4,5', 'C. 0,1,2,3,4,5', 'D. 1,2,3,4']), 'answer': 'A', 'analysis': 'range()包头不包尾，从0开始，range(5)生成0-4', 'difficulty': 1},
    {'category': 'Python', 'type': 'single', 'content': 'range(1,6,2)生成的序列是？', 'options': json.dumps(['A. 1,3,5', 'B. 1,2,3,4,5', 'C. 2,4', 'D. 1,3']), 'answer': 'A', 'analysis': 'range(起始,结束,步长)，包头不包尾，1,6,2表示从1开始到6，步长2，结果1,3,5', 'difficulty': 2},
    {'category': 'Python', 'type': 'single', 'content': 'break语句的作用是？', 'options': json.dumps(['A. 立即终止整个循环', 'B. 跳过当前一次循环', 'C. 继续执行循环', 'D. 返回值']), 'answer': 'A', 'analysis': 'break用于立即终止整个循环，执行循环后面的代码', 'difficulty': 1},
    {'category': 'Python', 'type': 'single', 'content': 'continue语句的作用是？', 'options': json.dumps(['A. 跳过当前一次循环，继续下一次', 'B. 终止整个循环', 'C. 退出程序', 'D. 返回函数值']), 'answer': 'A', 'analysis': 'continue跳过本次循环剩下的代码，直接开始下一次循环', 'difficulty': 1},
    {'category': 'Python', 'type': 'single', 'content': 'Python的三元运算语法是？', 'options': json.dumps(['A. 代码1 if 条件 else 代码2', 'B. if 条件 then 代码1 else 代码2', 'C. 条件 ? 代码1 : 代码2', 'D. if 代码1 else 代码2']), 'answer': 'A', 'analysis': '三元运算语法：代码1 if 条件 else 代码2，条件为True执行代码1，否则执行代码2', 'difficulty': 1},
    {'category': 'Python', 'type': 'single', 'content': 'random.randint(1,10)生成的随机数范围是？', 'options': json.dumps(['A. 1到10，包含两端', 'B. 1到10，不包含10', 'C. 0到9', 'D. 1到9']), 'answer': 'A', 'analysis': 'random.randint(a,b)生成a到b之间的随机整数，包含两端', 'difficulty': 1},
    {'category': 'Python', 'type': 'judge', 'content': 'for循环只能用于遍历序列，不能用于固定次数循环。', 'answer': 'FALSE', 'analysis': 'for循环配合range()可以用于固定次数循环', 'difficulty': 1},
    {'category': 'Python', 'type': 'judge', 'content': '在Python中，字符串是不可变的。', 'answer': 'TRUE', 'analysis': '字符串创建后不能直接修改，必须创建新的字符串', 'difficulty': 1},

    # Day03 数据容器
    {'category': 'Python', 'type': 'single', 'content': '列表的哪个方法用于在末尾添加元素？', 'options': json.dumps(['A. append()', 'B. insert()', 'C. add()', 'D. push()']), 'answer': 'A', 'analysis': 'list.append(元素)在列表末尾添加一个元素', 'difficulty': 1},
    {'category': 'Python', 'type': 'single', 'content': '列表中负数索引-1表示？', 'options': json.dumps(['A. 最后一个元素', 'B. 第一个元素', 'C. 倒数第二个', 'D. 无效索引']), 'answer': 'A', 'analysis': '-1表示访问最后一个元素，-2表示倒数第二个', 'difficulty': 1},
    {'category': 'Python', 'type': 'single', 'content': '获取列表长度的函数是？', 'options': json.dumps(['A. len()', 'B. length()', 'C. size()', 'D. count()']), 'answer': 'A', 'analysis': 'len(列表名)获取列表的数据个数', 'difficulty': 1},
    {'category': 'Python', 'type': 'single', 'content': '字典使用什么访问值？', 'options': json.dumps(['A. 键（key）', 'B. 下标索引', 'C. 顺序位置', 'D. 数字']), 'answer': 'A', 'analysis': '字典通过key获取value，如dict["name"]', 'difficulty': 1},
    {'category': 'Python', 'type': 'single', 'content': '集合的特点是？', 'options': json.dumps(['A. 无序、不允许重复', 'B. 有序、允许重复', 'C. 有序、不允许重复', 'D. 无序、允许重复']), 'answer': 'A', 'analysis': '集合使用{}定义，无序且不允许有重复元素', 'difficulty': 1},
    {'category': 'Python', 'type': 'single', 'content': '元组和列表的主要区别是？', 'options': json.dumps(['A. 元组不可变，列表可变', 'B. 列表不可变，元组可变', 'C. 两者完全相同', 'D. 语法不同，功能相同']), 'answer': 'A', 'analysis': '元组使用()定义，创建后不能修改；列表使用[]定义，可以增删改', 'difficulty': 1},
    {'category': 'Python', 'type': 'single', 'content': '字符串split()方法的作用是？', 'options': json.dumps(['A. 把字符串切成列表', 'B. 拼接字符串', 'C. 替换字符串', 'D. 查找字符串']), 'answer': 'A', 'analysis': 'split()把字符串按分隔符切成列表，如"a,b".split(",")得到["a","b"]', 'difficulty': 1},
    {'category': 'Python', 'type': 'single', 'content': '字符串join()方法的作用是？', 'options': json.dumps(['A. 把列表拼成字符串', 'B. 切割字符串', 'C. 替换字符串', 'D. 复制字符串']), 'answer': 'A', 'analysis': 'join()把列表拼成字符串，如"-".join(["a","b"])得到"a-b"', 'difficulty': 1},
    {'category': 'Python', 'type': 'single', 'content': '列表切片nums[1:4]的结果包含下标为几的元素？', 'options': json.dumps(['A. 1,2,3', 'B. 1,2,3,4', 'C. 0,1,2,3', 'D. 2,3,4']), 'answer': 'A', 'analysis': '切片包头不包尾，nums[1:4]获取索引1、2、3的元素', 'difficulty': 1},
    {'category': 'Python', 'type': 'single', 'content': '列表推导式[x**2 for x in range(1,5)]的结果是？', 'options': json.dumps(['A. [1, 4, 9, 16]', 'B. [0, 1, 4, 9, 16]', 'C. [2, 4, 6, 8]', 'D. [1, 2, 3, 4]']), 'answer': 'A', 'analysis': '列表推导式对range(1,5)即1,2,3,4进行平方运算，结果[1,4,9,16]', 'difficulty': 2},
    {'category': 'Python', 'type': 'single', 'content': 'isdigit()方法的作用是？', 'options': json.dumps(['A. 判断字符串是否由数字组成', 'B. 转换为数字', 'C. 计算位数', 'D. 求和']), 'answer': 'A', 'analysis': 'isdigit()判断字符串是否全部由数字组成', 'difficulty': 1},
    {'category': 'Python', 'type': 'judge', 'content': '字典可以通过下标索引访问元素。', 'answer': 'FALSE', 'analysis': '字典通过key访问值，不是通过下标索引', 'difficulty': 1},

    # Day04 函数
    {'category': 'Python', 'type': 'single', 'content': '定义函数使用的关键字是？', 'options': json.dumps(['A. def', 'B. function', 'C. func', 'D. define']), 'answer': 'A', 'analysis': 'Python使用def关键字定义函数', 'difficulty': 1},
    {'category': 'Python', 'type': 'single', 'content': '函数返回值使用哪个关键字？', 'options': json.dumps(['A. return', 'B. return ', 'C. get', 'D. output']), 'answer': 'A', 'analysis': '使用return关键字返回函数结果', 'difficulty': 1},
    {'category': 'Python', 'type': 'single', 'content': '如果函数没有return语句，默认返回什么？', 'options': json.dumps(['A. None', 'B. 0', 'C. 空字符串', 'D. False']), 'answer': 'A', 'analysis': '函数如果没有return数据，默认返回值是None', 'difficulty': 1},
    {'category': 'Python', 'type': 'single', 'content': '在函数内部修改全局变量，需要使用什么关键字？', 'options': json.dumps(['A. global', 'B. local', 'C. nonlocal', 'D. static']), 'answer': 'A', 'analysis': '在函数内部修改全局变量，需要先使用global声明', 'difficulty': 1},
    {'category': 'Python', 'type': 'single', 'content': '*args的作用是？', 'options': json.dumps(['A. 接收多余的位置参数，打包成元组', 'B. 接收关键字参数', 'C. 接收所有参数', 'D. 返回参数个数']), 'answer': 'A', 'analysis': '*args接收所有多余的位置参数，打包成元组', 'difficulty': 2},
    {'category': 'Python', 'type': 'single', 'content': '**kwargs的作用是？', 'options': json.dumps(['A. 接收多余的关键字参数，打包成字典', 'B. 接收位置参数', 'C. 返回关键字参数', 'D. 传递参数']), 'answer': 'A', 'analysis': '**kwargs接收所有多余的关键字参数，打包成字典', 'difficulty': 2},
    {'category': 'Python', 'type': 'single', 'content': 'lambda表达式的语法是？', 'options': json.dumps(['A. lambda 参数: 结果', 'B. lambda (参数) {结果}', 'C. lambda 参数 -> 结果', 'D. lambda (参数) -> 结果']), 'answer': 'A', 'analysis': 'lambda表达式语法：lambda 参数: 结果，只能有一行代码', 'difficulty': 2},
    {'category': 'Python', 'type': 'single', 'content': 'Python关键字参数的特点是？', 'options': json.dumps(['A. 指名道姓，顺序可乱', 'B. 必须按顺序', 'C. 不能有默认值', 'D. 只能是数字']), 'answer': 'A', 'analysis': '关键字参数通过参数名指定，顺序可以任意', 'difficulty': 1},
    {'category': 'Python', 'type': 'judge', 'content': 'Python支持多继承。', 'answer': 'TRUE', 'analysis': 'Python允许多继承，一个类可以继承多个父类', 'difficulty': 1},
    {'category': 'Python', 'type': 'judge', 'content': '默认参数必须放在位置参数前面。', 'answer': 'FALSE', 'analysis': '默认参数通常放在最后，位置参数在前', 'difficulty': 1},

    # Day05 文件操作与异常处理
    {'category': 'Python', 'type': 'single', 'content': '打开文件进行写入操作，使用什么模式？', 'options': json.dumps(['A. w', 'B. r', 'C. a', 'D. x']), 'answer': 'A', 'analysis': '"w"模式是写入模式，文件不存在则创建，存在则清空内容', 'difficulty': 1},
    {'category': 'Python', 'type': 'single', 'content': '打开文件进行追加写入，使用什么模式？', 'options': json.dumps(['A. a', 'B. w', 'C. r', 'D. x']), 'answer': 'A', 'analysis': '"a"模式是追加模式，在文件末尾追加内容', 'difficulty': 1},
    {'category': 'Python', 'type': 'single', 'content': '文件读取操作的推荐写法是？', 'options': json.dumps(['A. with open() as f:', 'B. open()后手动close()', 'C. 只用open()', 'D. readline()']), 'answer': 'A', 'analysis': 'with open()是安全的写法，文件会自动关闭', 'difficulty': 1},
    {'category': 'Python', 'type': 'single', 'content': 'JSON.dumps()的作用是？', 'options': json.dumps(['A. 把Python数据转换为JSON字符串', 'B. 读取JSON文件', 'C. 解析JSON', 'D. 写入文件']), 'answer': 'A', 'analysis': 'json.dumps()将Python数据序列化为JSON字符串', 'difficulty': 1},
    {'category': 'Python', 'type': 'single', 'content': 'JSON.loads()的作用是？', 'options': json.dumps(['A. 把JSON字符串转换为Python数据', 'B. 写入JSON', 'C. 创建JSON', 'D. 保存文件']), 'answer': 'A', 'analysis': 'json.loads()将JSON字符串反序列化为Python数据', 'difficulty': 1},
    {'category': 'Python', 'type': 'single', 'content': '异常处理的语法是？', 'options': json.dumps(['A. try...except', 'B. if...else', 'C. try...catch', 'D. error...handle']), 'answer': 'A', 'analysis': 'Python使用try...except进行异常处理', 'difficulty': 1},
    {'category': 'Python', 'type': 'single', 'content': 'FileNotFoundError异常表示什么？', 'options': json.dumps(['A. 文件不存在', 'B. 文件已存在', 'C. 文件损坏', 'D. 权限不足']), 'answer': 'A', 'analysis': 'FileNotFoundError表示试图读取一个不存在的文件', 'difficulty': 1},
    {'category': 'Python', 'type': 'single', 'content': '相对路径中../表示什么？', 'options': json.dumps(['A. 上一级目录', 'B. 当前目录', 'C. 根目录', 'D. 子目录']), 'answer': 'A', 'analysis': '../表示上一级目录，./表示当前目录', 'difficulty': 1},
    {'category': 'Python', 'type': 'judge', 'content': '用w模式打开已有内容的文件，原内容会被清空。', 'answer': 'TRUE', 'analysis': 'w模式会清空文件原有内容后从头写入', 'difficulty': 1},

    # Day06 面向对象
    {'category': 'Python', 'type': 'single', 'content': '类是什么？', 'options': json.dumps(['A. 对象的模板/图纸', 'B. 具体的对象', 'C. 函数的集合', 'D. 数据类型']), 'answer': 'A', 'analysis': '类是对象的模板，定义对象的属性和方法', 'difficulty': 1},
    {'category': 'Python', 'type': 'single', 'content': '创建类实例（对象）使用的是？', 'options': json.dumps(['A. 类名()', 'B. new 类名', 'C. create 类名', 'D. init 类名']), 'answer': 'A', 'analysis': '使用类名()创建类的实例对象', 'difficulty': 1},
    {'category': 'Python', 'type': 'single', 'content': '__init__方法的作用是？', 'options': json.dumps(['A. 初始化对象属性（构造函数）', 'B. 销毁对象', 'C. 打印对象', 'D. 返回值']), 'answer': 'A', 'analysis': '__init__在创建对象时自动调用，用于初始化属性', 'difficulty': 1},
    {'category': 'Python', 'type': 'single', 'content': 'self关键字代表什么？', 'options': json.dumps(['A. 当前对象自己', 'B. 类本身', 'C. 全局对象', 'D. 父类对象']), 'answer': 'A', 'analysis': 'self代表当前对象自己，用于访问自己的属性和方法', 'difficulty': 1},
    {'category': 'Python', 'type': 'single', 'content': '__str__方法的作用是？', 'options': json.dumps(['A. 定义print对象的输出格式', 'B. 初始化对象', 'C. 销毁对象', 'D. 比较对象']), 'answer': 'A', 'analysis': '__str__定义print对象时的输出格式，必须返回字符串', 'difficulty': 1},
    {'category': 'Python', 'type': 'single', 'content': '私有属性的命名规范是？', 'options': json.dumps(['A. 以双下划线__开头', 'B. 以单下划线_开头', 'C. 全大写', 'D. 无特殊要求']), 'answer': 'A', 'analysis': '私有属性以双下划线__开头，外部无法直接访问', 'difficulty': 1},
    {'category': 'Python', 'type': 'single', 'content': '继承的语法是？', 'options': json.dumps(['A. class 子类(父类):', 'B. class 子类 extends 父类', 'C. class 子类:inherit 父类', 'D. class 子类 from 父类']), 'answer': 'A', 'analysis': 'Python继承语法：class 子类(父类):', 'difficulty': 1},
    {'category': 'Python', 'type': 'single', 'content': '如果类定义时不指定父类，默认继承自？', 'options': json.dumps(['A. object', 'B. None', 'C. Base', 'D. Parent']), 'answer': 'A', 'analysis': 'Python3中，如果不写继承，默认继承自object（所有类的根类）', 'difficulty': 1},
    {'category': 'Python', 'type': 'single', 'content': 'super()函数的作用是？', 'options': json.dumps(['A. 调用父类的方法', 'B. 创建父类对象', 'C. 获取父类名称', 'D. 判断继承关系']), 'answer': 'A', 'analysis': 'super()可以显式调用父类的方法', 'difficulty': 2},
    {'category': 'Python', 'type': 'single', 'content': '多态的概念是？', 'options': json.dumps(['A. 不同对象对同一方法做出不同响应', 'B. 多个方法同名', 'C. 一个对象有多种形态', 'D. 继承多个类']), 'answer': 'A', 'analysis': '多态指不同对象对同一方法做出不同响应', 'difficulty': 2},
    {'category': 'Python', 'type': 'single', 'content': '类属性和实例属性的区别是？', 'options': json.dumps(['A. 类属性被所有对象共享，实例属性每个对象独有', 'B. 两者完全相同', 'C. 实例属性是类属性的一部分', 'D. 无区别']), 'answer': 'A', 'analysis': '类属性属于类，所有对象共享；实例属性属于单个对象', 'difficulty': 2},
    {'category': 'Python', 'type': 'judge', 'content': '在Python中，self指向类本身。', 'answer': 'FALSE', 'analysis': 'self指向类的实例对象，而不是类本身', 'difficulty': 2},

    # Day07 进阶语法
    {'category': 'Python', 'type': 'single', 'content': '闭包是指什么？', 'options': json.dumps(['A. 内层函数引用外层函数的变量', 'B. 关闭函数', 'C. 类的私有方法', 'D. 异常处理']), 'answer': 'A', 'analysis': '闭包是指内层函数引用了外层函数的变量，形成一个封闭的环境', 'difficulty': 2},
    {'category': 'Python', 'type': 'single', 'content': '装饰器的作用是？', 'options': json.dumps(['A. 在不修改原函数的情况下增加功能', 'B. 删除函数', 'C. 复制函数', 'D. 重命名函数']), 'answer': 'A', 'analysis': '装饰器可以在不修改原函数代码的情况下增加新功能', 'difficulty': 2},
    {'category': 'Python', 'type': 'single', 'content': '生成器和迭代器的主要区别是？', 'options': json.dumps(['A. 生成器使用yield，迭代器使用iter()', 'B. 两者完全相同', 'C. 迭代器更节省内存', 'D. 生成器不能迭代']), 'answer': 'A', 'analysis': '生成器使用yield返回，迭代器使用iter()，生成器是特殊的迭代器', 'difficulty': 2},
    {'category': 'Python', 'type': 'single', 'content': '深拷贝和浅拷贝的区别是？', 'options': json.dumps(['A. 深拷贝复制所有层，浅拷贝只复制第一层', 'B. 两者完全相同', 'C. 浅拷贝更节省内存', 'D. 无区别']), 'answer': 'A', 'analysis': '深拷贝递归复制所有层，浅拷贝只复制第一层引用', 'difficulty': 2},
    {'category': 'Python', 'type': 'single', 'content': '模块导入使用哪个关键字？', 'options': json.dumps(['A. import', 'B. include', 'C. require', 'D. using']), 'answer': 'A', 'analysis': 'Python使用import关键字导入模块', 'difficulty': 1},
    {'category': 'Python', 'type': 'single', 'content': 'from...import...的作用是？', 'options': json.dumps(['A. 从模块导入指定内容', 'B. 导出模块', 'C. 创建模块', 'D. 删除模块']), 'answer': 'A', 'analysis': 'from...import...可以从模块导入特定函数或变量', 'difficulty': 1},
]

# ----- Linux Shell题目 -----
linux_questions = [
    # Shell基础
    {'category': 'Linux', 'type': 'single', 'content': 'Shell脚本的文件后缀通常是？', 'options': json.dumps(['A. .sh', 'B. .bash', 'C. .shell', 'D. 无要求']), 'answer': 'A', 'analysis': 'Shell脚本推荐使用.sh后缀，方便区分', 'difficulty': 1},
    {'category': 'Linux', 'type': 'single', 'content': '给脚本添加可执行权限的命令是？', 'options': json.dumps(['A. chmod +x', 'B. chmod +r', 'C. chmod +w', 'D. chmod +s']), 'answer': 'A', 'analysis': 'chmod +x添加可执行权限，否则脚本无法运行', 'difficulty': 1},
    {'category': 'Linux', 'type': 'single', 'content': 'Shell变量的定义语法是？', 'options': json.dumps(['A. 变量名=值（等号前后不能有空格）', 'B. 变量名 = 值', 'C. $变量名=值', 'D. let 变量名=值']), 'answer': 'A', 'analysis': '变量赋值时等号前后不能有空格，否则会报错', 'difficulty': 1},
    {'category': 'Linux', 'type': 'single', 'content': '使用变量时需要在变量名前加什么符号？', 'options': json.dumps(['A. $', 'B. #', 'C. @', 'D. %']), 'answer': 'A', 'analysis': '使用变量时需要加$符号，如$name或${name}', 'difficulty': 1},
    {'category': 'Linux', 'type': 'single', 'content': '$0表示什么？', 'options': json.dumps(['A. 当前脚本的文件名', 'B. 第一个参数', 'C. 参数总数', 'D. 当前进程ID']), 'answer': 'A', 'analysis': '$0表示当前脚本的文件名', 'difficulty': 1},
    {'category': 'Linux', 'type': 'single', 'content': '$1表示什么？', 'options': json.dumps(['A. 第一个参数', 'B. 第二个参数', 'C. 脚本名', 'D. 参数总数']), 'answer': 'A', 'analysis': '$1表示运行脚本时传入的第一个参数', 'difficulty': 1},
    {'category': 'Linux', 'type': 'single', 'content': '$#表示什么？', 'options': json.dumps(['A. 参数总数', 'B. 第一个参数', 'C. 脚本名', 'D. 最后一个参数']), 'answer': 'A', 'analysis': '$#表示运行脚本时传入的参数总数', 'difficulty': 1},
    {'category': 'Linux', 'type': 'single', 'content': 'echo命令的作用是？', 'options': json.dumps(['A. 输出内容到终端', 'B. 读取用户输入', 'C. 创建文件', 'D. 删除文件']), 'answer': 'A', 'analysis': 'echo是最常用的输出命令', 'difficulty': 1},
    {'category': 'Linux', 'type': 'single', 'content': 'read命令的作用是？', 'options': json.dumps(['A. 接收用户输入', 'B. 读取文件内容', 'C. 创建文件', 'D. 输出内容']), 'answer': 'A', 'analysis': 'read命令接收用户输入并存储到变量中', 'difficulty': 1},
    {'category': 'Linux', 'type': 'single', 'content': 'Shell脚本中整数运算使用什么语法？', 'options': json.dumps(['A. $(())', 'B. []', 'C. {}', 'D. ()']), 'answer': 'A', 'analysis': 'Shell使用$(())进行整数运算，如$((a+b))', 'difficulty': 2},
    {'category': 'Linux', 'type': 'single', 'content': 'if条件判断的结束关键字是？', 'options': json.dumps(['A. fi', 'B. end', 'C. done', 'D. break']), 'answer': 'A', 'analysis': 'if语句必须以fi结束，形成if...fi的配对', 'difficulty': 1},
    {'category': 'Linux', 'type': 'single', 'content': '数字比较中-gt表示？', 'options': json.dumps(['A. 大于', 'B. 小于', 'C. 等于', 'D. 不等于']), 'answer': 'A', 'analysis': '-gt表示大于（greater than）', 'difficulty': 1},
    {'category': 'Linux', 'type': 'single', 'content': '数字比较中-eq表示？', 'options': json.dumps(['A. 等于', 'B. 大于', 'C. 小于', 'D. 不等于']), 'answer': 'A', 'analysis': '-eq表示等于（equal）', 'difficulty': 1},
    {'category': 'Linux', 'type': 'single', 'content': '文件判断中-f表示？', 'options': json.dumps(['A. 判断是否是普通文件', 'B. 判断是否是目录', 'C. 判断是否存在', 'D. 判断是否可读']), 'answer': 'A', 'analysis': '-f判断是否是普通文件（不是目录）', 'difficulty': 1},
    {'category': 'Linux', 'type': 'single', 'content': '文件判断中-d表示？', 'options': json.dumps(['A. 判断是否是目录', 'B. 判断是否是文件', 'C. 判断是否存在', 'D. 判断是否可写']), 'answer': 'A', 'analysis': '-d判断是否是目录（directory）', 'difficulty': 1},
    {'category': 'Linux', 'type': 'single', 'content': '文件判断中-e表示？', 'options': json.dumps(['A. 判断文件或目录是否存在', 'B. 判断是否为空', 'C. 判断是否可执行', 'D. 判断是否是文件']), 'answer': 'A', 'analysis': '-e判断文件或文件夹是否存在（exists）', 'difficulty': 1},
    {'category': 'Linux', 'type': 'single', 'content': 'for循环的结束关键字是？', 'options': json.dumps(['A. done', 'B. fi', 'C. end', 'D. break']), 'answer': 'A', 'analysis': 'for循环使用do...done包围循环体', 'difficulty': 1},
    {'category': 'Linux', 'type': 'single', 'content': 'while循环的条件判断语法是？', 'options': json.dumps(['A. while [ 条件 ]; do', 'B. while 条件 do', 'C. while (条件)', 'D. while {条件}']), 'answer': 'A', 'analysis': 'while循环语法：while [ 条件 ]; do ... done', 'difficulty': 1},
    {'category': 'Linux', 'type': 'single', 'content': '循环中break的作用是？', 'options': json.dumps(['A. 立即终止整个循环', 'B. 跳过当前一次循环', 'C. 退出脚本', 'D. 返回值']), 'answer': 'A', 'analysis': 'break立即终止整个循环，执行循环后面的代码', 'difficulty': 1},
    {'category': 'Linux', 'type': 'single', 'content': '循环中continue的作用是？', 'options': json.dumps(['A. 跳过当前一次循环', 'B. 终止整个循环', 'C. 退出脚本', 'D. 返回值']), 'answer': 'A', 'analysis': 'continue跳过当前一次循环，继续执行下一次循环', 'difficulty': 1},
    {'category': 'Linux', 'type': 'single', 'content': 'mkdir命令的作用是？', 'options': json.dumps(['A. 创建目录', 'B. 创建文件', 'C. 删除文件', 'D. 复制文件']), 'answer': 'A', 'analysis': 'mkdir(make directory)用于创建新目录', 'difficulty': 1},
    {'category': 'Linux', 'type': 'single', 'content': 'touch命令的作用是？', 'options': json.dumps(['A. 创建空文件', 'B. 创建目录', 'C. 删除文件', 'D. 复制文件']), 'answer': 'A', 'analysis': 'touch用于创建空文件或更新文件时间', 'difficulty': 1},
    {'category': 'Linux', 'type': 'single', 'content': 'cp命令的作用是？', 'options': json.dumps(['A. 复制文件/目录', 'B. 移动文件', 'C. 删除文件', 'D. 重命名文件']), 'answer': 'A', 'analysis': 'cp(copy)用于复制文件或目录', 'difficulty': 1},
    {'category': 'Linux', 'type': 'single', 'content': 'mv命令的作用是？', 'options': json.dumps(['A. 移动或重命名文件/目录', 'B. 复制文件', 'C. 删除文件', 'D. 创建文件']), 'answer': 'A', 'analysis': 'mv(move)用于移动或重命名文件/目录', 'difficulty': 1},
    {'category': 'Linux', 'type': 'single', 'content': 'cat命令的作用是？', 'options': json.dumps(['A. 查看文件内容', 'B. 创建文件', 'C. 复制文件', 'D. 删除文件']), 'answer': 'A', 'analysis': 'cat用于查看文件全部内容', 'difficulty': 1},
    {'category': 'Linux', 'type': 'single', 'content': 'set -x的作用是？', 'options': json.dumps(['A. 开启调试模式，显示每步执行过程', 'B. 退出脚本', 'C. 定义函数', 'D. 设置变量']), 'answer': 'A', 'analysis': 'set -x开启调试模式，显示脚本每一步执行的命令和变量值', 'difficulty': 2},
    {'category': 'Linux', 'type': 'single', 'content': '{1..10}表示什么？', 'options': json.dumps(['A. 1到10的数字序列', 'B. 10到1的序列', 'C. 1和10两个数字', 'D. 1或10']), 'answer': 'A', 'analysis': '{1..10}表示1到10的数字序列，是一种简写语法', 'difficulty': 1},
    {'category': 'Linux', 'type': 'judge', 'content': 'Shell脚本中变量赋值时，等号前后可以有空格。', 'answer': 'FALSE', 'analysis': '变量赋值时等号前后不能有空格，否则会报错', 'difficulty': 1},
    {'category': 'Linux', 'type': 'judge', 'content': 'if条件判断中，[]前后必须有空格。', 'answer': 'TRUE', 'analysis': 'Shell中[]前后必须有空格，如[ ${num} -gt 10 ]', 'difficulty': 1},
    {'category': 'Linux', 'type': 'judge', 'content': 'Linux默认使用的是Bash Shell。', 'answer': 'TRUE', 'analysis': 'Linux系统默认使用Bash（Bourne Again Shell）', 'difficulty': 1},

    # 常用命令
    {'category': 'Linux', 'type': 'single', 'content': 'pwd命令的作用是？', 'options': json.dumps(['A. 查看当前工作目录', 'B. 创建目录', 'C. 删除目录', 'D. 切换目录']), 'answer': 'A', 'analysis': 'pwd(print working directory)显示当前目录路径', 'difficulty': 1},
    {'category': 'Linux', 'type': 'single', 'content': 'ls命令的作用是？', 'options': json.dumps(['A. 列出目录下的文件', 'B. 创建文件', 'C. 删除文件', 'D. 移动文件']), 'answer': 'A', 'analysis': 'ls(list)列出目录下的文件/文件夹', 'difficulty': 1},
    {'category': 'Linux', 'type': 'single', 'content': 'cd命令的作用是？', 'options': json.dumps(['A. 切换工作目录', 'B. 复制文件', 'C. 删除文件', 'D. 创建文件']), 'answer': 'A', 'analysis': 'cd(change directory)切换到指定目录', 'difficulty': 1},
    {'category': 'Linux', 'type': 'single', 'content': 'rm -rf命令的作用是？', 'options': json.dumps(['A. 强制递归删除目录', 'B. 复制文件', 'C. 移动文件', 'D. 创建目录']), 'answer': 'A', 'analysis': 'rm -rf强制递归删除目录及其内容', 'difficulty': 1},
]

# ----- FastAPI题目 -----
fastapi_questions = [
    # HTTP协议
    {'category': 'FastAPI', 'type': 'single', 'content': 'HTTP的全称是？', 'options': json.dumps(['A. HyperText Transfer Protocol（超文本传输协议）', 'B. High Tech Transfer Protocol', 'C. Hyper Terminal Text Protocol', 'D. Home Text Transfer Protocol']), 'answer': 'A', 'analysis': 'HTTP是HyperText Transfer Protocol的缩写', 'difficulty': 1},
    {'category': 'FastAPI', 'type': 'single', 'content': 'HTTP状态码200表示？', 'options': json.dumps(['A. 请求成功', 'B. 资源不存在', 'C. 服务器错误', 'D. 权限不足']), 'answer': 'A', 'analysis': '200 OK表示请求成功，货物已送达', 'difficulty': 1},
    {'category': 'FastAPI', 'type': 'single', 'content': 'HTTP状态码404表示？', 'options': json.dumps(['A. 资源不存在', 'B. 请求成功', 'C. 服务器错误', 'D. 权限不足']), 'answer': 'A', 'analysis': '404 Not Found表示请求的资源在服务器上找不到', 'difficulty': 1},
    {'category': 'FastAPI', 'type': 'single', 'content': 'HTTP状态码500表示？', 'options': json.dumps(['A. 服务器内部错误', 'B. 请求成功', 'C. 资源不存在', 'D. 请求格式错误']), 'answer': 'A', 'analysis': '500 Internal Server Error表示服务器内部出错了', 'difficulty': 1},
    {'category': 'FastAPI', 'type': 'single', 'content': 'HTTP状态码400表示？', 'options': json.dumps(['A. 请求格式错误', 'B. 请求成功', 'C. 权限不足', 'D. 资源不存在']), 'answer': 'A', 'analysis': '400 Bad Request表示请求格式有问题，服务器无法理解', 'difficulty': 1},
    {'category': 'FastAPI', 'type': 'single', 'content': 'HTTP GET方法的作用是？', 'options': json.dumps(['A. 从服务器获取数据', 'B. 向服务器提交数据', 'C. 修改服务器数据', 'D. 删除服务器数据']), 'answer': 'A', 'analysis': 'GET用于从服务器获取（查询）数据', 'difficulty': 1},
    {'category': 'FastAPI', 'type': 'single', 'content': 'HTTP POST方法的作用是？', 'options': json.dumps(['A. 向服务器提交数据', 'B. 获取数据', 'C. 删除数据', 'D. 修改数据']), 'answer': 'A', 'analysis': 'POST用于向服务器提交（新增）数据', 'difficulty': 1},
    {'category': 'FastAPI', 'type': 'single', 'content': '前端与后端的主要区别是？', 'options': json.dumps(['A. 前端负责界面交互，后端负责业务逻辑', 'B. 两者完全相同', 'C. 前端在服务器运行', 'D. 后端在浏览器运行']), 'answer': 'A', 'analysis': '前端负责用户界面和交互，后端负责数据处理和业务逻辑', 'difficulty': 1},
    {'category': 'FastAPI', 'type': 'judge', 'content': 'HTTP协议是客户端与服务器之间传递数据的规范。', 'answer': 'TRUE', 'analysis': 'HTTP协议规定了客户端如何问、服务器如何答的格式', 'difficulty': 1},

    # FastAPI基础
    {'category': 'FastAPI', 'type': 'single', 'content': 'FastAPI框架的主要作用是？', 'options': json.dumps(['A. 构建API接口', 'B. 数据库操作', 'C. 前端开发', 'D. 图像处理']), 'answer': 'A', 'analysis': 'FastAPI是用于构建API的Python Web框架', 'difficulty': 1},
    {'category': 'FastAPI', 'type': 'single', 'content': 'FastAPI应用的创建语法是？', 'options': json.dumps(['A. FastAPI()', 'B. new FastAPI()', 'C. create FastAPI()', 'D. FastAPI.new()']), 'answer': 'A', 'analysis': '使用FastAPI()实例化创建应用', 'difficulty': 1},
    {'category': 'FastAPI', 'type': 'single', 'content': 'FastAPI中定义路由使用什么装饰器？', 'options': json.dumps(['A. @app.get()等', 'B. @route()', 'C. @router()', 'D. @path()']), 'answer': 'A', 'analysis': '使用@app.get()、@app.post()等装饰器定义路由', 'difficulty': 1},
    {'category': 'FastAPI', 'type': 'single', 'content': 'FastAPI启动命令是？', 'options': json.dumps(['A. uvicorn main:app --reload', 'B. python main.py', 'C. fastapi run', 'D. start fastapi']), 'answer': 'A', 'analysis': 'uvicorn main:app --reload是FastAPI标准启动命令，--reload表示热重载', 'difficulty': 1},
    {'category': 'FastAPI', 'type': 'single', 'content': 'FastAPI的交互式文档地址是？', 'options': json.dumps(['A. /docs', 'B. /api', 'C. /swagger', 'D. /document']), 'answer': 'A', 'analysis': 'FastAPI自动生成的交互式文档地址是http://127.0.0.1:8000/docs', 'difficulty': 1},
    {'category': 'FastAPI', 'type': 'single', 'content': 'FastAPI中路径参数使用什么语法定义？', 'options': json.dumps(['A. {参数名}', 'B. :参数名', 'C. <参数名>', 'D. (参数名)']), 'answer': 'A', 'analysis': 'FastAPI路径参数使用{}定义，如@app.get("/items/{item_id}")', 'difficulty': 1},
    {'category': 'FastAPI', 'type': 'single', 'content': '查询参数和路径参数的主要区别是？', 'options': json.dumps(['A. 查询参数在?后面，路径参数在URL路径中', 'B. 两者完全相同', 'C. 路径参数在?后面', 'D. 查询参数用于唯一标识']), 'answer': 'A', 'analysis': '路径参数是URL路径的一部分（如/items/{id}），查询参数是?后的键值对', 'difficulty': 1},
    {'category': 'FastAPI', 'type': 'single', 'content': 'FastAPI自动生成API文档依赖什么？', 'options': json.dumps(['A. OpenAPI标准', 'B. JSON格式', 'C. XML格式', 'D. HTML页面']), 'answer': 'A', 'analysis': 'FastAPI基于OpenAPI标准自动生成交互式API文档', 'difficulty': 2},
    {'category': 'FastAPI', 'type': 'single', 'content': 'FastAPI中使用Path模块的作用是？', 'options': json.dumps(['A. 对路径参数进行校验和元数据设置', 'B. 定义路由', 'C. 返回响应', 'D. 处理异常']), 'answer': 'A', 'analysis': 'Path模块用于路径参数的验证、范围限制和描述信息', 'difficulty': 2},
    {'category': 'FastAPI', 'type': 'single', 'content': 'FastAPI中使用Query模块的作用是？', 'options': json.dumps(['A. 对查询参数进行校验和设置默认值', 'B. 定义路径', 'C. 返回响应', 'D. 处理请求体']), 'answer': 'A', 'analysis': 'Query模块用于查询参数的验证、默认值设置和描述信息', 'difficulty': 2},
    {'category': 'FastAPI', 'type': 'single', 'content': 'B/S模式是指？', 'options': json.dumps(['A. 浏览器/服务器模式', 'B. 客户端/服务器模式', 'C. 业务/服务模式', 'D. 后端/前端模式']), 'answer': 'A', 'analysis': 'B/S是Browser/Server模式，即浏览器/服务器模式', 'difficulty': 1},
    {'category': 'FastAPI', 'type': 'single', 'content': 'C/S模式是指？', 'options': json.dumps(['A. 客户端/服务器模式', 'B. 浏览器/服务器模式', 'C. 业务/服务模式', 'D. 前端/后端模式']), 'answer': 'A', 'analysis': 'C/S是Client/Server模式，即客户端/服务器模式', 'difficulty': 1},
    {'category': 'FastAPI', 'type': 'single', 'content': 'FastAPI使用什么进行数据验证？', 'options': json.dumps(['A. Pydantic', 'B. JSON', 'C. XML', 'D. HTML']), 'answer': 'A', 'analysis': 'FastAPI基于Pydantic进行数据验证和类型提示', 'difficulty': 2},
    {'category': 'FastAPI', 'type': 'single', 'content': 'FastAPI安装命令是？', 'options': json.dumps(['A. pip install fastapi', 'B. npm install fastapi', 'C. apt install fastapi', 'D. get fastapi']), 'answer': 'A', 'analysis': '使用pip install fastapi安装FastAPI框架', 'difficulty': 1},
    {'category': 'FastAPI', 'type': 'single', 'content': 'ASGI服务器推荐使用？', 'options': json.dumps(['A. Uvicorn', 'B. Nginx', 'C. Apache', 'D. Tomcat']), 'answer': 'A', 'analysis': 'Uvicorn是FastAPI推荐的ASGI服务器', 'difficulty': 1},
    {'category': 'FastAPI', 'type': 'judge', 'content': 'FastAPI只支持同步请求处理。', 'answer': 'FALSE', 'analysis': 'FastAPI原生支持async/await异步请求处理', 'difficulty': 2},
    {'category': 'FastAPI', 'type': 'judge', 'content': '通过浏览器访问网址，发起的都是GET请求。', 'answer': 'TRUE', 'analysis': '浏览器地址栏访问URL默认发起GET请求', 'difficulty': 1},
    {'category': 'FastAPI', 'type': 'judge', 'content': 'FastAPI会自动生成交互式API文档。', 'answer': 'TRUE', 'analysis': 'FastAPI基于OpenAPI自动生成/docs和/redoc文档', 'difficulty': 1},
]


def add_questions_for_category(category_name, questions_list):
    """为指定分类添加题目"""
    existing = db.query(Question).filter(Question.category == category_name).count()
    print(f'Current {category_name} questions: {existing}')

    added = 0
    for q in questions_list:
        if not db.query(Question).filter(Question.content == q['content']).first():
            db.add(Question(**q))
            added += 1

    db.commit()
    print(f'Added {added} new {category_name} questions')
    print(f'Total {category_name} questions: {db.query(Question).filter(Question.category == category_name).count()}')


# 添加各类题目
add_questions_for_category('Python', python_questions)
add_questions_for_category('Linux', linux_questions)
add_questions_for_category('FastAPI', fastapi_questions)

db.close()
print('\nAll questions added successfully!')
