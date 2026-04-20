# -*- coding: utf-8 -*-
"""
    @Author  : Zephyr
    @Date    : 2026/4/20 8:27
    @Project  : PythonProject
    @File     : exercise5.py
    @IDE      : PyCharm
    @Description: 
"""
# 题目要求：
# 编写一个 Python 程序，输入一个整数，判断它是正数、负数还是零，正数输出 positive，负数输出 negative，0 输出 zero。
num = int(input("请输入一个整数："))

if num > 0:
    print("positive")
elif num < 0:
    print("negative")
else:
    print("zero")

# 题目 2：循环控制
# 题目要求：
# 编写一个 while 循环，计算 100 到 1000 的整数之和。
sum = 0
for i in range(100, 1001):
    sum += i
print(sum)

# 题目 3：输出 100~1000 中的所有水仙花数
# 题目要求：
# 水仙花数：3 位正整数等于各个位数字的立方和。
for i in range(100, 1000):
    a = i // 100
    b = i // 10 % 10
    c = i % 10

    if a**3 + b**3 + c**3 == i:
        print(i)

# 题目 4：字符串逆序输出
# 题目要求：
# 编写程序，接收用户输入的一个字符串，使用 循环 将字符串中的字符逆序输出。例如：输入 "hello"，输出 "olleh"。
s = input("请输入一个字符串：")
for i in range(len(s)-1, -1, -1):
    print(s[i], end="")





