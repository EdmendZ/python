# -*- coding: utf-8 -*-
"""
    @Author  : Zephyr
    @Date    : 2026/4/27 17:31
    @Project  : PythonProject
    @File     : sourcecodedistribution.py
    @IDE      : PyCharm
    @Description: 
"""
from setuptools import setup, find_packages


setup(
    name="atguigu",  # 打包后的包名称，必须唯一
    version="0.1.0",  # 版本号
    packages=["sdis"],  # 自动识别主包下的所有子包下的所有子包
    python_requires=">=3.7",  # 指定python版本
)
