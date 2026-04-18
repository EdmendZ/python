# -*- coding: utf-8 -*-
"""
    @Author  : Zephyr
    @Date    : 2026/4/17 8:33
    @Project  : PythonProject
    @File     : exercise1.py
    @IDE      : PyCharm
    @Description: 
"""

# ### 1 查看Python版本
#
# ```
# python --version
# python -V
# ```
#
# ### 2
#
# ```
# print('Hello World')
# ```
#
# ### 3 Python 命名规则
#
# ```
# 只能包含字母（a-z, A-Z）、数字（0-9）和下划线（_）。
# 不能以数字开头。
# 不能使用 Python 关键字作为标识符（如 if, for, class, def 等）。
# 区分大小写（myVar 与 myvar 是两个不同的标识符）。
# 不能包含空格或特殊字符（如 @, #, $, % 等）。
# 建议使用小写字母和下划线组合（如 user_name, age_count），符合 PEP 8 代码风格规范。
# ```
#
# ### Python 注释类型和语法
#
# Python 支持两种注释方式：
#
# 1. **单行注释**：
#    - 使用 **井号 `#`** 开头。
#    - 从 `#` 开始到行尾的所有内容都被视为注释，不会被执行。
# 2. **多行注释（文档字符串）**：
#    - 使用 **三个连续的双引号 `"""` 或三个单引号 `'''`** 包裹。
#    - 通常用于函数、类或模块的说明文档。
#    - 是字符串，但未被赋值时，相当于注释。
#
# ``` python
# name, age, gender, weight, is_married = "LisongZhang", 24, 'male', 74, False
#
# print("name: " + name)
# print("age: ", age)
# print("gender: " + gender)
# print("weight: ", weight)
# print("is_married: ", is_married)
# ```



name, age, gender, weight, is_married = "LisongZhang", 24, 'male', 74, False

print("name: " + name)
print("age: ", age)
print("gender: " + gender)
print("weight: ", weight)
print("is_married: ", is_married)