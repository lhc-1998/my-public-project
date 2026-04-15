# -*- coding: utf-8 -*-
from database import SessionLocal
from models import Question
import json

db = SessionLocal()

# Python高级题库 - 基于Day05-Day07进阶内容
advanced_questions = [
    # ============ 闭包与装饰器 ============
    {
        "type": "single",
        "difficulty": 3,
        "category": "Python",
        "content": "以下哪个是形成闭包的必要条件？",
        "options": json.dumps([
            "A. 函数必须返回数值",
            "B. 嵌套函数、内部函数引用外部函数变量、外部函数返回内部函数名",
            "C. 必须使用global关键字",
            "D. 内部函数必须定义在类中"
        ]),
        "answer": "B",
        "analysis": "闭包的三个必要条件：1.嵌套函数 2.内部函数引用外部函数的变量 3.外部函数返回内部函数名"
    },
    {
        "type": "single",
        "difficulty": 3,
        "category": "Python",
        "content": "Python中判断一个函数是否是闭包，可以通过查看该函数的哪个魔法属性？",
        "options": json.dumps([
            "A. __name__",
            "B. __closure__",
            "C. __code__",
            "D. __defaults__"
        ]),
        "answer": "B",
        "analysis": "函数的__closure__属性可以判断是否是闭包，如果有值则是闭包，None则不是"
    },
    {
        "type": "single",
        "difficulty": 3,
        "category": "Python",
        "content": "装饰器的本质是什么？",
        "options": json.dumps([
            "A. 一种特殊的数据类型",
            "B. 利用闭包实现的函数装饰模式",
            "C. 类的另一种写法",
            "D. 异步编程的一种方式"
        ]),
        "answer": "B",
        "analysis": "装饰器本质上就是利用了闭包实现，在不修改原函数代码的情况下动态增加功能"
    },
    {
        "type": "single",
        "difficulty": 3,
        "category": "Python",
        "content": """代码执行结果是什么？
def login(fn):
    def inner(*args, **kwargs):
        print('正在登录中.....')
        fn(*args, **kwargs)
    return inner

@login
def pay(money):
    print(f'支付了{money}元')

pay(100)""",
        "options": json.dumps([
            "A. 支付了100元",
            "B. 正在登录中.....\\n支付了100元",
            "C. 正在登录中.....",
            "D. 报错"
        ]),
        "answer": "B",
        "analysis": "@login装饰器会在执行pay函数前先执行inner函数，打印登录提示后再调用原函数"
    },
    {
        "type": "judge",
        "difficulty": 3,
        "category": "Python",
        "content": "闭包可以让局部变量长生不老，即使外部函数已经执行完毕。",
        "answer": "正确",
        "analysis": "闭包的核心作用之一就是让局部变量持久化，不被垃圾回收"
    },
    {
        "type": "judge",
        "difficulty": 3,
        "category": "Python",
        "content": "装饰器只能装饰函数，不能装饰类方法。",
        "answer": "错误",
        "analysis": "装饰器同样可以装饰类方法，只要方法符合被装饰的条件"
    },

    # ============ 迭代器与生成器 ============
    {
        "type": "single",
        "difficulty": 3,
        "category": "Python",
        "content": "迭代器必须实现哪两个方法？",
        "options": json.dumps([
            "A. __iter__ 和 __next__",
            "B. __enter__ 和 __exit__",
            "C. __str__ 和 __repr__",
            "D. __init__ 和 __del__"
        ]),
        "answer": "A",
        "analysis": "迭代器协议要求实现__iter__方法返回自身，和__next__方法返回下一个元素"
    },
    {
        "type": "single",
        "difficulty": 3,
        "category": "Python",
        "content": "生成器函数和普通函数最大的区别是什么？",
        "options": json.dumps([
            "A. 生成器函数执行更快",
            "B. 生成器函数包含yield表达式，调用不立即执行",
            "C. 生成器函数必须返回列表",
            "D. 生成器函数只能处理数值"
        ]),
        "answer": "B",
        "analysis": "生成器函数体中包含yield，调用时不会立即执行，只返回生成器对象，需要用next()触发执行"
    },
    {
        "type": "single",
        "difficulty": 3,
        "category": "Python",
        "content": """以下代码的输出是什么？
def my_gen():
    yield 1
    yield 2
    yield 3

g = my_gen()
print(next(g))
print(next(g))""",
        "options": json.dumps([
            "A. 1 2",
            "B. [1,2,3]",
            "C. 3",
            "D. 报错"
        ]),
        "answer": "A",
        "analysis": "调用my_gen()返回生成器对象，next()每次从yield处暂停并返回值，连续调用会依次返回1和2"
    },
    {
        "type": "single",
        "difficulty": 3,
        "category": "Python",
        "content": "关于生成器和列表处理大型数据的说法，正确的是？",
        "options": json.dumps([
            "A. 列表更适合，因为查询速度快",
            "B. 生成器更适合，因为逐个计算不占内存",
            "C. 两者一样，没有区别",
            "D. 列表可以处理无限数据"
        ]),
        "answer": "B",
        "analysis": "生成器通过计算规则得到每个数据，不一次性加载入内存，适合处理大型数据和无限数据流"
    },
    {
        "type": "judge",
        "difficulty": 3,
        "category": "Python",
        "content": "生成器的本质也是一种迭代器。",
        "answer": "正确",
        "analysis": "生成器实现了迭代器协议（__iter__和__next__），所以生成器本质上是迭代器的一种"
    },
    {
        "type": "judge",
        "difficulty": 3,
        "category": "Python",
        "content": "yield表达式会使函数变成生成器，调用函数时会立即执行函数体中的代码。",
        "answer": "错误",
        "analysis": "函数体中包含yield时，调用函数不会立即执行，只返回一个生成器对象"
    },

    # ============ 深拷贝与浅拷贝 ============
    {
        "type": "single",
        "difficulty": 3,
        "category": "Python",
        "content": """代码执行后，a的值是什么？
import copy
a = [1, 2, [3, 4]]
b = a.copy()
b[2][0] = 999
print(a)""",
        "options": json.dumps([
            "A. [1, 2, [3, 4]]",
            "B. [1, 2, [999, 4]]",
            "C. [999, 2, [3, 4]]",
            "D. 报错"
        ]),
        "answer": "B",
        "analysis": "copy()是浅拷贝，只复制最外层容器，内部元素仍然是引用，所以修改b的内层列表会影响a"
    },
    {
        "type": "single",
        "difficulty": 3,
        "category": "Python",
        "content": """代码执行后，c的值是什么？
import copy
c = [1, 2, [3, 4]]
d = copy.deepcopy(c)
d[2][0] = 888
print(c)""",
        "options": json.dumps([
            "A. [1, 2, [888, 4]]",
            "B. [1, 2, [3, 4]]",
            "C. [1, 2, [888, 4]]",
            "D. [888, 2, [3, 4]]"
        ]),
        "answer": "B",
        "analysis": "deepcopy是深拷贝，完全递归复制，修改d的内层列表不会影响原对象c"
    },
    {
        "type": "single",
        "difficulty": 3,
        "category": "Python",
        "content": "以下哪种情况深拷贝是必须的？",
        "options": json.dumps([
            "A. 拷贝简单数字",
            "B. 拷贝字符串",
            "C. 拷贝包含嵌套可变对象的数据结构",
            "D. 拷贝元组"
        ]),
        "answer": "C",
        "analysis": "当数据结构包含嵌套的可变对象（列表、字典）时，如果需要完全独立复制，互不影响，应使用深拷贝"
    },
    {
        "type": "judge",
        "difficulty": 3,
        "category": "Python",
        "content": "直接赋值 b = a，两个变量指向同一个对象，修改其中一个会影响另一个。",
        "answer": "正确",
        "analysis": "直接赋值只是让两个变量名指向同一个内存地址，不是真正的拷贝"
    },
    {
        "type": "judge",
        "difficulty": 3,
        "category": "Python",
        "content": "不可变数据类型（如tuple）不需要深拷贝，因为它们不可修改。",
        "answer": "正确",
        "analysis": "不可变类型在修改时会创建新对象，所以不存在引用共享导致意外修改的问题"
    },

    # ============ 类属性与类方法 ============
    {
        "type": "single",
        "difficulty": 3,
        "category": "Python",
        "content": """代码执行结果是什么？
class Student:
    school_name = '沃林'
    instance_count = 0
    
    def __init__(self, name):
        self.name = name
        Student.instance_count += 1

s1 = Student('zs')
s2 = Student('ls')
print(Student.instance_count)""",
        "options": json.dumps([
            "A. 0",
            "B. 1",
            "C. 2",
            "D. 报错"
        ]),
        "answer": "C",
        "analysis": "每次创建实例都会执行__init__，类属性instance_count递增，创建两个实例后值为2"
    },
    {
        "type": "single",
        "difficulty": 3,
        "category": "Python",
        "content": "类属性和实例属性的区别是什么？",
        "options": json.dumps([
            "A. 没有区别",
            "B. 类属性所有对象共享，通过类名修改；实例属性每个对象独立",
            "C. 实例属性不能修改",
            "D. 类属性不能被访问"
        ]),
        "answer": "B",
        "analysis": "类属性是所有对象共享的数据，只能通过类名修改；实例属性是每个对象独立拥有的"
    },
    {
        "type": "single",
        "difficulty": 3,
        "category": "Python",
        "content": """代码执行结果是什么？
class Test:
    @classmethod
    def show(cls):
        print(cls.__name__)

Test.show()""",
        "options": json.dumps([
            "A. Test",
            "B. object",
            "C. cls",
            "D. 报错"
        ]),
        "answer": "A",
        "analysis": "@classmethod装饰的方法会自动接收类作为第一个参数，cls.__name__返回类名'Test'"
    },
    {
        "type": "judge",
        "difficulty": 3,
        "category": "Python",
        "content": "类方法必须通过类名调用，不能通过实例对象调用。",
        "answer": "错误",
        "analysis": "类方法既可以通过类名调用，也可以通过实例对象调用（此时cls仍指向类）"
    },
    {
        "type": "judge",
        "difficulty": 3,
        "category": "Python",
        "content": "通过实例对象可以直接修改类属性的值。",
        "answer": "错误",
        "analysis": "通过实例对象修改类属性会创建新的实例属性，而不是修改类属性本身"
    },

    # ============ __del__与引用计数 ============
    {
        "type": "single",
        "difficulty": 3,
        "category": "Python",
        "content": "__del__方法在什么时候被调用？",
        "options": json.dumps([
            "A. 对象创建时",
            "B. 对象被销毁前",
            "C. 每次访问对象时",
            "D. 程序结束时"
        ]),
        "answer": "B",
        "analysis": "__del__是析构方法，在对象即将被销毁（引用计数为0）时自动调用"
    },
    {
        "type": "single",
        "difficulty": 3,
        "category": "Python",
        "content": "Python中使用什么方式判断对象是否需要被回收？",
        "options": json.dumps([
            "A. 标记-清除算法",
            "B. 引用计数",
            "C. 分代收集",
            "D. 手动释放"
        ]),
        "answer": "B",
        "analysis": "Python使用引用计数方式判断对象是否需要销毁，当引用计数为0时立即回收"
    },
    {
        "type": "single",
        "difficulty": 3,
        "category": "Python",
        "content": "__del__方法的典型应用场景是什么？",
        "options": json.dumps([
            "A. 初始化对象属性",
            "B. 释放非内存资源（如关闭文件、数据库连接）",
            "C. 打印对象信息",
            "D. 创建新对象"
        ]),
        "answer": "B",
        "analysis": "__del__常用于释放非内存资源，因为这些资源需要及时关闭避免泄漏，内存资源由垃圾回收器自动处理"
    },
    {
        "type": "judge",
        "difficulty": 3,
        "category": "Python",
        "content": "如果对象的引用计数变为0，Python会立即销毁该对象。",
        "answer": "正确",
        "analysis": "引用计数为0时，对象会立即被销毁并回收内存，这是Python与其他使用标记-清除的语言的区别"
    },

    # ============ 多继承与MRO ============
    {
        "type": "single",
        "difficulty": 3,
        "category": "Python",
        "content": """代码执行结果是什么？
class A:
    def show(self): return 'A'

class B(A):
    def show(self): return 'B'

class C(A):
    def show(self): return 'C'

class D(B, C):
    pass

d = D()
print(d.show())""",
        "options": json.dumps([
            "A. A",
            "B. B",
            "C. C",
            "D. 报错"
        ]),
        "answer": "B",
        "analysis": "D继承B和C，MRO顺序从左到右，先子后父，所以优先使用B的show方法"
    },
    {
        "type": "single",
        "difficulty": 3,
        "category": "Python",
        "content": "如何查看一个类的MRO（方法解析顺序）？",
        "options": json.dumps([
            "A. 类名.mro()",
            "B. 类名.__parents__",
            "C. 类名.inherit()",
            "D. 类名.order()"
        ]),
        "answer": "A",
        "analysis": "通过 类名.mro() 或 类名.__mro__ 可以查看该类的继承顺序"
    },
    {
        "type": "judge",
        "difficulty": 3,
        "category": "Python",
        "content": "在多继承中，如果多个父类有同名方法，Python按照从左到右的顺序在MRO列表中查找。",
        "answer": "正确",
        "analysis": "MRO遵循C3线性化算法，查找顺序是从左到右，先查找子类，再查找父类"
    },

    # ============ 面向对象高级特性 ============
    {
        "type": "single",
        "difficulty": 3,
        "category": "Python",
        "content": "多态的核心概念是什么？",
        "options": json.dumps([
            "A. 同一个类可以创建多个对象",
            "B. 同一个行为，不同对象做出不同响应",
            "C. 一个类可以继承多个父类",
            "D. 对象可以动态添加属性"
        ]),
        "answer": "B",
        "analysis": "多态指不同对象对同一方法做出不同响应，例如动物都叫，但猫喵喵、狗汪汪"
    },
    {
        "type": "single",
        "difficulty": 3,
        "category": "Python",
        "content": "Python中私有属性的命名规范是什么？",
        "options": json.dumps([
            "A. _属性名",
            "B. __属性名",
            "C. ___属性名",
            "D. private_属性名"
        ]),
        "answer": "B",
        "analysis": "Python中以双下划线__开头的属性会被解释器进行名字改写，实现类似private的效果"
    },
    {
        "type": "single",
        "difficulty": 3,
        "category": "Python",
        "content": "以下代码执行后，obj.__money的值是多少？\\nclass BankCard:\\n    def __init__(self):\\n        self.__money = 100\\ncard = BankCard()\\ncard.__money = 999",
        "options": json.dumps([
            "A. 100",
            "B. 999",
            "C. 报错",
            "D. None"
        ]),
        "answer": "A",
        "analysis": "__money被改名为_BankCard__money，外部设置的__money实际上是创建了新属性，不影响原私有属性"
    },
    {
        "type": "single",
        "difficulty": 3,
        "category": "Python",
        "content": "super()函数的作用是什么？",
        "options": json.dumps([
            "A. 创建父类对象",
            "B. 调用父类的方法",
            "C. 销毁子类对象",
            "D. 定义父类"
        ]),
        "answer": "B",
        "analysis": "super()返回父类对象，可以显式调用父类的方法，常用于在子类中扩展父类功能"
    },
    {
        "type": "judge",
        "difficulty": 3,
        "category": "Python",
        "content": "在Python中，所有类如果不写继承父类，默认都继承自object。",
        "answer": "正确",
        "analysis": "Python3默认使用新式类，所有类都直接或间接继承object，这就是为什么任何类都有__str__、__dict__等方法"
    },
    {
        "type": "judge",
        "difficulty": 3,
        "category": "Python",
        "content": "封装就是将属性和方法名字前加双下划线，使其无法被外部访问。",
        "answer": "错误",
        "analysis": "封装的核心是将属性和方法放到类内部，通过公开接口控制访问，而不是简单阻止访问"
    },

    # ============ 模块与包 ============
    {
        "type": "single",
        "difficulty": 3,
        "category": "Python",
        "content": "Python中一个.py文件被称为什么？",
        "options": json.dumps([
            "A. 包",
            "B. 模块",
            "C. 类库",
            "D. 函数"
        ]),
        "answer": "B",
        "analysis": "一个.py文件就是一个模块，可以包含变量、函数、类等"
    },
    {
        "type": "single",
        "difficulty": 3,
        "category": "Python",
        "content": "包和普通文件夹的区别是什么？",
        "options": json.dumps([
            "A. 包名更长",
            "B. 包包含__init__.py文件",
            "C. 包不能导入",
            "D. 包只能放一个模块"
        ]),
        "answer": "B",
        "analysis": "带__init__.py的文件夹才是Python包，__init__.py可以控制包的导出行为"
    },
    {
        "type": "single",
        "difficulty": 3,
        "category": "Python",
        "content": "__all__变量的作用是什么？",
        "options": json.dumps([
            "A. 定义包的版本",
            "B. 控制from pkg import *时能导入的内容",
            "C. 导入所有模块",
            "D. 导出所有类"
        ]),
        "answer": "B",
        "analysis": "__all__在__init__.py中设置，控制from pkg import *时能导入的成员"
    },
    {
        "type": "single",
        "difficulty": 3,
        "category": "Python",
        "content": "__name__变量在什么情况下等于'__main__'？",
        "options": json.dumps([
            "A. 作为模块导入时",
            "B. 作为主程序直接运行时",
            "C. 永远不等于",
            "D. 导入时和运行时都等于"
        ]),
        "answer": "B",
        "analysis": "__name__作为主程序运行时得到__main__，作为模块导入时得到模块名"
    },
    {
        "type": "judge",
        "difficulty": 3,
        "category": "Python",
        "content": "导入模块时，模块里的代码会立即执行。",
        "answer": "正确",
        "analysis": "import语句会执行被导入模块的顶层代码，这是需要注意避免在模块顶层执行耗时操作的原因"
    },
    {
        "type": "judge",
        "difficulty": 3,
        "category": "Python",
        "content": "from 模块 import * 可以导入该模块的所有内容。",
        "answer": "错误",
        "analysis": "import * 只能导入模块中不在_开头的成员，以及__all__列表中定义的成员"
    },

    # ============ 文件操作进阶 ============
    {
        "type": "single",
        "difficulty": 3,
        "category": "Python",
        "content": "以'w'模式打开一个已有内容的文件，会发生什么？",
        "options": json.dumps([
            "A. 追加内容",
            "B. 报错",
            "C. 清空原有内容",
            "D. 跳过"
        ]),
        "answer": "C",
        "analysis": "'w'模式会清空文件原有内容，从头开始写入，使用时需注意"
    },
    {
        "type": "single",
        "difficulty": 3,
        "category": "Python",
        "content": "JSON和Python字典的区别是什么？",
        "options": json.dumps([
            "A. 没有区别",
            "B. JSON是字符串，字典是Python数据类型",
            "C. JSON只能存数字",
            "D. 字典只能存字符串"
        ]),
        "answer": "B",
        "analysis": "JSON本质上是字符串格式，用于跨语言数据交换；字典是Python的内存数据结构"
    },
    {
        "type": "single",
        "difficulty": 3,
        "category": "Python",
        "content": "json.dumps()和json.loads()的作用分别是？",
        "options": json.dumps([
            "A. dumps是反序列化，loads是序列化",
            "B. dumps是序列化，loads是反序列化",
            "C. 都是序列化",
            "D. 都是反序列化"
        ]),
        "answer": "B",
        "analysis": "dumps(序列化)将Python对象转JSON字符串，loads(反序列化)将JSON字符串转Python对象"
    },
    {
        "type": "judge",
        "difficulty": 3,
        "category": "Python",
        "content": "使用with open语句可以确保文件被正确关闭，即使中间代码出错。",
        "answer": "正确",
        "analysis": "with语句会在离开代码块时自动调用__exit__关闭文件，避免忘记close()导致的资源泄漏"
    },
    {
        "type": "judge",
        "difficulty": 3,
        "category": "Python",
        "content": "'r+'模式和'w+'模式的主要区别是'r+'不会清空文件，'w+'会清空文件。",
        "answer": "正确",
        "analysis": "'r+'要求文件必须存在且不清空，'w+'文件不存在则创建，存在则清空"
    },

    # ============ 异常处理进阶 ============
    {
        "type": "single",
        "difficulty": 3,
        "category": "Python",
        "content": "try...except...else...finally结构中，else子句在什么时候执行？",
        "options": json.dumps([
            "A. 任何时候",
            "B. except捕获到异常时",
            "C. try块没有发生异常时",
            "D. except没有捕获到异常时"
        ]),
        "answer": "C",
        "analysis": "else子句只在try块正常执行完毕（没有发生异常）时执行"
    },
    {
        "type": "single",
        "difficulty": 3,
        "category": "Python",
        "content": "try...except...finally结构中，finally子句在什么时候执行？",
        "options": json.dumps([
            "A. 只有try块执行时",
            "B. 只有except块执行时",
            "C. 不管有没有异常都会执行",
            "D. 只有程序结束时"
        ]),
        "answer": "C",
        "analysis": "finally子句无论是否有异常都会执行，常用于释放资源的清理工作"
    },
    {
        "type": "single",
        "difficulty": 3,
        "category": "Python",
        "content": """代码执行结果是什么？
try:
    print(1/0)
except ZeroDivisionError:
    print('除数不能为零')
except Exception as e:
    print('其他错误')""",
        "options": json.dumps([
            "A. 其他错误",
            "B. 除数不能为零",
            "C. 报错",
            "D. 无输出"
        ]),
        "answer": "B",
        "analysis": "1/0会触发ZeroDivisionError，被第一个匹配的except捕获，打印对应消息"
    },
    {
        "type": "judge",
        "difficulty": 3,
        "category": "Python",
        "content": "捕获异常时，应该先捕获具体异常，再捕获通用异常。",
        "answer": "正确",
        "analysis": "异常匹配从上到下进行，先捕获具体异常能更精确处理不同错误类型"
    },

    # ============ 综合应用题 ============
    {
        "type": "single",
        "difficulty": 3,
        "category": "Python",
        "content": """以下代码输出什么？
def outer(x):
    def inner(y):
        return x + y
    return inner

add5 = outer(5)
print(add5(3))""",
        "options": json.dumps([
            "A. 3",
            "B. 5",
            "C. 8",
            "D. 报错"
        ]),
        "answer": "C",
        "analysis": "outer(5)返回inner函数，add5(3)调用inner，x=5被闭包记住，所以返回5+3=8"
    },
    {
        "type": "single",
        "difficulty": 3,
        "category": "Python",
        "content": """以下代码输出什么？
class Parent:
    def __init__(self):
        print('Parent init')
        
class Child(Parent):
    def __init__(self):
        super().__init__()
        print('Child init')

Child()""",
        "options": json.dumps([
            "A. Child init",
            "B. Parent init\\nChild init",
            "C. Parent init",
            "D. 报错"
        ]),
        "answer": "B",
        "analysis": "子类的__init__中调用super().__init__()显式执行父类的初始化方法，所以两者都会输出"
    },
    {
        "type": "single",
        "difficulty": 3,
        "category": "Python",
        "content": """以下代码输出什么？
def count():
    result = []
    for i in range(3):
        def f():
            return i
        result.append(f)
    return result

fs = count()
print(fs[0]())""",
        "options": json.dumps([
            "A. 0",
            "B. 1",
            "C. 2",
            "D. 3"
        ]),
        "answer": "C",
        "analysis": "三个函数都返回i，当循环结束后i=2，所以所有函数都返回2（闭包陷阱）"
    },
    {
        "type": "single",
        "difficulty": 3,
        "category": "Python",
        "content": """以下代码输出什么？
class A:
    x = 1
    
class B(A):
    pass

class C(A):
    pass

B.x = 2
print(A.x, B.x, C.x)""",
        "options": json.dumps([
            "A. 1 2 1",
            "B. 2 2 2",
            "C. 1 1 1",
            "D. 报错"
        ]),
        "answer": "A",
        "analysis": "B.x=2创建了B的新实例属性，不影响A和C的类属性x=1"
    },
    {
        "type": "judge",
        "difficulty": 3,
        "category": "Python",
        "content": "列表推导式[func(i) for i in range(3)]和生成器表达式(func(i) for i in range(3))的主要区别是前者返回列表，后者返回生成器对象。",
        "answer": "正确",
        "analysis": "列表推导式立即生成所有元素到列表，生成器表达式返回迭代器，按需生成元素"
    },
    {
        "type": "judge",
        "difficulty": 3,
        "category": "Python",
        "content": "在类方法中，self代表当前对象；在类方法中，cls代表当前类。",
        "answer": "正确",
        "analysis": "实例方法的第一个参数是self（当前对象），类方法的第一个参数是cls（当前类）"
    },
]

def add_questions():
    """添加高级题目"""
    existing = db.query(Question).filter(Question.category == 'Python', Question.difficulty == 'hard').count()
    print(f'Current Python advanced questions: {existing}')
    
    added = 0
    for q in advanced_questions:
        # 检查是否已存在
        existing_q = db.query(Question).filter(
            Question.content == q['content']
        ).first()
        
        if not existing_q:
            db.add(Question(**q))
            added += 1
    
    db.commit()
    print(f'Added {added} new Python advanced questions')
    print(f'Total Python advanced questions: {existing + added}')

if __name__ == '__main__':
    add_questions()
    db.close()
