# -*- coding: utf-8 -*-
"""
    @Author  : Zephyr
    @Date    : 2026/4/25 8:32
    @Project  : PythonProject
    @File     : exercise1.py
    @IDE      : PyCharm
    @Description: 
"""

# 1. 创建一个`TodoList`类，包含以下内容：
#    - **类属性**：`total_tasks`（所有待办事项的总数，初始值为0）
#    - **实例属性**：`owner`（拥有者）、`task_type`（类别，例如“生活”，“工作”），
#    `tasks`（任务列表，每个任务是一个字典：{"task": "任务名", "completed": False}）、
#    `created_time`（创建时间，提示datetime.datetime.now()可以获取当前时间）
import datetime

class TodoList:
    total_tasks = 0
    def __init__(self, owner, task_type):
        self.owner = owner
        self.task_type = task_type
        self.tasks = {}
        self.created_time = datetime.datetime.now()
    def add_task(self, task_name):
        self.tasks[task_name] = {"task": task_name, "completed": False}
        TodoList.total_tasks += 1
    def complete_task(self, finished_task_name):
        for task_name in self.tasks:
            if self.tasks[task_name]["task"] == task_name:
                self.tasks[task_name]["completed"] = True
                break
    def show_tasks(self, show_all=True):
        for task, finished in self.tasks.items():
            if show_all or not finished['completed']:
                print(f"{task}: {finished['completed']}")
    def delete_task(self, task_name):
        for task_name in self.tasks:
            if self.tasks[task_name]["task"] == task_name:
                del self.tasks[task_name]
                TodoList.total_tasks -= 1
                break
    def get_progress(self):
        completed_tasks = sum(1 for task in self.tasks if self.tasks[task]["completed"] == True)
        return completed_tasks / len(self.tasks) if self.tasks else 0
    @classmethod
    def get_total_tasks(cls):
        return cls.total_tasks
    @staticmethod
    def is_valid_task(task_name):
        return 1 <= len(task_name) <= 50

# 2. 在`__init__`方法中：
#    - 初始化实例属性
#    - 任务列表为空



# 3. 定义实例方法：
#    - `add_task(self,task_name)`：添加新任务（更新tasks列表，并更新total_tasks+=1）
#    - `complete_task(self,task_name)`：将指定任务标记为已完成
#    - `show_tasks(self,show_all=True)`：显示所有任务（如果show_all=False，只显示未完成的任务）
#    - `delete_task(self,task_name)`：删除指定任务（更新tasks列表，并更新total_tasks-=1）
#    - `get_progress()`：计算并返回完成任务的百分比

# 4. 定义类方法：
#    - `get_total_tasks(cls)`：获取所有待办事项的总数

# 5. 定义静态方法：
#    - `is_valid_task(task_name)`：验证任务名称是否有效（长度1-50字符）

# 6. 创建2个待办事项列表（不同拥有者），并进行以下操作：
#    - 分别添加几个个任务
#    - 完成部分任务
#    - 显示所有任务和只显示未完成任务
#    - 查看任务完成进度
#    - 删除一个任务
#    - 使用静态方法验证1个任务名称
todo_list1 = TodoList("Zephyr", "生活")
todo_list2 = TodoList("Zephyr", "工作")
todo_list1.add_task("购物")
todo_list1.add_task("做饭")
todo_list1.complete_task("购物")
todo_list2.add_task("写代码")
todo_list2.add_task("测试")
todo_list1.show_tasks()
todo_list2.show_tasks()


# 7. **动态操作练习**：
#    - 为某个TodoList对象动态添加一个`priority`属性（优先级）
#    - 动态添加一个实例方法`sort_by_name()`，按任务名称排序
#    - 动态增加类属性`category`
#    - 尝试动态删除某个对象的`show_tasks`方法，观察调用时的错误
todo_list1.priority = "高"
todo_list1.sort_by_name = lambda self: sorted(self.tasks.keys())
todo_list1.category = "待办事项"
del todo_list1.show_tasks
todo_list1.sort_by_name ()
