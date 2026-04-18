# -*- coding: utf-8 -*-
"""
    @Author  : Zephyr
    @Date    : 2026/4/18 10:16
    @Project  : PythonProject
    @File     : exercise4.py
    @IDE      : PyCharm
    @Description: 
"""
# # 练习题1：
# #
# #     从控制台输入1个整数，
# #     如果它是3的倍数，输出 foo
# #     如果它是5的倍数，输出 baz
# #     如果它是7的倍数，输出 biz
# num = int(input("请输入一个整数: "))
# if num % 3 == 0:
#     print("foo")
# if num % 5 == 0:
#     print("baz")
# if num % 7 == 0:
#     print("biz")
#
#
# # 练习题2：
# #
# #     从键盘输入3个整数，按照从小到大输出
# #     例如：输入5,6,4   输出4,5,6
# a = int(input("请输入第一个整数: "))
# b = int(input("请输入第二个整数: "))
# c = int(input("请输入第三个整数: "))
# if a > b:
#     a, b = b, a
# if a > c:
#     a, c = c, a
# if b > c:
#     b, c = c, b
# print(a, b, c)
#
#
# # 练习题3：输入年月，输出该月总天数有几天
# #
# #     例如：输入年份：2026，月份：2     输出：2026年2月有28天
# year = int(input("请输入年份: "))
# month = int(input("请输入月份: "))
# if month == 2:
#     if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#         print(f"{year}年{month}月有29天")
#     else:
#         print(f"{year}年{month}月有28天")
# elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
#     print(f"{year}年{month}月有31天")
# else:
#     print(f"{year}年{month}月有30天")

# # 练习题4：
# #
# # 给定一个三位的状态码，左边第一位标识大小写状态（1-大写，0-小写），
# #         第二位标识输入法语言（1-简体中文，0-英语），
# #         第三位标识输入法模式（1-中文，0-英文）。
# #     例如：状态码  0B011 或 0B110 或 0B000
# #     state = 0B011
# #     判断输入法的状态：
# #     - 如果是大写状态，打印“大写状态”。
# #     - 如果不是大写状态，判断输入法语言是“简体中文-微软拼音”还是“英语-美式键盘”。
# #     - 如果是“简体中文-微软拼音”，判断是中文模式还是英文模式，并打印。
# #     - 如果是“英语-美式键盘”，打印“英语-美式键盘”。
# code = int(input("请输入状态码: "), 2)
# if code & 0b100 != 0:
#     print("大写状态")
# else:
#     if code & 0b10 == 0:
#         print("英语-美式键盘")
#     else:
#         print("简体中文-微软拼音")
#     if code & 0b1 == 0:
#         print("英文模式")
#     else:
#         print("中文模式")

# # 练习题6：输出1-100之间的偶数
# for i in range(1, 101):
#     if i % 2 == 0:
#         print(i)


# # 练习题7：统计正负数个数
# # 从键盘不断输入整数，统计输入的正整数、负整数的个数，输入0循环结束。
# positive_integer_count = 0
# negative_integer_count = 0
# while True:
#     num = int(input("请输入一个整数: "))
#     if num > 0:
#         positive_integer_count += 1
#     elif num < 0:
#         negative_integer_count += 1
#     else:
#         break
#
# print("当前输入的正整数个数:", positive_integer_count)
# print("当前输入的负整数个数:", negative_integer_count)



# # 练习题8：猜数
# #
# #     先随机产生1个[1,100]范围的整数，提示 random.randint(a,b)产生[a,b]范围的整数。
# #     从键盘输入数字num，猜随机产生的数是多少。例如：随机数是45
# #     如果猜大了，提示大了。例如输入50，提示大了，范围在[1,50]之间,
# #     如果猜小了，提示小了。例如输入25，提示小了，范围在[25,50]之间,
# import random
# random_number = random.randint(1, 100)
# print(f"随机数是{random_number}")
# min_bound = 1
# max_bound = 100
# while True:
#     guess = int(input("请输入你的猜测: "))
#     if guess == random_number:
#         print("恭喜，猜对了！")
#         break
#     elif guess > random_number:
#         if max_bound > guess - 1:
#             max_bound = guess - 1
#         print(f"大了，范围在[{min_bound},{guess - 1}]之间")
#     elif guess < random_number:
#         if min_bound < guess + 1:
#             min_bound = guess + 1
#         print(f"小了，范围在[{guess + 1},{max_bound}]之间")


# # 练习题9：统计正负数个数
# #
# # 从键盘不断输入整数，统计输入的正整数个数，输入0循环结束。忽略负数（使用continue）
# positive_integer_count = 0
#
# while True:
#     num = int(input("请输入一个整数: "))
#     if num == 0:
#         break
#     if num > 0:
#         positive_integer_count += 1
#     else:
#         continue
# print(f"当前输入的正整数个数: {positive_integer_count}")

# # 练习题10：使用for循环完成九九乘法表
# #
# # 1 * 1 = 1
# # 2 * 1 = 2	2 * 2 = 4
# # 3 * 1 = 3	3 * 2 = 6	3 * 3 = 9
# # 4 * 1 = 4	4 * 2 = 8	4 * 3 = 12	4 * 4 = 16
# # 5 * 1 = 5	5 * 2 = 10	5 * 3 = 15	5 * 4 = 20	5 * 5 = 25
# # 6 * 1 = 6	6 * 2 = 12	6 * 3 = 18	6 * 4 = 24	6 * 5 = 30	6 * 6 = 36
# # 7 * 1 = 7	7 * 2 = 14	7 * 3 = 21	7 * 4 = 28	7 * 5 = 35	7 * 6 = 42	7 * 7 = 49
# # 8 * 1 = 8	8 * 2 = 16	8 * 3 = 24	8 * 4 = 32	8 * 5 = 40	8 * 6 = 48	8 * 7 = 56	8 * 8 = 64
# # 9 * 1 = 9	9 * 2 = 18	9 * 3 = 27	9 * 4 = 36	9 * 5 = 45	9 * 6 = 54	9 * 7 = 63	9 * 8 = 72	9 * 9 = 81
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(f"{j} * {i} = {i * j}", end="\t")
#     print()

# # ### 练习题11：使用for循环，完成打印
# #
# # ```
# # *
# # **
# # ***
# # ****
# # *****
# # ```
# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print("*", end="")
#     print()

# # ### 练习题12：使用for循环，找出1000以内所有的完数
# #
# # 所谓完数是一个数等于它因子之和，例如：6=1+2+3
# for num in range(1, 1001):
#     divisors_sum = sum([i for i in range(1, num) if num % i == 0])
#     if divisors_sum == num:
#         print(num)


# # ### 练习题13：使用for循环，找出100以内所有的素数
# #
# # 所谓素数是大于1的自然数且只能被1和它本身整除
# for num in range(2, 101):
#     if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
#         print(num)


# ### 练习题14：输入年、月、日的值，使用while或for循环完成统计这一天是这一年的第几天。
#
# 且要控制年、月、日的合法输入，如果输入不正确，让用户重新输入。
# 年份必须大于0，月份必须[1,12]，日期必须在[1,这个月最大天数]范围内。

# ```
#
#
# def is_leap_year(year):
#     """
#     判断指定年份是否为闰年。
#     规则：能被4整除但不能被100整除，或者能被400整除的年份是闰年。
#     """
#     return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
#
#
# def get_max_days(year, month):
#     """
#     根据年份和月份，返回该月的最大天数。
#     """
#     # 定义平年每个月的天数
#     days_in_month =
#
#     # 如果是闰年，将2月天数修改为29天
#     if is_leap_year(year):
#         days_in_month = 29
#
#     # 返回指定月份的天数（月份从1开始，数组索引从0开始，所以要-1）
#     return days_in_month[month - 1] < websource > source_group_web_1 < / websource >
#
#
# # --- 1. 输入验证部分 (使用 while 循环) ---
#
# # 验证年份
# while True:
#     try:
#         year = int(input("请输入年份 (必须大于0): "))
#         if year > 0:
#             break
#         else:
#             print("年份必须大于0，请重新输入！")
#     except ValueError:
#         print("输入无效，请输入一个整数！")
#
# # 验证月份
# while True:
#     try:
#         month = int(input("请输入月份 (1-12): "))
#         if 1 <= month <= 12:
#             break
#         else:
#             print("月份必须在1到12之间，请重新输入！")
#     except ValueError:
#         print("输入无效，请输入一个整数！")
#
# # 验证日期
# while True:
#     try:
#         day = int(input(f"请输入日期 (1-{get_max_days(year, month)}): "))
#         if 1 <= day <= get_max_days(year, month):
#             break
#         else:
#             print(f"日期必须在1到{get_max_days(year, month)}之间，请重新输入！")
#     except ValueError:
#         print("输入无效，请输入一个整数！")
#
# # --- 2. 计算天数部分 (使用 for 循环) ---
#
# day_of_year = day  # 初始化为当前日期的天数
#
# # 循环累加当前月份之前的所有月份的天数
# for m in range(1, month):
#     day_of_year += get_max_days(year, m)
#
# # --- 3. 输出结果 ---
# print(f"\n{year}年{month}月{day}日 是这一年的第 {day_of_year} 天。")
# ```

while True:
    year = int(input("请输入年份: "))
    month = int(input("请输入月份: "))
    day = int(input("请输入日期: "))

    if year == 0 or month == 0 or day == 0:
        break

    # 年份必须大于0
    if year < 0:
        print("输入的日期不合法，请重新输入")
        continue

    # 判断是否是闰年
    is_leap_year = False

    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        is_leap_year = True

    if month == 2 and day > 29 and is_leap_year:
        print("输入的日期不合法，请重新输入")
        continue
    elif month == 2 and day > 28:
        print("输入的日期不合法，请重新输入")
        continue
    elif month in [4, 6, 9, 11] and day > 30:
        print("输入的日期不合法，请重新输入")
        continue
    elif month in [1, 3, 5, 7, 8, 10, 12] and day > 31:
        print("输入的日期不合法，请重新输入")
        continue
    else:
        day_of_year = 0
        for i in range(1, month):
            if i in [1, 3, 5, 7, 8, 10, 12]:
                day_of_year += 31
            elif i in [4, 6, 9, 11]:
                day_of_year += 30
            else:
                day_of_year += 29 if is_leap_year else 28

    print(f"这一天是这一年的第{day_of_year}天")





