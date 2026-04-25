# -*- coding: utf-8 -*-
"""
    @Author  : Zephyr
    @Date    : 2026/4/25 16:53
    @Project  : PythonProject
    @File     : exercise3.py
    @IDE      : PyCharm
    @Description: 
"""
# ## 9.5 案例：愤怒的小鸟

# ### 9.5.1 类的设计
# #### 1、Birds 基类
# 1）设计目的
# 作为所有小鸟类的基类，它定义了小鸟的通用属性和行为，为后续具体小鸟类的扩展提供基础框架，体现了面向对象编程中的抽象和封装思想。
# 2）属性设计
# name：用于标识每只小鸟的名称，方便区分不同个体。
# color：代表小鸟的颜色，这是小鸟的一个显著特征，在游戏中可以对应不同类型的小鸟。
# skill_description：描述小鸟所具备的独特技能，让玩家了解每只小鸟的特殊能力。
# 3）方法设计
# fly()：描述小鸟飞行的基本动作，是小鸟在游戏中的常见行为，所有子类都可以重写该方法来展示不同的飞行特点。
# call()：模拟小鸟发出叫声的行为，同样可以被子类重写以体现不同小鸟的叫声差异。
# use_skill()：用于触发小鸟的特殊技能，展示小鸟使用技能的情况，子类可以根据自身技能特点进行相应实现。
class Birds:
    def __init__(self, name, color, skill_description):
        self.name = name
        self.color = color
        self.skill_description = skill_description

    def fly(self):
        print(f"{self.name} is flying.")

    def call(self):
        print(f"{self.name} is calling.")

    def use_skill(self):
        print(f"{self.name} is using skill: {self.skill_description}")
# #### 2、具体小鸟子类（RedBirds、YellowBirds、BlueBirds）
# 1）设计目的
# 继承自 Birds 基类，每个子类代表一种特定颜色的小鸟，它们在继承基类属性和方法的基础上，重写部分方法以展示不同小鸟的独特行为和技能，体现了面向对象编程中的继承和多态思想。
# 2）属性设计
# 通过调用基类的 `__init__ `方法，初始化各自的 name、color 和 skill_description 属性，确保每只小鸟都有自己的独特标识和技能。
# 3）方法设计
# fly()：重写基类的 fly() 方法，展示不同小鸟的飞行特点，如红鸟以稳定速度飞行，黄鸟快速飞行，蓝鸟优雅飞行。
# call()：重写基类的 call() 方法，模拟不同小鸟的叫声，增加游戏的趣味性。
class RedBirds(Birds):
    def __init__(self):
        super().__init__(name="Red Bird", color="Red", skill_description="Stable Flight")
    def fly(self):
        print(f"{self.name} is flying at a stable speed.")
    def call(self):
        print(f"{self.name} is calling with a loud voice.")
    def use_skill(self):
        print(f"{self.name} is using skill: {self.skill_description}")

class YellowBirds(Birds):
    def __init__(self):
        super().__init__(name="Yellow Bird", color="Yellow", skill_description="Quick Flight")
    def fly(self):
        print(f"{self.name} is flying at a quick speed.")
    def call(self):
        print(f"{self.name} is calling with a cheerful voice.")
    def use_skill(self):
        print(f"{self.name} is using skill: {self.skill_description}")

class BlueBirds(Birds):
    def __init__(self):
        super().__init__(name="Blue Bird", color="Blue", skill_description="Graceful Flight")
    def fly(self):
        print(f"{self.name} is flying gracefully.")
    def call(self):
        print(f"{self.name} is calling with a serene voice.")
    def use_skill(self):
        print(f"{self.name} is using skill: {self.skill_description}")
# #### 3、Obstacle障碍类
# 1）设计目的
# 代表游戏中的障碍物，如木头堡垒、石头塔楼等，负责处理障碍物被小鸟攻击的逻辑，与小鸟类进行交互，体现了面向对象编程中的对象交互和封装思想。
# 2）属性设计
# name：标识障碍物的名称，方便区分不同类型的障碍物。
# strength：表示障碍物的强度，即它能够承受的伤害值，当强度降为 0 时，障碍物被摧毁。
# 3）方法设计
# be_attacked(bird)：模拟障碍物被小鸟攻击的过程，根据小鸟的类型计算伤害，并更新障碍物的强度，同时输出攻击和受损信息，让玩家了解游戏进展。
class Obstacle:
    def __init__(self, name, strength):
        self.name = name
        self.strength = strength

    def be_attacked(self, bird):
        damage = 10  # 假设每次攻击造成固定伤害
        self.strength -= damage
        print(f"{bird.name} attacks {self.name}, causing {damage} damage.")
        if self.strength <= 0:
            print(f"{self.name} is destroyed.")

# ### 9.5.2 设计思路
# #### 1、Birds 类的方法
# 1）fly()
# 作为通用的飞行方法，提供了小鸟飞行的基本描述，子类可以根据自身特点进行个性化实现，以体现不同小鸟的飞行风格。
# 2）call()
# 模拟小鸟发出叫声的行为，为游戏增加生动性，子类可以重写该方法来展示不同小鸟的叫声特点。
# 3）use_skill()
# 用于触发小鸟的特殊技能，通过输出技能描述，让玩家了解小鸟使用技能的情况，不同子类可以根据自身技能进行不同的实现。
# #### 2、具体小鸟子类的方法
# fly() 和 call()：重写基类的方法，根据不同小鸟的特点进行个性化实现，展示不同小鸟的飞行和叫声差异，体现了多态性。
# #### 3、Obstacle 类的方法
# be_attacked(bird)：接收一个小鸟对象作为参数，根据小鸟的类型计算伤害，
# 并更新障碍物的强度。通过判断障碍物的强度是否小于等于 0，
# 输出障碍物是否被摧毁的信息，实现了障碍物与小鸟之间的交互逻辑。
# > 通过这样的类和方法设计，整个游戏模拟程序具有良好的扩展性和可维护性，
# 方便后续添加更多类型的小鸟和障碍物，以及实现更复杂的游戏逻辑。

if __name__ == '__main__':
    red_bird = RedBirds()
    red_bird.fly()
    red_bird.call()
    red_bird.use_skill()
    obstacle = Obstacle("Wooden Fortress", 100)
    obstacle.be_attacked(red_bird)
    obstacle.be_attacked(red_bird)
    obstacle.be_attacked(red_bird)
    obstacle.be_attacked(red_bird)
    obstacle.be_attacked(red_bird)
    obstacle.be_attacked(red_bird)
    obstacle.be_attacked(red_bird)
    obstacle.be_attacked(red_bird)
    obstacle.be_attacked(red_bird)
    obstacle.be_attacked(red_bird)
    obstacle.be_attacked(red_bird)
    obstacle.be_attacked(red_bird)
    obstacle.be_attacked(red_bird)

