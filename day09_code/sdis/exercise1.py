# -*- coding: utf-8 -*-
"""
    @Author  : Zephyr
    @Date    : 2026/4/27 8:31
    @Project  : PythonProject
    @File     : exercise1.py
    @IDE      : PyCharm
    @Description: 
"""


### 题目1：车辆租赁计费系统

# **背景**：实现不同车型的租赁费用计算。
# **要求**：
#
# 1. 父类`Vehicle`包含私有属性`_base_rate`（日基础租金）和`_rent_days`（租的天数）。方法`calculate_cost()`返回基础租金×天数。
# 2. 子类：
#    - `Car`：额外收取每天50元保险费，重写`calculate_cost()`。
#    - `Truck`：基础租金×天数 + 每公里5元（公里数作为额外参数传入），因此重写`calculate_cost(km)`。
# 3. **封装**：`_base_rate`只能通过构造函数设置，不能直接修改。提供`set_rent_days()`方法修改租的天数。
# 4. 创建Car和Truck对象测试
class Vehicle:
    def __init__(self, base_rate):
        self.__base_rate = base_rate
        self.__rent_days = 0

    @property
    def rent_days(self):
        return self.__rent_days

    @rent_days.setter
    def rent_days(self, days):
        self.__rent_days = days

    def calculate_cost(self):
        return self.__base_rate * self.__rent_days


class Car(Vehicle):
    def __init__(self, base_rate, rent_days=0):
        super().__init__(base_rate)
        self.__rent_days = rent_days

    def calculate_cost(self):
        return super().calculate_cost() + 50 * self.__rent_days


class Truck(Vehicle):
    def __init__(self, base_rate, km):
        super().__init__(base_rate)
        self.km = km

    def calculate_cost(self):
        return super().calculate_cost() + self.km * 5


car1 = Car(100)
car1.rent_days = 3
print(car1.calculate_cost())

truck = Truck(100, 100)
print(truck.calculate_cost())


### 题目2：游戏角色职业系统

# **背景**：RPG游戏中角色有多种能力来源。
# **要求**：
#
# 1. 创建三个基类：
#    - 战士`Fighter`：包含属性`__strength`力量值、提供`attack()`方法输出“物理攻击”
#    - 法师`Mage`：包含属性`__intelligence`智力值、提供`cast_spell()`方法输出“火球术”
#    - 医师`Healer`：包含`__wisdom`智慧值、提供`heal()`方法输出“治疗术”）。
#    - 每个类都有`get_power()`方法返回不同数值（战士返回力量值，法师返回智力值等）。
# 2. 创建子类`Paladin`（圣骑士）同时继承`Fighter`和`Healer`，重写`get_power()`为(力量×0.6 + 智慧×0.4)。并拥有自己的`holy_light()`技能。
# 3. 创建子类`Spellblade`（魔剑士）同时继承`Fighter`和`Mage`，重写`attack()`为先施放一个附加魔法效果再物理攻击（调用两个父类对应方法）。
# 4. **多态**：定义一个函数`show_power(character)`，调用其`get_power()`。演示不同角色传入时得到不同计算方式。
# 5. **封装**：每个角色的力量/智力等属性设为私有，通过getter访问。
class Fighter:
    def __init__(self, strength):
        self.__strength = strength

    def attack(self):
        print("物理攻击")

    @property
    def strength(self):
        return self.__strength

    def get_power(self):
        return self.__strength


class Mage:
    def __init__(self, intelligence):
        self.__intelligence = intelligence

    def cast_spell(self):
        print("火球术")

    @property
    def intelligence(self):
        return self.__intelligence

    def get_power(self):
        return self.__intelligence


class Healer:
    def __init__(self, wisdom):
        self.__wisdom = wisdom

    def heal(self):
        print("治疗术")

    @property
    def wisdom(self):
        return self.__wisdom

    def get_power(self):
        return self.__wisdom


class Paladin(Fighter, Healer):
    def __init__(self, strength, intelligence):
        super().__init__(strength)
        super().__init__(intelligence)

    def get_power(self):
        return self.strength * 0.6 + self.intelligence * 0.4

    def holy_light(self):
        print("圣光")

    def attack(self):
        super().attack()
        self.holy_light()

    def cast_spell(self):
        super().cast_spell()
        self.holy_light()
