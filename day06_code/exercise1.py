# -*- coding: utf-8 -*-
"""
    @Author  : Zephyr
    @Date    : 2026/4/22 11:05
    @Project  : PythonProject
    @File     : exercise1.py
    @IDE      : PyCharm
    @Description: 
"""
# ## 题1：
# 有一组商品信息：
# product_price = {
#     "苹果": 5.99,
#     "香蕉": 3.50,
#     "牛奶": 12.80,
#     "面包": 8.50,
#     "笔记本电脑": 4999.99,
#     "无线耳机": 299.99,
#     "运动鞋": 399.00,
#     "保温杯": 69.90
# }
product_price = {
    "苹果": 5.99,
    "香蕉": 3.50,
    "牛奶": 12.80,
    "面包": 8.50,
    "笔记本电脑": 4999.99,
    "无线耳机": 299.99,
    "运动鞋": 399.00,
    "保温杯": 69.90
}
# （1）筛选出价格高于100的商品
high_price_products = {k: v for k, v in product_price.items() if v > 100}
print(high_price_products)
# （2）按照商品价格排序
sorted_products = sorted(product_price.items(), key=lambda item: item[1])
print(sorted_products)

print("-----------------")
# ## 题2：
# 有一组商品信息：
# goods_stock = [
#     {"商品名称": "苹果", "库存量": 120, "价格": 5.99},
#     {"商品名称": "香蕉", "库存量": 85, "价格": 3.50},
#     {"商品名称": "牛奶", "库存量": 200, "价格": 12.80},
#     {"商品名称": "面包", "库存量": 150, "价格": 8.50},
#     {"商品名称": "笔记本电脑", "库存量": 30, "价格": 4999.99},
#     {"商品名称": "无线耳机", "库存量": 55, "价格": 299.99},
#     {"商品名称": "运动鞋", "库存量": 78, "价格": 399.00},
#     {"商品名称": "保温杯", "库存量": 99, "价格": 69.90}
# ]
goods_stock = [
    {"商品名称": "苹果", "库存量": 120, "价格": 5.99},
    {"商品名称": "香蕉", "库存量": 85, "价格": 3.50},
    {"商品名称": "牛奶", "库存量": 200, "价格": 12.80},
    {"商品名称": "面包", "库存量": 150, "价格": 8.50},
    {"商品名称": "笔记本电脑", "库存量": 30, "价格": 4999.99},
    {"商品名称": "无线耳机", "库存量": 55, "价格": 299.99},
    {"商品名称": "运动鞋", "库存量": 78, "价格": 399.00},
    {"商品名称": "保温杯", "库存量": 99, "价格": 69.90}
]
# （1）按照商品库存量升序排序
sorted_goods_stock = sorted(goods_stock, key=lambda item: item["库存量"])
print(sorted_goods_stock)
# （2）找出库存量最多的3个商品的名称
top_3_products = [item["商品名称"] for item in sorted_goods_stock[-3:]]
print(top_3_products)
# （3）库存量最多的3个商品的库存量总和有多少
total_stock = sum(int(item["库存量"]) for item in sorted_goods_stock[-3:])
print(total_stock)

print("-----------------")

# ## 题3：
#
# （1）随机生成10个[1,100]的整数
import random
random_numbers = [random.randint(1, 100) for _ in range(10)]
print(random_numbers)
# （2）定义一个判断x是不是质数的函数
def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True
# （3）筛选出所有质数
primes = [num for num in random_numbers if is_prime(num)]
# （4）求所有质数的和
prime_sum = sum(primes) 


