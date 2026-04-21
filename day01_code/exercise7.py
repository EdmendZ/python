# -*- coding: utf-8 -*-
"""
    @Author  : Zephyr
    @Date    : 2026/4/21 8:28
    @Project  : PythonProject
    @File     : exercise7.py
    @IDE      : PyCharm
    @Description: 
"""

# # 1. 字符串操作（5 题）
# # 1. 定义字符串 s = "Hello Python 123"，统计字符串中字母的个数。
# s = "Hello Python 123"
# print(sum(s[i].isalpha() for i in range(len(s))))
# # 2. 给定字符串 name = "  python learner  "，去除首尾空格，并将所有字母转为大写。
# name = "  python learner  "
# print(name.strip().upper())
# # 3. 截取字符串 s = "abcdefg"，输出第 3 个到第 6 个字符（包含两端）。
# s = "abcdefg"
# print(s[2:6])
# # 4. 判断字符串 tel = "13800138000" 是否全部由数字组成。
# tel = "13800138000"
# print(tel.isdigit())
# # 5. 将字符串 words = "python-java-c++" 按照 - 分割，得到列表。
# words = "python-java-c++"
# print(words.split("-"))


# # 2. 列表操作（5 题）
# # 1. 创建一个列表 nums = [1,2,3,4,5]，在列表末尾添加数字 6，在开头插入数字 0。
# nums = [1,2,3,4,5]
# nums.append(6)
# nums.insert(0, 0)
# print(nums)
# # 2. 列表 lst = [10,20,30,20,40,20]，删除列表中第一个 20。
# lst = [10,20,30,20,40,20]
# lst.remove(20)
# print(lst)
# # 3. 计算列表 scores = [88,92,76,90,85] 的总和和平均值。
# scores = [88,92,76,90,85]
# print(sum(scores))
# print(sum(scores) / len(scores))
# # 4. 反转列表 lst = [1,2,3,4]（直接修改原列表）。
# lst = [1,2,3,4]
# lst.reverse()
# print(lst)
# # 5. 列表 fruits = ["apple","banana","orange"]，判断 "apple" 是否在列表中。
# fruits = ["apple","banana","orange"]
# print("apple" in fruits)


# 3. 集合操作（5 题）
# 1. 创建集合 s1 = {1,2,3,4} 和 s2 = {3,4,5,6}，求两个集合的交集。
s1 = {1,2,3,4}
s2 = {3,4,5,6}
print(s1 & s2)
# 2. 向集合 s = {1,2} 中添加元素 3，删除元素 1。
s = {1,2}
s.add(3)
s.remove(1)
print(s)
# 3. 判断集合 a = {1,2} 是否是集合 b = {1,2,3} 的子集。
a = {1,2}
b = {1,2,3}
print(a.issubset(b))
# 4. 有两个列表 lst1 = [1,2,3,4]、lst2 = [3,4,5,6]，找出两个列表中都存在的元素。
lst1 = [1,2,3,4]
lst2 = [3,4,5,6]
print(set(lst1) & set(lst2))
# 5. 去除列表 lst = [5,2,5,1,2,1,3] 中的重复元素，并从小到大排序。
lst = [5,2,5,1,2,1,3]
print(sorted(set(lst)))
