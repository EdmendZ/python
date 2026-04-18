# -*- coding: utf-8 -*-
"""
    @Author  : Zephyr
    @Date    : 2026/4/17 11:42
    @Project  : PythonProject
    @File     : exercise2.py
    @IDE      : PyCharm
    @Description: 
"""

# Q1 输入 2 个整数，求它们的和、差、乘积、商。
num1 = int(input("请输入第一个整数: "))
num2 = int(input("请输入第二个整数: "))

sum_val = num1 + num2
diff_val = num1 - num2
prod_val = num1 * num2
quot_val = num1 / num2

print(f"和: {sum_val}")
print(f"差: {diff_val}")
print(f"乘积: {prod_val}")
print(f"商: {quot_val}")

# Q2 定义变量 r 代表圆的半径，求面积和周长，并保留小数点后 2 位
import math

r = float(input("请输入圆的半径: "))

area = math.pi * r * r
perimeter = 2 * math.pi * r

print(f"面积: {area:.2f}")
print(f"周长: {perimeter:.2f}")

# Q3 输入一个三位数的正整数，求它的百位、十位、个位。
num = int(input("请输入一个三位数的正整数: "))

hundreds = num // 100
tens = (num // 10) % 10
ones = num % 10

print(f"百位: {hundreds}")
print(f"十位: {tens}")
print(f"个位: {ones}")

# Q4 输入一个整数，判断它是不是偶数，同时是 3 的倍数
num = int(input("请输入一个整数: "))
if num % 2 == 0 and num % 3 == 0:
    print("是偶数且是 3 的倍数\n")
else:
    print("不是偶数或不是 3 的倍数\n")

# Q5 输入一个整数，判断它是不是满足：3 的倍数、或 5 的倍数、或 7 的倍数。
num = int(input("请输入一个整数: "))
if num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
    print("是 3 的倍数、或 5 的倍数、或 7 的倍数\n")
else:
    print("不是 3 的倍数、也不是 5 的倍数、也不是 7 的倍数\n")

# Q6 输入：一个整数，代表完成某个任务所需的总小时数。
# 目标：计算该任务至少需要几天。
num_hours = int(input("请输入完成任务任务所需的总小时数: "))
num_days = num_hours // 8
print(f"至少需要 {num_days} 天来完成任务")

