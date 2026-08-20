# Day 2 练习：变量、数据类型、if 判断
# 运行：python 02_basics.py

import sys
sys.stdout.reconfigure(encoding="utf-8")  # 让 Windows 终端正常显示中文

# 四种不同的数据类型
b = [1, 2, 3, 4, 'a']          # 列表 list
c = {'a': 1, 'b': 2, 'd': 3}   # 字典 dict
e = 'abc'                      # 字符串 str
f = (1, 3, 4, 5)               # 元组 tuple

# 遍历列表，逐个判断元素是不是整数
for i in b:
    if isinstance(i, int):
        print(i, 'is int')
    else:
        print(i, 'is not int')

# 用 isinstance 判断各变量的类型
# 字典
if isinstance(c, dict):
    print(c, 'is dict')
else:
    print(c, 'is not dict')
# 字符串
if isinstance(e, str):
    print(e, 'is str')
else:
    print(e, 'is not str')
# 列表
if isinstance(b, list):
    print(b, 'is list')
else:
    print(b, 'is not list')
# 元组
if isinstance(f, tuple):
    print(f, 'is tuple')
else:
    print(f, 'is not tuple')
