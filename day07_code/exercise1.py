# -*- coding: utf-8 -*-
"""
    @Author  : Zephyr
    @Date    : 2026/4/24 8:52
    @Project  : PythonProject
    @File     : exercise1.py
    @IDE      : PyCharm
    @Description: 
"""


# 题1：文件读取、字符串拆分
# 任务： 编写函数 count_words_in_file(filename)，读取指定文本文件，返回文件中的总单词数（单词以空格等分隔）。
# 示例： 假设 test.txt 内容如下，则函数返回 4。
def count_words_in_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        words = content.split()
        return len(words)


print(count_words_in_file("a.txt"))


# 题2：文件写入、字典操作
# 任务： 编写函数 save_contacts(contacts, filename)，将通讯录字典（键为姓名，值为电话）保存到文件中，
def save_contacts(contacts, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        for name, phone in contacts.items():
            f.write(f"{name}:{phone}\n")


print(save_contacts({"sfafa": "21fea", "21fea": "777247", "56ggh": "56ggh"}, "b.txt"))


# 题3：文件逐行读取、字符串处理
# 任务： 有一个日志文件 log.txt，每行格式为 时间 - 级别 - 消息，例如 2023-01-01 10:00 - ERROR - Disk full。
# 编写函数 count_log_levels(filename)，统计并返回一个字典，记录每个日志级别（INFO、WARNING、ERROR）出现的次数。
# 示例： {"ERROR": 5, "WARNING": 3, "INFO": 10}
#
# log.txt文件内容
# 1 2023-01-01 10:00 - ERROR - Disk full
# 2 2023-01-01 10:05 - INFO - System started
# 3 2023-01-01 10:10 - WARNING - Low memory
# 4 2023-01-01 10:15 - INFO - User logged in
# 5 2023-01-01 10:20 - ERROR - Connection timeout

def count_log_levels(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        lines = content.splitlines()
        levels = {"ERROR": 0, "WARNING": 0, "INFO": 0}
        for line in lines:
            line = line.strip()
            if line.startswith("2023-01-01"):
                _, level, _ = line.split(" - ")
                levels[level] += 1
        return levels


print(count_log_levels("log.txt"))
