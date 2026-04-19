# -*- coding: utf-8 -*-
"""
    @Author  : Zephyr
    @Date    : 2026/4/18 17:26
    @Project  : PythonProject
    @File     : homework1.py
    @IDE      : PyCharm
    @Description:
"""

# ### 题1：使用for循环，完成打印
#
# ```
#     *
#    ***
#   *****
#  *******
#   *****
#    ***
#     *
# ```

# 假设菱形最宽处为 7 个星号
n = 7
mid = n // 2 + 1

for i in range(1, mid + 1):
    print(" " * (mid - i), end="")
    print("*" * (2 * i - 1))

# 下半部分
for i in range(mid - 1, 0, -1):
    print(" " * (mid - i), end="")
    print("*" * (2 * i - 1))

print("=" * 20)

# ### 题2：使用for循环，完成打印
#
# ```
#     *
#    * *
#   *   *
#  *     *
#   *   *
#    * *
#     *
# ```
# 假设菱形最宽处为 7 个位置
n = 7
mid = n // 2 + 1

for i in range(1, mid + 1):
    print(" " * (mid - i), end="")
    if i == 1:
        print("*")
    else:
        # * + " " + *
        # " " = 2 * row - 3
        print("*" + " " * (2 * i - 3) + "*")

for i in range(mid - 1, 0, -1):
    print(" " * (mid - i), end="")
    if i == 1:
        print("*")
    else:
        print("*" + " " * (2 * i - 3) + "*")

# ### 题3：最大公约数和最小公倍数
#
# 从键盘输入2个自然数m和n（自然数必须是大于0），求它们的最大公约数和最小公倍数
import math

m = int(input("Please input m: "))
n = int(input("Please input n: "))

if m <= 0 or n <= 0:
    print("must be greater than 0")
    exit()

gcd = math.gcd(m, n)
lcm = (m * n) // gcd

print(f"gcd: {gcd}")
print(f"lcm: {lcm}")

# ### 题4：打鱼还是晒网
#
# 假设张三从2000年1月1日开始执行3天打鱼2天晒网的生活安排，李四打算在xx年xx月xx日找张三喝酒，判断哪一天张三有空吗
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def solve_fishing():
    end_year = int(input("Please input year: "))
    end_month = int(input("Please input month: "))
    end_day = int(input("Please input day: "))

    months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    res = 0

    for y in range(2000, end_year):
        if is_leap_year(y):
            res += 366
        else:
            res += 365

    if is_leap_year(end_year):
        months[2] = 29

    for m in range(1, end_month):
        res += months[m]

    res += end_day

    cycle_status = res % 5

    if 1 <= cycle_status <= 3:
        print("Zhang San is fishing, is not available")
    else:
        print("Zhang San is drying nets, is available")


solve_fishing()
