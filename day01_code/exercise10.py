# -*- coding: utf-8 -*-
"""
    @Author  : Zephyr
    @Date    : 2026/4/22 8:53
    @Project  : PythonProject
    @File     : exercise10.py
    @IDE      : PyCharm
    @Description: 
"""
# ### 题目 1：函数定义与调用
#
# 定义一个函数 calculate，它接受两个整数参数 a 和 b，返回这两个数的商和余数，并调用该函数计算 15和4的商和余数。如果b为0，则商和余数为None。
def calculate(a, b):
    if b == 0:
        return None, None
    else:
        return a // b, a % b
quotient, remainder = calculate(15, 4)
print(quotient, remainder)

# ### 题目 2：默认参数
#
# 定义一个函数 greet，它接受一个字符串参数 name，并且有一个默认参数 message，默认值为 "Hello"，
# 函数功能是打印出问候语，如 "Hello, Alice"。调用该函数时，分别传入和不传入 message 参数进行测试。
def greet(name, message="Hello"):
    print(f"{message}, {name}")
    return f"{message}, {name}"
greet("Alice")


# ### 题目 3：可变参数
#
# 定义一个函数 find_all_even，它接受任意数量的整数参数，返回所有参数中的偶数。例如调用 find_all_even(1, 2, 3, 4, 5) 应返回 [2,4]。
def find_all_even(*args):
    return [num for num in args if num % 2 == 0]
even_nums = find_all_even(1, 2, 3, 4, 5)
print(even_nums)

# ### 题目 4：函数嵌套调用
#
# 定义两个函数，square 函数接受一个整数参数，返回该数的平方；cube 函数接受一个整数参数，通过调用 square 函数返回该数的立方（立方 = 平方 × 该数）。调用 cube 函数计算 3 的立方。
def square(x):
    return x ** 2
def cube(x):
    return square(x) * x
print(cube(3))

# ### 题目5：递归
#
# 通项公式如下：f(n)=n + (n-1) + (n-2) + .... + 1，其中n大于等于1，例如：f(5) = 5 + 4 + 3 + 2 + 1，f(10) = 10 + 9 + 8 + 7+ 6 + 5 + 4 + 3 + 2 + 1，请用递归的方式完成方法long f( int n)的方法体。
def f(n):
    if n == 1:
        return 1
    else:
        return n + f(n-1)
print(f(5))
