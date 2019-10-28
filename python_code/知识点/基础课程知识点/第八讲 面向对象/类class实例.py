#!/Python37/python
# -*- coding: utf-8 -*-
# @Time : 2019/10/24 20:51
# @Author : xiaobink
# @File : 类class实例.py.py
# @Software: PyCharm

# 一、定义一个表示车的类
# class Car():
#     def __init__(self,name,color):
#         self.name=name
#         self.color=color
#
#     def run(self):
#         print('%s汽车开始跑了'%self.color)
#     def laba(self):
#         print('%s 滴滴滴滴'%self.name)
# c=Car('大G','黑色')
# print(c.name,c.color)
# c.run()
# c.laba()

#增加数据安全性
#1、属性不能随意修改（允许修改的才能改）
#2、属性可以修改，但不能改为任意的值（比如年龄没有负的，月份是在1-12之间...）

#二、封装（比如电脑主机箱）
#封装是面向对象的三大特性之一
# 封装指隐藏对象中一些不希望被外部访问到的属性或方法
#如何隐藏对象中的属性:将对象的属性名，修改为一个外部不知道的名字
#如何获取（修改）对象当中的属性
# 提供getter() 和 setter()方法来访问和修改属性
# 使用封装一定程度上增长了类定义的复杂度，但保证了数据的安全性
# 1、隐藏了属性名，使调用者无法随意修改对象中的属性
#2、提供getter() 和 setter()方法来访问和修改属性
#3、使用setter方法来确保值是正确的
# class Dog():
#     def __init__(self,name,age):
#         self.hidden_name=name
#         self.hidden_age=age
#     def speak(self):
#         print('大家好，我是%s'%self.hidden_name)
#     def get_name(self):
#         #get_name()用来获取对象的属性
#         return self.hidden_name,self.hidden_age
#     def set(self,name,age):
#         self.hidden_name=name
#         self.hidden_age=age
# d=Dog('二哈',6)
# d.set('金毛',3)
# print(d.get_name())
# d.speak()

# 三、
#可以为对象的属性使用双下划线__开头
#双下划线开头的属性是对象的隐藏属性，隐藏属性只能在类的内部访问，不能在外部访问
#是python自动为属性改了一个名字，实际修改的名字是：_类名_属性名（_Person_name)
#__不推荐，使用一个_就可以了
class Person():
    def __init__(self,name):
        self.__name=name

    def get_name(self):
        return self.__name

    def set_name(self,name):
        self.__name=name

p=Person('葫芦娃')
# print(p.__name)
p.__name='123'

p._Person__name="黑猫警长"
print(p._Person__name)
print(p.get_name())

#一般情况使用单下划线开头的都是私有的，无特殊情况不要修改私有属性
