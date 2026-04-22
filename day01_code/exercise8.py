# -*- coding: utf-8 -*-
"""
    @Author  : Zephyr
    @Date    : 2026/4/21 15:20
    @Project  : PythonProject
    @File     : exercise8.py
    @IDE      : PyCharm
    @Description: 
"""

# 题1：默认值参数
# 编写函数 calc_area(width, height, unit="cm")
# 计算矩形面积：面积 = 宽 × 高，输出格式：矩形面积：xx 平方xx
# 分别使用位置传参和关键字传参调用 calc_area 函数。
def calc_area(width, height, unit="cm"):
    area = width * height
    print(f"矩形面积：{area} 平方{unit}")

# 使用位置传参调用函数
calc_area(5, 10)
calc_area(width=5, height=10, unit="cm")

# 题2：可变传参
# 编写函数实现拼接任意个字符串，并且字符串之间使用 - 分割，concat(*args)。
# 如果没有传入字符串，则返回空字符串。
# 如果传入1个字符串，则返回这1个字符串。如果传入多个字符串，则返回使用 - 分割拼接后的字符串。
def concat(*args):
    if not args:
        return ""
    elif len(args) == 1:
        return args[0]
    else:
        return "-".join(args)

print(concat("a", "b", "c"))

# 题3：可变传参
# 编写函数 cal_max(*nums) 求任意个整数的最大值。如果没有传入整数，则返回None。
def cal_max(*nums):
    if not nums:
        return None
    else:
        return max(nums)

print(cal_max(1, 2, 3, 4, 5))

# 题4：可变传参
# 编写函数 cal_perimeter(name, *base)，求某个图形的周长
# name 表示图形的名称，base 表示图形的边长。输出格式：xx的周长：xx
def cal_perimeter(name, *base):
    if not base:
        return None
    else:
        perimeter = sum(base)
        print(f"{name}的周长：{perimeter}")
        return perimeter

cal_perimeter("矩形", 5, 10)
cal_perimeter("三角形", 3, 4, 5)

# 题5：参数
# 编写函数 print_rectangle(line, column, sign='*')，实现打印 line 行 column 列由 sign 接收的字符组成的矩形。
# 如果 sign 没有接收参数，则图形由 * 组成。line 和 column 必须是正整数，否则不打印。
def print_rectangle(line, column, sign='*'):
    if line <= 0 or column <= 0:
        return None
    else:
        for i in range(line):
            for j in range(column):
                print(sign, end="")
            print()
print_rectangle(5, 10, '*')

# 题6：参数、列表
# 编写函数 cal_list_max(list_one, list_two) 实现找出2个列表中所有元素的最大值，可以使用 max 函数找最大值，通过 解包 传参调用 max 函数。
def cal_list_max(list_one, list_two):
    if not list_one and not list_two:
        return None
    else:
        return max(list_one + list_two)
print(cal_list_max([1, 2, 3], [4, 5, 6]))
