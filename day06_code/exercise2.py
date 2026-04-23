# -*- coding: utf-8 -*-
"""
    @Author  : Zephyr
    @Date    : 2026/4/22 19:40
    @Project  : PythonProject
    @File     : exercise2.py
    @IDE      : PyCharm
    @Description: 
"""
# ### 题1：写文件
# 编写程序，接收用户从控制台输入的留言，将其追加到message.txt文件中，每句留言单独一行
# import os
# import time
# def write_message():
#     while True:
#         message = input("请输入留言：")
#         if not message:
#             break
#         with open("message.txt", "a", encoding="utf-8") as f:
#             f.write(message + "\n")
# write_message()
# print("=="*20)
# ### 题2：读文件
# 编写程序，读取message.txt文件的所有留言内容。如果message.txt文件不存在，则提示还没有留言内容。
# import os
# def read_message():
#     if not os.path.exists("message.txt"):
#         print("还没有留言内容")
#     else:
#         with open("message.txt", "r", encoding="utf-8") as f:
#             messages = f.readlines()
#             for message in messages:
#                 print(message.strip())
# read_message()



# ### 题3：写文件
#
# 编写程序，先接收用户输入的用户名，再接收用户输入的留言内容，将其追加到user_message.txt文件中，每个用户的留言单独一行，
#
# 格式是
#
# ```
# 用户名:留言内容
# 用户名:留言内容
# 用户名:留言内容
# ```
# def write_user_message():
#     username = input("请输入用户名：")
#     message = input("请输入留言内容：")
#     with open("user_message.txt", "a", encoding="utf-8") as f:
#         f.write(f"{username}:{message}\n")
#     print("留言已写入文件")
# write_user_message()

# ### 题4：读文件
#
# 编写程序，接收用户输入的用户名，读取user_message.txt文件内容，筛选出该用户的留言内容。如果user_message.txt文件不存在，或没有找到该用户的留言，则提示没有该用户的留言。
# import os
# def read_user_message():
#     username = input("请输入用户名：")
#     if not os.path.exists("user_message.txt"):
#         print("user_message.txt文件不存在")
#     else:
#         with open("user_message.txt", "r", encoding="utf-8") as f:
#             lines = f.readlines()
#             for line in lines:
#                 if username in line:
#                     print(line.strip())
#             else:
#                 print("没有该用户的留言")
# read_user_message()

# ### 题5：获取文件信息
#
# （1）获取message.txt文件大小，创建时间，最后修改时间
#
# （2）获取message.txt文件的绝对路径，文件名部分，扩展名部分
#
# （3）获取user_message.txt文件中，一共有多少个不同用户的留言
# import os
# def get_file_info():
#     if os.path.exists("message.txt"):
#         file_size = os.path.getsize("message.txt")
#         file_create_time = os.path.getctime("message.txt")
#         file_last_modified_time = os.path.getmtime("message.txt")
#         print(f"文件大小：{file_size}字节")
#         print(f"创建时间：{file_create_time}")
#         print(f"最后修改时间：{file_last_modified_time}")
#
#         absolute_path = os.path.abspath("message.txt")
#         print(f"绝对路径：{absolute_path}")
#         print(f"文件名部分：{os.path.basename(absolute_path)}")
#         print(f"文件名部分：{os.path.splitext(os.path.basename(absolute_path))[0]}")
#         print(f"扩展名部分：{os.path.splitext(os.path.basename(absolute_path))[1]}")
#
#         if os.path.exists("user_message.txt"):
#             with open("user_message.txt", "r", encoding="utf-8") as f:
#                 lines = f.readlines()
#                 users = set()
#                 for line in lines:
#                     users.add(line.split(":")[0])
#                 print(f"一共有 {len(users)} 个不同用户的留言")
#     else:
#         print("message.txt文件不存在")
# get_file_info()
# ### 题6：目录和文件操作
#
# （1）编写代码实现：在当前工作目录下创建 homework 目录
#
# （2）编写代码实现：将上述message.txt和user_message.txt文件 移动到 homework目录
#
# （3）编写代码实现：遍历当前工作目录
#
# （4）编写代码实现：删除homework目录
import os
import shutil
def delete_homework_dir():
    if os.path.exists("homework"):
        shutil.rmtree("homework")
        print("homework目录已删除")
    else:
        print("homework目录不存在")
def move_files_to_homework_dir():
    if not os.path.exists("homework"):
        os.mkdir("homework")
    os.rename("message.txt", "homework/message.txt")
    os.rename("user_message.txt", "homework/user_message.txt")
    print("文件已移动到 homework 目录")
def iterator_current_directory():
    for filename in os.listdir("."):
        print(filename)

delete_homework_dir()
move_files_to_homework_dir()
print(os.listdir("."))
iterator_current_directory()


