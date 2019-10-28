#!/Python37/python
# -*- coding: utf-8 -*-
# @Time : 2019/10/22 20:48
# @Author : xiaobink
# @File : 类class简介.py.py
# @Software: PyCharm

# 一、类（class)的简介
#类 简单来说是一张图纸，在程序中我们需要根据类来创建对象

#定义一个类
#语法：class 类名（[父类]）：类名一般采用大驼峰命名法
          # 代码块

# class MyClass():
#     pass
# mc=MyClass() #用这个类创建了一个对象mc,mc是类的实例
# print(mc,type(mc))

# 二、对象的创建流程
# 类是什么？
# 类也是一个对象，是一个用来创建对象的对象
#类是一个type类型的对象

#可以向对象中添加变量，对象中的变量称为属性
# 语法：对象.属性=值

#三、类的定义
# 类和对象都是对现实生活事物或程序内容的抽象

# 1、数据（属性）
# 2、行为（方法）method

#定义一个人类
# class Person:
    # 在类中的变量是实例的公共属性
    # name='葫芦娃'

    # 在类中的函数是实例的公共方法
    # def speak(self):
        #self 是调用该方法的实例化对象本身
#         print()
# p1=Person()
# p2=Person()
# print(p1.name)

#四、属性和方法
#属性和方法的查找流程
#当我们调用一个属性或方法的时候，解析器会先在当前的对象中寻找，有则返回，
# 如果没有则去对象中的类中寻找，有则返回，没有则报错

#类对象和实例对象都可以保存属性值
#属性（方法）是所有类共享的，保存到类当中
#否则保存到实例对象当中，一般属性保存到实例中，方法保存到类当中

# 五、特殊方法（初始化方法）
#初始化方法不需要调用，实例一旦创建，初始化方法将自动调用
#init会向新创建的对象初始化属性
class Person():
    def __init__(self):
        print('init方法执行了')
    def speak(self):
        print()

p1=Person()
p2=Person()
p3=Person()


# 类的基本结构
#class 类名([父类]):
    #公共的属性
    #def__init__(self,...)初始化方法
    #def method(self,...)其他方法