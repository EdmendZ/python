# -*- coding: utf-8 -*-
"""
    @Author  : Zephyr
    @Date    : 2026/4/17 19:40
    @Project  : PythonProject
    @File     : test.py
    @IDE      : PyCharm
    @Description: 
"""
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# print(f"切片[5::-1]范围: {nums[5::-1]}")
# print(f"切片[5:-1:-1]范围: {nums[5:-1:-1]}")


def func(*data):
    print(data)        # 输出: (1, 2, 3)
    print(type(data))  # 输出: <class 'tuple'>


func()
