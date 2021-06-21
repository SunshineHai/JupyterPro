# 读取文件好方便

# 1.遍历输出
# 1.1 使用的是绝对路径，也可以使用相对路径
path = 'F:/DataSet/test1.txt'
f = open(path, encoding='UTF-8') # 设置读取的编码，否则中文会输出乱码

for line in f:      # 若一行中有换行，则会输出多个换行。
    print(line)
    pass

# 1.2 x.rstrip() ：末尾字符串中的空格符。
lines = [x.rstrip() for x in open(path, encoding='utf-8')]
print(lines)
# 创建open() 对象后，如不用，则显式地关闭文件。
f.close()
# 2.或使用with语句,文件会在with代码块结束后自动关闭
with open(path, 'r', encoding='utF-8') as f:
    lines = [x.rstrip() for x in f]
print(lines)

path2 = 'F:/dataset/codetext.txt'
f = open(path2, encoding='utf-8')
print(f.read(10))  # 读取前10个字符

f2 = open(path2, 'rb') # Binary mode
print(f2.read(10))
# tell() ： 返回当前的文件位置，返回值是整数
print(f.tell())     # 14
print(f2.tell())    # 10

# 检测文件编码
import sys
print(sys.getdefaultencoding())

f.seek(3)
print(f.read(4))

f.close()
f2.close()

path = 'F:/dataset/template.txt'
# 写入文件：write或者writelline
with open('F:/dataset/tmp.txt', 'w') as handle:
    handle.writelines(x for x in open(path) if len(x) > 1)
f = open('F:/dataset/tmp.txt', 'r+') # r+ : 读写模式
lines = f.readlines()
print(lines)
# 把字符串写入到 指定文件的末尾。好NB
f.write('Python is Stronger than Java!')

f.close()
# f.read() # 前边已经关闭文件，再次读会报错：ValueError: I/O operation on closed file.

# 文本模式与二进制模式： 对于有汉字的该怎么处理？对于字符，python默认是UNICode编码
path = 'F:/DataSet/BinarycodeAndTextcode.txt'
with open(path) as f:
    chars = f.read(10)      # 默认以文本模式读取
print(chars)        # Sue@a el 鍥

with open(path, 'rb') as f: # 默认以二进制模式读取
    data = f.read(10)   # b'Sue@a el \xe5'
# 汉字是乱码
print(data)

# print(data.decode('utf-8'))
# 解码时报错：UnicodeDecodeError: 'utf-8' codec can't decode byte 0xe5 in position 9: unexpected end of data

path = 'F:/DataSet/BinarycodeAndTextcode.txt'
sink_path = 'sink.txt'
with open(path, encoding='utf-8') as source:
    # x 只写模式：但存在同名路径时会创建失败 ： FileExistsError: [Errno 17] File exists: 'sink.txt'
    with open(sink_path, 'wt', encoding='utf-8') as sink: # x代表只写，t代表文件的文本模式(自动将字节解码为Unicode)
        sink.write(source.read())

# 打开sink_path路径下的文件，显示到控制台。
with open(path) as f:
    print(f.read(10))

f = open(path)

print(f.read(5))
print(f.seek(10))
print(f.read(1))

'''
注：'F:/DataSet/BinarycodeAndTextcode.txt'的文件内容  ： Sue@a el 国
可以自己随便填，进行测试。
'''
