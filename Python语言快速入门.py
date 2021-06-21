
# 1.在Python中对一个变量赋值时，你就创建了一个指向等号右边对象的引用。
a = [1, 2, 3]
b = a           # 注意：在Python中，a 和 b实际上是指向了相同的对象
print(a, b)

a.append(4)
print(b)

# 2.type() : 返回对象的类型
a = 5
print(type(a))
a = 'foo'
print(type(a))
# isinstance() : 检查一个对象是否是特定类型的实例
a = 5
print(isinstance(a, int))

a = 5; b = 4.5
print(isinstance(a, (int, float)))

a = 'foo'
print(getattr(a, 'split'))

def isiterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:   # 不可遍历
        return False

print(isiterable('a string'))
print(isiterable([1, 2, 3]))
print(isiterable(5))

x = '1234'
print('x 原始输出：{0}'.format(x))
print('x : {0} 可以迭代吗？{1}'.format(x, isiterable(x)))
print('x : {0} 是 list 对象吗？{1}'.format(x, isinstance(x, list)))
if not isinstance(x, list) and isiterable(x):   # 不是列表对象，但是可以迭代则执行
    x = list(x)
    print('执行我了！')
print(x)

if not (False and False):
    print('该语句已执行！')
else:
    print('else 语句已执行！')

# 在 该文件可以使用 import 调用 some_module 文件
import some_module
result = some_module.f(5)
pi = some_module.PI
print(pi)

# 或者
import some_module as sm
from some_module import PI as pi, g as gf

r1 = sm.f(pi)
r2 = gf(6, pi)
print(r1, r2)

a = [1, 2, 3]
b = a
c = list(a)

print(a is b)
print(a is not c)

a = None
print(a is None)

# 可变对象 和 不可变对象
# 列表、字典和 Numpy 数组是可变对象
a_list = ['foo', 2, [4, 5]]
a_list[2] = (3, 4)
print(a_list)

# 还有一些对象是不可变的，比如字符串、元组
a_tuple = (3, 5, (4, 5))
# a_tuple[1] = 'four' # 报错：TypeError: 'tuple' object does not support item assignment
print(a_tuple)

ival = 100
print( 2 ** ival)

# 含有换行符的多个字符串 使用 '\n' 表示
c = """
This is a longer string that
spans multiple lines
"""
print(c)
print(c.count('\n'))

# Python 字符串是不可变的，你无法修改一个字符串
a = 'this is a string'
# a[10] = 'f' # TypeError: 'str' object does not support item assignment
print(a)

a = 5.6
s = str(a)
print(s, type(s))

s = 'python'
print(list(s))
print(list(s[:3]))

s = '12\\34'
print('输出原生的反斜杠字符：{0}'.format(s))
# 另外一种方法：字符串前面加 'r'，r ：raw 表示原生的
s = r'12\\34'
print(s)

a = 'this is the first half '
b = 'and this is the second half'
print(a + b)
print('{0} + {1} = {2}'.format(1, 2, 3))

template = '{0:.2f} {1:s} are worth US${2:d}'
print(template.format(4.5660, 'Agentine Pesos', 1))

bytes_val = b'this is bytes'
print(bytes_val)
decoded  = bytes_val.decode('utf-8')
print(decoded)

print(bool(0))
print(bool(3.14))

# None 是Python 的null值类型。如果一个函数没有显式地返回值，则它会隐式地返回None。
a = None
print(type(a))
print(a is None)

def add_and_maybe_multiply(a, b, c=None):
    result = a + b

    if c is not None:
        result = result * c
    return result

print(add_and_maybe_multiply(23, 5, 10))
print(type(None))

# 日期和时间
from datetime import datetime, date, time
dt = datetime(2021, 6, 9, 15, 30, 21)
print(dt)
print(dt.day)
print(dt.minute)

print(dt.date())
print(dt.time())
# 将 datetime --> 字符串
print(dt.strftime('%Y/%m/%d %H:%M'))
print(datetime.strptime('20091031', '%Y%m%d'))
dt2 = dt.replace(minute=0, second=0)
print(dt)
print(dt2)  # 新建了一个对象

dt2 = datetime(2021, 7, 15, 22, 30)
delta = dt2 - dt
print(delta)
print(dt + delta)

# 循环语句 :
# if 语句
x = 10
if x < 0:
    print('It\'s negative')
else:
    print('x is pssitive')
# for循环：用于遍历一个集合（例如列表或元组）或一个迭代器
# for value in collection:
    # 用值做些什么哪
sequence = [1, 2, None, 4, None, 5]
total = 0
for value in sequence:
    if value == None:
        continue
    total += value
print('total : {0}'.format(total))
x = 256
total = 0
while x > 0:
    if total > 500:
        break
    total += x
    x = x // 2
print('x : {0}'.format(x))

# pass : 什么都不做
if x < 0:
    print('negative!')
elif x == 0:
    pass
else:
    print('positive!')

print(list(range(5, 0, -1)))

seq = [1, 2, 3, 4]
for i in range(len(seq)):
    val = seq[i]
print('val : {0}'.format(val))

# 三元表达式：类似于C语言中的三目运算符
a = -1
value = a if a > 0 else 0
print(value)

x = 5
print('Non-negative' if x >= 0 else 'Negative')