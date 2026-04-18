# -*- coding: utf-8 -*-
"""
    @Author  : Zephyr
    @Date    : 2026/4/17 19:40
    @Project  : PythonProject
    @File     : test.py
    @IDE      : PyCharm
    @Description: 
"""
# 1. 布尔值 False
if False:
    print("不会执行")
else:
    print("1. False 是假")

# 2. 空值 None
if None:
    print("不会执行")
else:
    print("2. None 是假")

# 3. 数字 0 (包括整数、浮点数)
if 0:
    print("不会执行")
else:
    print("3. 数字 0 是假")

if 0.0:
    print("不会执行")
else:
    print("4. 浮点数 0.0 也是假")

# 5. 空字符串
if "":
    print("不会执行")
else:
    print("5. 空字符串是假")

# 6. 空列表、空字典、空元组
if []:
    print("不会执行")
else:
    print("6. 空列表是假")

if {}:
    print("不会执行")
else:
    print("7. 空字典是假")


