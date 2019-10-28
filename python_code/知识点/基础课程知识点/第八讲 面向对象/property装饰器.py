#!/Python37/python
# -*- coding: utf-8 -*-
# @Time : 2019/10/24 21:55
# @Author : xiaobink
# @File : property装饰器.py.py
# @Software: PyCharm

# 一、@property
#用来将一个get方法转换为对象的属性
#添加property装饰器后，可以按属性的方式来调用
class Person():
    def __init__(self,name):
        self._name=name
    @property
    def name(self):

        return self._name
    @name.setter
    def name(self,name):
        self._name = name
p=Person('葫芦娃')
print(p.name)