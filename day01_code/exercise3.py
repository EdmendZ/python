# -*- coding: utf-8 -*-
"""
    @Author  : Zephyr
    @Date    : 2026/4/18 8:33
    @Project  : PythonProject
    @File     : exercise3.py
    @IDE      : PyCharm
    @Description: 
"""
from functools import total_ordering

# 题目1：原码、反码、补码（1个字节为例）
# 需求：正数19和负数-19的原码、反码、补码表示（1字节=8位）。

# 1个字节=8位，最高位为符号位（0正1负）
# 正数19的原码、反码、补码：
# 1. 计算19的二进制（7位数值位）：19 = 16+2+1 = 0b10011 → 补零为7位：0010011
# 2. 原码：符号位0 + 数值位 → 0 0010011 → 00010011（8位）
# 3. 反码=原码（正数）→ 00010011
# 4. 补码=反码（正数）→ 00010011

# 负数-19的原码、反码、补码：
# 1. 原码：符号位1 + 数值位（19的二进制）→ 1 0010011 → 10010011（8位）
# 2. 反码：符号位不变，数值位取反 → 1 1101100 → 11101100
# 3. 补码：反码+1 → 11101100 + 1 = 11101101

# # 题目2：订单满减活动
# # 需求：输入订单总价，满200减30，否则不减，输出结算价。
# # 核心逻辑：条件判断（if语句）。
# total_price = float(input("请输入订单总价："))
# if total_price >= 200:
#     print("满200减30，结算价为：", total_price - 30)
# else:
#     print("不满200，结算价为：", total_price)
#
# # 题目3：总秒数转分钟和剩余秒数
# # 需求：输入总秒数，输出分钟数和剩余秒数。
# # 核心逻辑：整数除法（//）求分钟，取余（%）求剩余秒数。
# total_seconds = int(input("Please input the total seconds"))
# min = total_seconds // 60
# sec = total_seconds % 60
# print(f"min:{min},sec:{sec}")
#
# # 题目4：温度换算（华氏度→摄氏度）
# # 需求：输入华氏度，转换为摄氏度，分别显示两种单位。
# # 核心逻辑：公式 ℃ = (℉ - 32) / 1.8
# f = float(input("Please input the frequence"))
# c= (f - 32) / 1.8
# print(f"c:{c}")
#
# # 题目5：100天后是周几
# # 需求：今天是周6（week=6），计算100天后是周几（显示周1~周日）。
# # 核心逻辑：一周7天，用取余（%）计算偏移量。
# week = int(input("Please input the week"))
# move = 100 % 7
# if (week + move) % 7 == 0:
#     result = 7
# else:
#     result= (week + move) % 7
#
# print(f"result:{result}")
#
# # 题目6：计算BMI值
# # 需求：输入身高（米）、体重（千克），计算BMI（保留两位小数），公式 BMI = 体重 / 身高²。
# # 核心逻辑：数学运算（平方、除法）。
# weight = float(input("Please input the weight"))
# height = float(input("Please input the height"))
# bmi = weight / height ** 2
# print(f"bmi:{bmi:.2f}")


# # 题目7：男生女生人数占比
# # 需求：输入男生、女生人数，计算各自占总人数的百分比（保留两位小数）。
# # 核心逻辑：百分比公式 占比 = (部分人数 / 总人数) × 100。
# male_num = int(input("please input the male number:"))
# female_num = int(input("please input the female number:"))
# total_num = male_num + female_num
# print(f"male_ratio:{male_num / total_num:.2%}")
# print(f"female_ratio:{female_num / total_num:.2%}")

# 题目8：计算2与自然数n的最小公倍数（最快方式）
# 需求：用最快方式计算2与自然数n的最小公倍数（LCM）。
# 核心逻辑：最小公倍数公式 LCM(a,b) = |a*b| / GCD(a,b)（GCD为最大公约数）。
# 当n为偶数时，2和n的GCD为2，LCM=n（因为n是2的倍数）。
# 当n为奇数时，2和n的GCD为1，LCM=2*n（互质）。
# 最大公约数    greatest common divisor
# 最小公倍数    least common multiple
import math
a = int(input("Please input the first number"))
b = int(input("Please input the second number"))

lcm = abs(a * b) // math.gcd(a, b)
print(f"lcm:{lcm}")

# n if n%2==0 else 2*n
# n << (n&1)