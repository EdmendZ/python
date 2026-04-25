# -*- coding: utf-8 -*-
"""
    @Author  : Zephyr
    @Date    : 2026/4/25 11:18
    @Project  : PythonProject
    @File     : exercise2.py
    @IDE      : PyCharm
    @Description: 
"""
## 练习题1：银行账户系统（封装）

# 创建一个银行账户类 `BankAccount`，实现基本的封装特性：
#
# **要求：**
#
# - 私有属性：`__account_number`（账号）、`__balance`（余额）、`__password`（密码）
# - 提供公开方法：
#   - `deposit(amount, password)`：存款（需要验证密码）
#   - `withdraw(amount, password)`：取款（需要验证密码）
#   - `check_balance(password)`：查询余额（需要验证密码）
#   - `set_password(old_password, new_password)`：修改密码，修改密码时，还得输入旧密码用于验证
# - 设置合理的属性访问控制，不允许直接访问和修改私有属性
#
# **提示：** 使用双下划线前缀实现私有属性
class BankAccount:
    def __init__(self, account_number, balance, password):
        self.__account_number = account_number
        self.__balance = balance
        self.__password = password
    def deposit(self, amount, password):
        if self.__password == password:
            self.__balance += amount
            return True
        else:
            return False
    def withdraw(self, amount, password):
        if self.__password == password:
            if self.__balance >= amount:
                self.__balance -= amount
                return True
            else:
                return False
        else:
            return False
    def check_balance(self, password):
        if self.__password == password:
            return self.__balance
        else:
            return None
    def set_password(self, old_password, new_password):
        if self.__password == old_password:
            self.__password = new_password
            return True
        else:
            return False

# ## 练习题2：动物继承体系（继承）
#
# 创建一个动物继承体系，展示基本的继承特性：
#
# **要求：**
#
# - 基类 `Animal`：
#   - 属性：`name`、`age`
#   - 方法：`eat()`、`sleep()`（打印通用信息）
# - 派生类：
#   - `Dog`：添加方法 `bark()`
#   - `Cat`：添加方法 `meow()`
#   - `Bird`：添加方法 `fly()`，并重写 `eat()` 方法（鸟类吃虫子的特殊行为）
# - 每个派生类都应调用父类的初始化方法
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def eat(self):
        print("This animal is eating.")
    def sleep(self):
        print("This animal is sleeping.")

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
    def bark(self):
        print("The dog is barking.")

class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
    def meow(self):
        print("The cat is meowing.")

class Bird(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
    def fly(self):
        print("The bird is flying.")
    def eat(self):
        print("The bird is eating insects.")

# ## 练习题3：图形面积计算（多态）
#
# 创建一个图形类体系，展示多态特性：
#
# **要求：**
#
# - 基类 `Shape`：
#   - 定义方法 `area()` 和 `perimeter()`，方法体用pass表示
# - 派生类：
#   - `Rectangle`（矩形）：属性 `width`、`height`
#   - `Circle`（圆形）：属性 `radius`
#   - `Triangle`（三角形）：属性 `a`、`b`、`c`（三边长）
# - 创建函数 `print_shape_info(shape)`，接收任何形状对象并打印其面积和周长
# - 演示多态：用不同形状对象调用同一函数
class Shape:
    def area(self):
        pass
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)
    def print_shape_info(self):
        print(f"Rectangle - Area: {self.area()}, Perimeter: {self.perimeter()}")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2
    def perimeter(self):
        return 2 * 3.14 * self.radius
    def print_shape_info(self):
        print(f"Circle - Area: {self.area()}, Perimeter: {self.perimeter()}")

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def area(self):
        s = (self.a + self.b + self.c) / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5
    def perimeter(self):
        return self.a + self.b + self.c
    def print_shape_info(self):
        print(f"Triangle - Area: {self.area()}, Perimeter: {self.perimeter()}")

# --- 演示多态 ---
if __name__ == "__main__":
    rect = Rectangle(3, 4)
    circle = Circle(5)
    tri = Triangle(3, 4, 5)

    shapes = [rect, circle, tri]

    for shape in shapes:
        # 同一个函数，处理不同类型的对象
        shape.print_shape_info()
        def print_shape_info(shape):
            print(f"Shape - Area: {shape.area()}, Perimeter: {shape.perimeter()}")
        print_shape_info(shape)

# ## 练习题4：员工管理系统（组合封装与继承）
#
# 设计一个员工管理系统，综合运用封装和继承：
#
# **要求：**
#
# - 基类 `Employee`（封装）：
#   - 私有属性：`__name`、`__id`、`__base_salary`
#   - 公开方法：`get_details()`、`calculate_salary()`（基本工资）
# - 派生类：
#   - `Manager`：额外属性 `bonus`（奖金），重写 `calculate_salary()`
#   - `Developer`：额外属性 `project_count`，重写 `calculate_salary()`（按项目数量计算）
#   - `Intern`：额外属性 `mentor`（指导人），重写 `calculate_salary()`（固定津贴）
# - 公司类 `Company`（组合）：
#   - 属性：员工列表
#   - 方法：`add_employee()`、`remove_employee()`、`get_total_salary()`、`list_all_employees()`
class Employee:
    def __init__(self, name, id, base_salary):
        self.__name = name
        self.__id = id
        self.__base_salary = base_salary
    def get_details(self):
        return f"Name: {self.__name}, ID: {self.__id}, Base Salary: {self.__base_salary}"
    def calculate_salary(self):
        return self.__base_salary
    def print_employee_info(self):
        print(self.get_details())
        print(f"Salary: {self.calculate_salary()}")

class Manager(Employee):
    def __init__(self, name, id, base_salary, bonus):
        super().__init__(name, id, base_salary)
        self.bonus = bonus
    def calculate_salary(self):
        return super().calculate_salary() + self.bonus
    def print_manager_info(self):
        print(self.get_details())
        print(f"Salary: {self.calculate_salary()}")

class Developer(Employee):
    def __init__(self, name, id, base_salary, project_count):
        super().__init__(name, id, base_salary)
        self.project_count = project_count
    def calculate_salary(self):
        return super().calculate_salary() + self.project_count * 1000
    def print_developer_info(self):
        print(self.get_details())
        print(f"Salary: {self.calculate_salary()}")

class Intern(Employee):
    def __init__(self, name, id, base_salary, mentor):
        super().__init__(name, id, base_salary)
        self.mentor = mentor
    def calculate_salary(self):
        return super().calculate_salary() + 500
    def print_intern_info(self):
        print(self.get_details())
        print(f"Salary: {self.calculate_salary()}")


# ## 练习题5：图书馆借阅系统（综合练习）
# 设计一个图书馆借阅系统，综合运用三大特性：
# **要求：**
# - 基类 `LibraryItem`（封装）：
#   - 私有属性：`__item_id`、`__title`、`__is_borrowed`
#   - 方法：
#     - `borrow()`：修改`__is_borrowed`为True
#     - `return_item()`：修改`__is_borrowed`为False
#     - ``get_info()`：编号：xx，名称：xx，是否可借阅：是/否
# - 派生类（继承与多态）：
#   - `Book`：额外属性 `author`、`pages`，重写 `get_info()`
#   - `DVD`：额外属性 `director`、`duration`，重写 `get_info()`
#   - `Magazine`：额外属性 `issue_number`，重写 `get_info()`
# - 类 `Library`（组合）：
#   - 属性：物品列表
#   - 方法：`add_item()`、`remove_item()`、`search_by_title()`、`display_available_items()`
# - 实现多态：`display_item_info(item)` 函数能正确显示任何类型物品的信息
class LibraryItem:
    def __init__(self, item_id, title, is_borrowed):
        self.__item_id = item_id
        self.__title = title
        self.__is_borrowed = is_borrowed
    def borrow(self):
        self.__is_borrowed = True
    def return_item(self):
        self.__is_borrowed = False
    def get_info(self):
        return f"Item ID: {self.__item_id}, Title: {self.__title}, Borrowed: {self.__is_borrowed}"

class Book(LibraryItem):
    def __init__(self, item_id, title, is_borrowed, author, pages):
        super().__init__(item_id, title, is_borrowed)
        self.author = author
        self.pages = pages
    def get_info(self):
        return super().get_info() + f", Author: {self.author}, Pages: {self.pages}"
    def print_book_info(self):
        print(self.get_info())

class DVD(LibraryItem):
    def __init__(self, item_id, title, is_borrowed, director, duration):
        super().__init__(item_id, title, is_borrowed)
        self.director = director
        self.duration = duration
    def get_info(self):
        return super().get_info() + f", Director: {self.director}, Duration: {self.duration} minutes"

class Magazine(LibraryItem):
    def __init__(self, item_id, title, is_borrowed, issue_number):
        super().__init__(item_id, title, is_borrowed)
        self.issue_number = issue_number
    def get_info(self):
        return super().get_info() + f", Issue Number: {self.issue_number}"

class Library:
    def __init__(self):
        self.items = []
    def add_item(self, item):
        self.items.append(item)
    def remove_item(self, item):
        self.items.remove(item)
    def search_by_title(self, title):
        for item in self.items:
            if item.__title == title:
                return item
        return None
    def display_all_items(self):
        for item in self.items:
            print(item.get_info())
    def display_available_items(self):
        for item in self.items:
            if not item.__is_borrowed:
                print(item.get_info())
    def display_item_info(self, item):
        item.print_book_info()
