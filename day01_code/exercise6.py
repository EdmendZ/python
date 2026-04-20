# -*- coding: utf-8 -*-
"""
    @Author  : Zephyr
    @Date    : 2026/4/20 11:03
    @Project  : PythonProject
    @File     : exercise6.py
    @IDE      : PyCharm
    @Description:
"""


# ### 练习题1：随机数列表
#
# 1. 定义一个包含 10 个随机整数（范围 1-100）的列表（可手动输入或用 random 模块）
# 2. 打印列表的长度、最大值、最小值、总和
# 3. 打印列表中索引为 5 的元素，以及最后 3 个元素（切片）
# 4. 统计列表中数字`50`出现的次数
# 5. 遍历列表，打印每个元素的索引和值（用 enumerate）
# import random
# numbers = [random.randint(1, 100) for _ in range(10)]
# print(numbers)
# print(f"列表长度: {len(numbers)}")
# print(f"最大值: {max(numbers)}")
# print(f"最小值: {min(numbers)}")
# print(f"总和: {sum(numbers)}")
# print(f"索引为 5 的元素: {numbers[5]}")
# print(f"最后 3 个元素: {numbers[-3:]}")
# print(f"数字 50 出现次数: {numbers.count(50)}")
# for num in enumerate(numbers):
#     print(f"索引: {num[0]}, 值: {num[1]}")


# ### 练习题2：成绩分析
#
# 给定学生成绩列表 `scores = [78, 92, 85, 69, 100, 88, 75, 92, 100, 85]`，完成以下操作：
#
# 1. 计算班级的平均分（总和 / 人数），保留 1 位小数
# 2. 找出最高分和最低分，并打印 “最高分：XX，最低分：XX”
# 3. 检查是否有学生考了满分（100 分），有则打印 “有满分，满分有x个”，无则打印 “无满分”
# 4. 通过切片获取成绩列表中前 5 个分数，计算其平均分
# 5. 遍历成绩列表，打印 “第 X 个学生的成绩是：XX”（X 从 1 开始）
# scores = [78, 92, 85, 69, 100, 88, 75, 92, 100, 85]
# print(f"平均分: {round(sum(scores) / len(scores), 1)}")
# print(f"最低分: {min(scores)}")
# print(f"最高分: {max(scores)}")
# print(f"是否有满分: {'有' if 100 in scores else '无'}")
#
# print(f"前 5 个学生的平均分: {round(sum(scores[:5]) / 5, 1)}")
# for score in enumerate(scores):
#     print(f"第 {score[0]+1} 个学生的成绩是: {score[1]}")

# # ### 练习题3：列表
# #
# # 1）给定一个列表 numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]，编写一个程序，将列表中所有的偶数元素删除
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# numbers = [num for num in numbers if num % 2 != 0]
# print(numbers)

# # ### 练习题4：列表
# #
# # 2）创建一个空列表 fruits，然后添加 "apple", "banana", "cherry", "date" 四个元素。接着在列表的开始添加 "elderberry"，在 "cherry" 之前添加 "fig"，并将列表的最后一个元素替换为 "grape"。
# fruits = []
# fruits.append("apple")
# fruits.append("banana")
# fruits.append("cherry")
# fruits.append("date")
# fruits.insert(0, "elderberry")
# cherry_index = fruits.index("cherry")
# fruits.insert(cherry_index, "fig")
# fruits[-1] = "grape"
# print(fruits)

# # ### 练习题5：列表
# #
# # 3）给定一个列表 prices = [10.5, 20.0, 15.75, 8.2, 12.0]，编写一个程序，将列表中的元素都乘以 1.1（表示增加 10%），并将结果存储在一个新列表 new_prices 中。
# prices = [10.5, 20.0, 15.75, 8.2, 12.0]
# new_prices = [price * 1.1 for price in prices]
# print(new_prices)



# # ### 练习题6：列表
# #
# # 4）有两个列表 list1 = [1, 2, 3, 4, 5] 和 list2 = [6, 7, 8, 9, 10]，将它们合并为一个新列表 combined_list，并对 combined_list 进行降序排序
# list1 = [1, 2, 3, 4, 5]
# list2 = [6, 7, 8, 9, 10]
#
# combined_list = list1 + list2
# combined_list.sort(reverse=True)
# print(combined_list)

# ### 练习题7：列表
# # 从控制台输入一句话，包含中英文等多种字符，然后将里面的英文字母筛选出来构成一个新列表（使用列表推导式）
# # 1. 从控制台输入一句话
# text = input("请输入一句话：")
# # 2. 使用列表推导式筛选英文字母
# # isalpha() 方法可以判断字符是否为字母（包括中文和英文）
# # isascii() 方法用于确保字符属于 ASCII 编码（排除中文字符）
# # 组合起来：char.isalpha() and char.isascii() 就能精准锁定英文字母
# letters = [char for char in text if char.isalpha() and char.isascii()]
#
# print("筛选出的英文字母列表：", letters)


# ### 练习题8：列表
#
# 从控制台输入一组单词放到列表中，直到输入exit（不放到列表）结束，统计最长的字符串
words = []
while True:
    word = input("请输入一个单词（输入 'exit' 结束）：")
    if word == "exit":
        break
    words.append(word)

print("最长的字符串是：", max(words, key=len))

# ### 练习题9：集合操作
# #
# # 随机产生一组[1,100]的偶数，放到集合中，使得集合长度正好为10。提示：random.randint(a,b)可以产生[a,b]的随机整数
# import random
#
# even_numbers = {random.randint(1, 100) for _ in range(10)}
# print(even_numbers)


# ### 练习题10：集合操作
#
# # 现有集合 set1 = {1, 2, 3, 4, 5} 和 set2 = {3, 4, 5, 6, 7} 。
# #
# # 1. 求这两个集合的并集。
# #
# # 1. 求这两个集合的交集。
# #
# # 1. 从 set1 中移除元素 3 。
# set1 = {1, 2, 3, 4, 5}
# set2 = {3, 4, 5, 6, 7}
# print(set1.union(set2))
# print(set1.intersection(set2))
# set1.discard(3)
# print(set1)

# ### 练习题11：统计字母出现次数
#
# 给定字符串 "Atguigu is a Good place"统计出现次数最多的字母，Aa不区分
import collections

text = "Atguigu is a Good place"
text = text.lower()
letter_counts = collections.Counter(char for char in text if char.isalpha() and char.isascii())
print(letter_counts.most_common(1)[0][0])



# ### 练习题12：字典
#
# 给定一个字典 student_scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 88}，编写一个程序，
#
# （1）增加一个新学生的成绩：Lily成绩60
#
# （2）查看Alice成绩
#
# （3）删除Bob的成绩信息
#
# （4）将每个学生的分数增加 5 分，并将结果存储在一个新的字典 updated_scores 中。
student_scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 88}

student_scores["Lily"] = 60
print(student_scores["Alice"])
del student_scores["Bob"]
updated_scores = {student: score + 5 for student, score in student_scores.items()}
print(updated_scores)


# ### 练习题13：字典
#
# 给定一个字典 fruit_prices = {"apple": 1.2, "banana": 0.5, "cherry": 2.5, "date": 3.0}，编写一个程序，找出价格最高的水果及其价格。
fruit_prices = {"apple": 1.2, "banana": 0.5, "cherry": 2.5, "date": 3.0}
print(max(fruit_prices, key=fruit_prices.get), fruit_prices[max(fruit_prices, key=fruit_prices.get)])


