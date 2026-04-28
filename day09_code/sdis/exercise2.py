# -*- coding: utf-8 -*-
"""
    @Author  : Zephyr
    @Date    : 2026/4/27 11:13
    @Project  : PythonProject
    @File     : exercise2.py
    @IDE      : PyCharm
    @Description: 
"""
# ## 练习题1：成绩计算器
#
# **题目描述：**
# 编写一个程序，让用户输入学生的考试成绩（整数），然后计算这些成绩的平均分。程序需要：
#
# - 循环接收用户输入的成绩，输入"-1"时停止输入
# - 使用try-except处理输入错误（非整数输入）
# - 当输入非整数时，提示"输入无效，请输入整数"
# - 使用else子句在成功输入时累加成绩
# - 使用finally子句在每次输入后打印"当前已输入 X 个有效成绩"
# - 最后显示平均分（保留两位小数）

# def calculate_average():
#     total = 0
#     count = 0
#     while True:
#         try:
#             score = int(input("请输入成绩（输入'-1'结束）："))
#             if score == -1:
#                 break
#             total += score
#             count += 1
#         except ValueError:
#             print("输入无效，请输入整数")
#             continue
#     if count == 0:
#         print("没有有效成绩输入")
#         return
#     average = total / count
#     print(f"平均成绩为：{average:.2f}")
#     return average
#
# calculate_average()

## 练习题2：列表元素访问器

# **题目描述：**
# 创建一个包含10个随机整数的列表（1-100之间）。让用户输入索引值来访问列表中的元素。程序需要：
#
# - 预设列表：`numbers = [23, 45, 67, 89, 12, 34, 56, 78, 90, 21]`
# - 让用户输入索引（整数）
# - 使用try-except处理两种异常：
#   - 输入不是整数时，提示"请输入整数索引"
#   - 索引超出范围时，提示"索引超出范围，有效范围是0-9"
# - 使用else子句在成功访问时显示该位置的元素
# - 使用finally子句显示"索引访问尝试完成"
# - 程序持续运行直到用户输入"退出"

# def list_element_accessor():
#     numbers = [23, 45, 67, 89, 12, 34, 56, 78, 90, 21]
#     while True:
#         try:
#             index = int(input("请输入索引值（输入-1结束）："))
#             if index == -1:
#                 break
#             print(numbers[index])
#         except ValueError:
#             print("请输入整数索引")
#         except IndexError:
#             print("索引超出范围，有效范围是0-9")
#         finally:
#             print("索引访问尝试完成")
# list_element_accessor()

# ## 练习题3：文件读取统计器
#
# **题目描述：**
# 创建一个程序，要求用户输入文件名，然后读取该文件内容并统计文件中的单词数量。需要处理以下情况：
#
# - 如果文件不存在，提示"文件不存在，请检查文件名"
# - 如果文件存在但无法读取（如权限问题），提示"无法读取文件"
# - 如果文件读取成功，显示"文件包含 X 个单词"
# - 无论是否发生异常，都要打印"文件操作完成"
#
# 要求：分别使用finally关闭和with关闭完成

# def file_word_counter():
#     filename = input("请输入文件名：")
#     try:
#         with open(filename, 'r') as file:
#             content = file.read()
#             words = content.split()
#             print(f"文件包含 {len(words)} 个单词")
#     except FileNotFoundError:
#         print("文件不存在，请检查文件名")
#     except Exception as e:
#         print("无法读取文件")
#     finally:
#         print("文件操作完成")
#
# def file_word_counter1():
#     filename = input("请输入文件名：")
#     try:
#         file = open(filename, 'r')
#         content = file.read()
#         words = content.split()
#         print(f"文件包含 {len(words)} 个单词")
#     except FileNotFoundError:
#         print("文件不存在，请检查文件名")
#     except Exception as e:
#         print("无法读取文件")
#     finally:
#         file.close()
#         print("文件操作完成")
# file_word_counter1()

# ## 练习题4：文件合并工具
#
# **题目描述：**
# 编写一个程序，读取两个文本文件（data1.txt和data2.txt）的内容，然后将它们合并写入一个新的文件merged.txt中。程序需要：
#
# - 尝试读取data1.txt和data2.txt
# - 使用两个try-except块分别处理两个文件的读取
# - 如果某个文件不存在，使用空字符串替代该文件的内容，并提示"文件XXX不存在，使用空内容"
# - 如果文件存在但读取时发生其他错误（如权限问题），同样使用空字符串，并提示"读取文件XXX时发生错误"
# - 使用else子句在文件读取成功时显示"成功读取文件XXX"
# - 使用finally子句记录文件操作状态（无论成功与否都打印"处理文件XXX完成"）
# - 最后，将两个文件内容合并（用换行符分隔）写入merged.txt
# - 写入merged.txt时也要进行异常处理，如果写入失败，提示"无法创建合并文件"
#
# 要求：分别使用finally关闭和with关闭完成
def file_merge():
    try:
        with open('data1.txt', 'r') as file1:
            content1 = file1.read()
    except FileNotFoundError:
        print("文件不存在，使用空内容")
        content1 = ""
    except Exception as e:
        print("无法读取文件")
    else:
        print("成功读取文件data1.txt")
    finally:
        print("处理文件data1.txt完成")

    try:
        with open('data2.txt', 'r') as file2:
            content2 = file2.read()
    except FileNotFoundError:
        print("文件不存在，使用空内容")
        content2 = ""
    except Exception as e:
        print("无法读取文件")
    else:
        print("成功读取文件data2.txt")
    finally:
        print("处理文件data2.txt完成")

    try:
        with open('merged.txt', 'w') as merged_file:
            merged_file.write(content1 + '\n' + content2)
    except Exception as e:
        print("无法创建合并文件")
    else:
        print("成功创建合并文件merged.txt")
    finally:
        print("处理文件merged.txt完成")

file_merge()

# ## 练习题5：安全的数字输入处理
#
# **题目描述：**
# 编写一个程序，不断要求用户输入数字，直到用户输入"done"。程序需要：
#
# 1. 计算所有输入数字的总和和平均值
# 2. 处理无效输入（非数字）的情况，并提示"忽略无效输入"
# 3. 使用一个计数器跟踪有效输入的数量
# 4. 如果用户没有输入任何有效数字就输入"done"，引发一个自定义异常"NoValidNumbersError"，并捕获它，打印"没有输入任何有效数字"
# 5. 最后，无论是否发生异常，都要打印"程序结束"
#
# **要求：**
#
# - 定义自己的异常类NoValidNumbersError
# - 使用try-except-else-finally完整结构
# - 使用异常处理来控制程序流程

# class NoValidNumbersError(Exception):
#     """没有输入任何有效数字"""
#     def __str__(self):
#         return "没有输入任何有效数字" + self.message
#     def __repr__(self):
#         return "NoValidNumbersError"
#     def __init__(self, message):
#         self.message = message
#         super().__init__(message)
#
# def safe_input():
#     sum = 0
#     while True:
#         try:
#             value = input("请输入一个数字（或输入'done'结束）：")
#             if value == "-1":
#                 raise NoValidNumbersError("没有输入任何有效数字")
#             value = float(value)
#             sum += value
#         except ValueError:
#             print("忽略无效输入")
#         except NoValidNumbersError:
#             print("没有输入任何有效数字")
#             break
#     print(sum)
#
# safe_input()


# ## 练习题6：三角形
#
# **题目描述：**
#
# 编写一个函数，接收3个参数，代表三角形三条边。
#
# 1、如果参数不是整数或小数，抛出自定义异常"NotANumberError"
#
# 2、如果参数是数字但是不能构成三角形，抛出自定义异常"NotATriangleError"
#
# 3、如果参数没问题，则计算三角形的面积和周长
#
# 要求：
#
# - 自定义异常类NotANumberError 和 NotATriangleError

class NotANumberError(Exception):
    """参数必须是整数或小数"""
    pass

class NotATriangleError(Exception):
    """参数不能构成三角形"""
    pass

def triangle_area_perimeter(a, b, c):
    """计算三角形的面积和周长"""
    try:
        a = int(a)
        b = int(b)
        c = int(c)
        if a + b <= c or a + c <= b or b + c <= a:
            raise NotATriangleError("参数不能构成三角形")
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        perimeter = a + b + c
        return area, perimeter
    except ValueError:
        raise NotANumberError("参数必须是整数")
    except Exception as e:
        raise Exception("计算三角形面积和周长时发生错误")
    finally:
        print("三角形面积和周长计算完成")

area, perimeter = triangle_area_perimeter(3, 4, 5)
print(area, perimeter)

# 写一个dfs算法示例
