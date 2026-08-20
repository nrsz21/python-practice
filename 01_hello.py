# 我的第一个 Python 程序
# 运行方法：在项目目录下执行  python 01_hello.py

import sys
sys.stdout.reconfigure(encoding="utf-8")  # 让 Windows 终端正常显示中文

# 1. 输出文字
print("你好，世界！")

# 2. 变量和字符串
name = "沈德圣"
print("我叫", name)

# 3. 数字计算
year = 2026
print("现在是", year, "年")

# 4. 一个简单的判断
score = 60
if score >= 60:
    print("及格了，加油！")
else:
    print("还差一点，继续努力")

# 5. 循环输出
for i in range(1, 6):
    print("第", i, "天打卡")
