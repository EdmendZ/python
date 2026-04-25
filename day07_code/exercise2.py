# -*- coding: utf-8 -*-
"""
    @Author  : Zephyr
    @Date    : 2026/4/24 11:40
    @Project  : PythonProject
    @File     : exercise2.py
    @IDE      : PyCharm
    @Description: 
"""
"""
## 练习1：学生信息管理系统

**题目要求：**

1. 创建一个Student类，包含以下内容：
   - 类属性：`school_name`（学校名称，初始值为"第一中学"）、`student_count`（学生总数，初始值为0）
   - 实例属性：`name`（姓名）、`age`（年龄）、`class_name`（班级）
2. 在`__init__`方法中：
   - 初始化实例属性
   - 每次创建学生对象时，让`student_count`自动增加1
3. 定义实例方法：
   - `introduce(self)`：打印学生的所有个人信息
   - `have_birthday(self)`：让学生年龄增加1岁，并打印生日祝福
4. 定义类方法：
   - `change_school(cls, new_name)`：修改学校名称
   - `get_student_count(cls)`：返回当前学生总数
5. 定义静态方法：
   - `is_valid_age(age)`：判断年龄是否在6-18岁之间（包含边界）
6. 创建至少3个学生对象，并依次：
   - 调用`introduce()`方法
   - 为其中一个学生调用`have_birthday()`方法
   - 使用类方法修改学校名称
   - 使用类方法查看学生总数
   - 使用静态方法验证几个不同年龄

## 
"""
class Student:
    school_name = "第一中学"
    student_count = 0

    def __init__(self, name, age, class_name):
        self.name = name
        self.age = age
        self.class_name = class_name
        Student.student_count += 1

    def introduce(self):
        print(f"姓名：{self.name}，年龄：{self.age}，班级：{self.class_name}，学校：{Student.school_name}")

    def have_birthday(self):
        self.age += 1
        print(f"{self.name}的生日快乐，现在{self.age}岁了")
    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name

    @classmethod
    def get_student_count(cls):
        return cls.student_count

    @staticmethod
    def is_valid_age(age):
        return 6 <= age <= 18
    def __str__(self):
        return f"Student(name={self.name}, age={self.age}, class_name={self.class_name})"
    def __repr__(self):
        return self.__str__()


student1 = Student("张三", 12, "7年级3班")
student2 = Student("李四", 14, "7年级4班")
student3 = Student("王五", 13, "7年级5班")
student1.introduce()
student2.introduce()
student3.introduce()
student2.have_birthday()
Student.change_school("第二中学")
student2.introduce()
print(Student.get_student_count())
print(Student.is_valid_age(5))
print(Student.is_valid_age(15))
print(student1)
print(student2)
print(student3)
print(student1)

print("=="*20)
## 练习2：简单的购物车系统

# **题目要求：**
#
# 1. 创建一个`ShoppingCart`类，包含以下内容：
#    - 类属性：`store_name`（商店名称）、`total_carts`（创建的购物车总数）
#    - 实例属性：`owner`（拥有者）、`items`（物品列表，初始为空）、`total_price`（总价，初始为0）
# 2. 定义实例方法：
#    - `add_item(self,item_name, price)`：添加物品到购物车（更新items列表和total_price）
#    - `remove_item(self,item_name)`：从购物车中移除指定物品
#    - `show_cart(self)`：显示购物车中的所有物品和总价
# 3. 定义类方法：
#    - `set_store_name(cls, new_name)`：修改商店名称
#    - `show_total_carts(cls)`：显示创建的购物车总数
# 4. 定义静态方法：
#    - `calculate_discount(price, discount_rate)`：计算折扣后的价格
# 5. 创建2个购物车对象（不同拥有者），并测试：
#    - 分别添加3-4件物品
#    - 从一个购物车中移除一件物品
#    - 显示两个购物车的内容
#    - 修改商店名称并验证
#    - 使用静态方法计算某个物品的折扣价
class ShoppingCart:
    store_name = "购物街"
    total_carts = 0
    def __init__(self, owner):
        self.owner = owner
        self.items = []
        self.total_price = 0
        ShoppingCart.total_carts += 1
    def add_item(self, item_name, price):
        self.items.append((item_name, price))
        self.total_price += price
    def remove_item(self, item_name):
        for item in self.items:
            if item[0] == item_name:
                self.items.remove(item)
                self.total_price -= item[1]
                break
    def show_cart(self):
        print(f"购物车拥有者：{self.owner}")
        for item in self.items:
            print(f"物品：{item[0]}，价格：{item[1]}")
        print(f"总价：{self.total_price}")
    @classmethod
    def set_store_name(cls, new_name):
        cls.store_name = new_name

    @classmethod
    def show_total_carts(cls):
        print(f"创建的购物车总数：{cls.total_carts}")

    @staticmethod
    def calculate_discount(price, discount_rate):
        return price * (1 - discount_rate)

print("=="*20)
# ## 练习3：图书管理系统
#
# **题目要求：**
#
# 1. 创建一个`Book`类，包含以下内容：
#    - 类属性：`library_name`（图书馆名称）、`total_books`（图书总数）
#    - 实例属性：`title`（书名）、`author`（作者）、`is_borrowed`（是否借出，默认为False）
# 2. 定义实例方法：
#    - `borrow(self)`：借出图书（如果未被借出则改为借出状态，否则打印提示信息）
#    - `return_book(self)`：归还图书（改为未借出状态）
#    - `display_info(self)`：显示图书信息
# 3. 定义类方法：
#    - `change_library_name(cls, new_name)`：修改图书馆名称
#    - `get_total_books(cls)`：获取图书总数
# 4. 定义静态方法：
#    - `is_valid_book(book_title)`：判断书名是否有效（长度大于0且不为空）
# 5. 创建3个图书对象，并进行以下操作：
#    - 借出其中一本书
#    - 尝试借出同一本书（应该提示已被借出）
#    - 归还一本书
#    - 显示所有图书信息
#    - 修改图书馆名称
#    - 使用静态方法验证几个书名
class Book:
    library_name = "图书馆"
    total_books = 0
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False
        Book.total_books += 1
    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
        else:
            print(f"{self.title}已经借出")
    def return_book(self):
        self.is_borrowed = False
    def display_info(self):
        print(f"书名：{self.title}，作者：{self.author}，是否借出：{'是' if self.is_borrowed else '否'}")
    @classmethod
    def change_library_name(cls, new_name):
        cls.library_name = new_name

    @classmethod
    def get_total_books(cls):
        return cls.total_books

    @staticmethod
    def is_valid_book(book_title):
        return len(book_title) > 0 and book_title.strip() != ""
Book1 = Book("Python编程", "一")
Book2 = Book("Python编程", "二")
Book3 = Book("Python编程", "三")
Book1.borrow()
Book1.borrow()
Book1.return_book()
Book1.display_info()
Book2.display_info()
Book3.display_info()
print(Book.get_total_books())
Book.change_library_name("第二图书馆")
Book1.display_info()
print(Book.is_valid_book("Python编程"))
print(Book.is_valid_book(" "))

print("=="*20)
## 练习4：动态修改类和实例

# **题目要求：**
#
# 1. 创建一个`Car`类，初始包含：
#    - 类属性：`wheels`（轮子数量，默认为4）
#    - 实例属性：`brand`（品牌）、`color`（颜色）
#    - 实例方法：`drive(self)`（打印"汽车正在行驶"）
# 2. 进行以下动态操作练习：
#    - **动态添加实例属性**：
#      - 为某个汽车对象添加`engine`属性（发动机型号）
#    - **动态修改实例属性**：
#      - 修改某个汽车对象的颜色
#    - **动态删除实例属性**：
#      - 删除某个汽车对象的颜色属性
#    - **动态添加类属性**：
#      - 为Car类添加`fuel_type`属性（燃料类型）
#    - **动态修改类属性**：
#      - 修改Car类的`wheels`属性
#    - **动态添加方法**：
#      - 为Car类动态添加一个类方法`show_info(cls)`
#      - 为某个汽车对象动态添加一个实例方法`stop(self)`
#    - **动态删除方法**：
#      - 删除某个对象的方法或类的某个方法
# 3. 每一步操作后，验证属性/方法是否存在并展示效果
import types  # 导入 types 模块，用于动态绑定方法


# 1. 创建 Car 类
class Car:
    # 类属性
    wheels = 4

    # 初始化方法
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    # 实例方法
    def drive(self):
        print(f"{self.color}的{self.brand}汽车正在行驶...")


# 创建两个实例用于测试
car1 = Car("Toyota", "Red")
car2 = Car("Honda", "Blue")

print("--- 初始状态 ---")
print(f"car1: {car1.brand}, {car1.color}, 轮子: {car1.wheels}")
car1.drive()

# ==========================================
# 2. 动态操作练习
# ==========================================

# --- (1) 动态添加实例属性 ---
print("\n--- (1) 动态添加实例属性: engine ---")
car1.engine = "V6 Turbo"  # 只给 car1 添加发动机属性
print(f"car1 添加了 engine: {car1.engine}")
# print(car2.engine) # 如果运行这行会报错，因为 car2 没有 engine

# --- (2) 动态修改实例属性 ---
print("\n--- (2) 动态修改实例属性: color ---")
car2.color = "Black"
print(f"car2 的颜色修改为: {car2.color}")

# --- (3) 动态删除实例属性 ---
print("\n--- (3) 动态删除实例属性: color ---")
del car1.color
# 验证：尝试访问已删除的属性
try:
    print(f"car1 的颜色: {car1.color}")
except AttributeError as e:
    print(f"错误提示: {e} (说明属性已被成功删除)")

# --- (4) 动态添加类属性 ---
print("\n--- (4) 动态添加类属性: fuel_type ---")
Car.fuel_type = "Gasoline"
print(f"Car 类添加了 fuel_type: {Car.fuel_type}")
print(f"car2 也能访问类属性: {car2.fuel_type}")

# --- (5) 动态修改类属性 ---
print("\n--- (5) 动态修改类属性: wheels ---")
Car.wheels = 6
print(f"Car 类轮子数修改为: {Car.wheels}")
print(f"car2 的轮子数也随之变为: {car2.wheels}")

# --- (6) 动态添加方法 ---
print("\n--- (6) 动态添加方法 ---")


# A. 为 Car 类动态添加类方法 show_info
@classmethod
def show_info(cls):
    print(f"这是{cls.__name__}类，燃料类型: {cls.fuel_type}")


Car.show_info = show_info  # 直接赋值

# 调用类方法
Car.show_info()


# B. 为 car1 对象动态添加实例方法 stop
def stop(self):
    print(f"{self.brand} 汽车停了下来。")


# 使用 types.MethodType 将函数绑定到实例
car1.stop = types.MethodType(stop, car1)

# 调用实例方法
car1.stop()
# car2.stop() # 报错，因为 stop 方法只绑定给了 car1

# --- (7) 动态删除方法 ---
print("\n--- (7) 动态删除方法 ---")
del car1.stop

# 验证：尝试调用已删除的方法
try:
    car1.stop()
except AttributeError as e:
    print(f"错误提示: {e} (说明方法已被成功删除)")

# 也可以删除类的方法
del Car.show_info
try:
    Car.show_info()
except AttributeError as e:
    print(f"错误提示: {e} (说明类方法已被成功删除)")


# ## 练习5：综合练习 - 银行账户系统
#
# **题目要求：**
#
# 1. 创建一个`BankAccount`类，包含以下内容：
#    - 类属性：`bank_name`（银行名称）、`total_accounts`（账户总数）、`interest_rate`（利率，默认为0.03）
#    - 实例属性：`account_number`（账号）、`owner`（户主）、`balance`（余额，初始为0）
# 2. 定义实例方法：
#    - `deposit(self,amount)`：存款（增加余额）
#    - `withdraw(self,amount)`：取款（检查余额是否足够）
#    - `check_balance(self)`：查询余额
#    - `apply_interest(self)`：应用利率计算利息并加到余额
# 3. 定义类方法：
#    - `change_interest_rate(cls, new_rate)`：修改利率
#    - `get_total_accounts(cls)`：获取总账户数
#    - `create_account(cls, owner)`：创建账户并自动生成账号（账号规则：BANK + 10001 + 序号）
# 4. 定义静态方法：
#    - `validate_amount(amount)`：验证金额是否为正数
#    - `format_currency(amount)`：将金额格式化为货币格式（如：¥1,234.56）
# 5. 创建3个账户并进行以下操作：
#    - 存款操作
#    - 取款操作
#    - 查询余额
#    - 应用利息
#    - 修改利率后再次应用利息
#    - 使用静态方法验证金额和格式化金额
class BankAccount:
    bank_name = "中国银行"
    total_accounts = 0
    interest_rate = 0.03
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
        BankAccount.total_accounts += 1
        print(f"账户 {self.account_number} 创建成功，初始余额为: {self.balance}")

    def deposit(self, amount):
        if BankAccount.validate_amount(amount):
            self.balance += amount
            print(f"存款 {amount} 成功，当前余额为: {self.balance}")
        else:
            print("存款金额无效")

    def withdraw(self, amount):
        if BankAccount.validate_amount(amount):
            if self.balance >= amount:
                self.balance -= amount
                print(f"取款 {amount} 成功，当前余额为: {self.balance}")
            else:
                print("余额不足")
        else:
            print("取款金额无效")

    def check_balance(self):
        print(f"账户 {self.account_number} 的余额为: {self.balance}")

    def apply_interest(self):
        interest = self.balance * BankAccount.interest_rate
        self.balance += interest
        print(f"已应用利息，当前余额为: {self.balance}")

    @classmethod
    def change_interest_rate(cls, new_rate):
        cls.interest_rate = new_rate
        print(f"利率已修改为: {cls.interest_rate}")

    @classmethod
    def get_total_accounts(cls):
        return cls.total_accounts

    @staticmethod
    def validate_amount(amount):
        return amount > 0

    @staticmethod
    def format_currency(amount):
        return f"¥{amount:,.2f}"
