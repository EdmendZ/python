# -*- coding: utf-8 -*-
"""
    @Author  : Zephyr
    @Date    : 2026/4/21 18:54
    @Project  : PythonProject
    @File     : exercise9.py
    @IDE      : PyCharm
    @Description: 
"""

# ### 1、练习题：
#
# 定义一个函数，功能是将序列容器（以list、tuple、str为例）中的首尾元素删除，请问该如何设计这个函数？
# 是否需要返回删除首尾元素后的容器对象？
# 提示：判断类型   isinstance(对象,类型)
# def delete_first_last(obj):
#     if not isinstance(obj, (list, tuple, str)):
#         return None
#     if len(obj) <= 2:
#         return []
#     else:
#         return obj[1:-1]
# print(delete_first_last([1, 2, 3, 4, 5]))



# ### 2、练习题：
#
# 定义一个函数，功能是交换2个变量的值，请问该如何设计这个函数？能否实现？
# def swap(a, b):
#     return b, a
# print(swap(1, 2))
# ### 3、可变参数练习题
#
# 定义一个函数calculate，功能可以接收2个整数，及其任意个运算符，实现对这2个整数的计算。
# 如果没有传入运算符，返回None
# calculate(1,2) 返回None
# calculate(1,2,"+") 返回3
# calculate(1,2,"+","-","*","/"), 返回[3,-1,2,0.5]

# def calculate(a,b, *operator):
#     if not operator:
#         return None
#     result = []
#     for p in operator:
#         match p:
#             case "+":
#                 result.append(a+b)
#             case "-":
#                 result.append(a-b)
#             case "*":
#                 result.append(a*b)
#             case "/":
#                 result.append(a/b)
#             case _:
#                 pass
#     return result
#
# #测试
# print(calculate(1,2))
# print(calculate(1,2,"+"))
# print(calculate(1,2,"+","-","*","/"))
# (2)定义一个函数 find_info(*name, **note_book)， name代表你要查找的用户的姓名，note_book代表通讯录，
# 通讯录的key是用户姓名，value是用户电话号码，最后可以返回所有name对应的电话号码的列表。
# find_info("张三","李四", 张三="1111",王五="3333") 返回 ["1111"]

def find_info(*name, **note_book):
    result = []
    for k, v in note_book.items():
        if k in name:
            result.append(v)
    return result

print(find_info("张三","李四", 张三="1111",王五="3333"))

# ### 4、走台阶（递归）
#
# （2）如果走台阶，一次只能跨1步或2步，台阶数量共10级，请问共有多少种走法。
def climb(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return climb(n-1) + climb(n-2)
print(climb(10))

# ### 5、猴子吃桃（递归）
#
# 一个猴子第一天摘了n个桃子，从第一天开始，每天吃剩余桃子数量的一半+1个桃子，
# 第10天只有1个桃子了，问第一天摘了多少桃子。
def eat(n):
    if n == 1:
        return 1
    else:
        return (eat(n-1) + 1) * 2
print(eat(10))


# ### 6、不死神兔（递归）
#
# 案例需求：
#
# 用递归实现不死神兔：故事得从西元1202年说起，话说有一位意大利青年，名叫斐波那契。在他的一部著作中提出了一个有趣的问题：假设一对刚出生的小兔一个月后就能长成大兔，再过一个月就能生下一对小兔，并且此后每个月都生一对小兔，没有发生死亡，问：现有一对刚出生的兔子2年后(24个月)会有多少对兔子?
def rabbit(n):
    if n == 1 or n == 2:
        return 1
    else:
        return rabbit(n-1) + rabbit(n-2)
    # 大兔子才能生小兔子 两个月前的兔子数量就是当前月的大兔子数量 一个月前的兔子数量就是当前月的小兔子数量
# 1(1) 2(1+1) 3(2+1) 4(3+1)
# ### 7、通项公式（递归）
#
# 案例需求：通项公式如下：f(n)=n + (n-1) + (n-2) + .... + 1，其中n是大于等于5并且小于10000的整数，例如：f(5) = 5 + 4 + 3 + 2 + 1，f(10) = 10 + 9 + 8 + 7+ 6 + 5 + 4 + 3 + 2 + 1，请用递归的方式完成方法long f( int n)的方法体。
def f(n):
    if n == 1:
        return 1
    else:
        return f(n-1) + n
print(f(10))


import functools
import heapq
list_demo = [3, 5, 6, 2, 1, 8, 4, 9, 10]
print("累加：", functools.reduce(lambda a, b: a + b, list_demo))
print("最大值：", functools.reduce(lambda a, b: a if a > b else b, list_demo))
print("最小值：", functools.reduce(lambda a, b: a if a < b else b, list_demo))
print("最大的3个偶数：", heapq.nlargest(3, list_demo, key=lambda x: x if x % 2 == 0 else float('-inf')))
print("最小的3个奇数：", heapq.nsmallest(3, list_demo, key=lambda x: x if x % 2 != 0 else float('inf')))
print(heapq.nlargest(3, list_demo))