#!/Python37/python
# -*- coding: utf-8 -*-
# @Time : 2019/10/17 19:29
# @Author : xiaobink
# @File : 函数-返回值及文档字符串.py
# @Software: PyCharm

#函数调用要加（）
# 一、函数的返回值
#返回值就是函数执行完后的结果
#使用return来指定函数的返回值
#可以直接使用函数的返回值，也可以通过变量来接收函数的返回值
#return 后面可以跟任意对象，包括函数
#不写return 或return后没有值，则返回None，函数执行到return，函数自动结束，不会执行后面的语句

# def fn():

#     # return 100
#     def fn1():
#         print('hello')
#     return fn1

# r=fn()
# r()  #hello
# print(r)  #100
# print(fn())  #100

# def fn2():
#     return 1
# print(fn2)    #打印的是函数对象
# print(fn2())  #加括号，调用函数，打印的是函数的返回值

# help(print)


# 二、文档字符串

# def fn(a:int,b:str,c:bool)-> int: #特殊写法，int是参数的类型，->int 是返回值的类型
# def fn(a,b,c):  #常规写法
#     '''
#
#     :param a: 类型 int 默认值...
#     :param b: 类型 str 默认值...
#     :param c: 类型 book 默认值...
#     :return: int
#     '''

#三、函数作用域
#作用域指的是变量生效的区域

#全局作用域
#在程序执行时创建，在程序执行结束时销毁
#所有函数以外的部分都是全局作用域，全局变量就是在全局作用域中定义的变量，可以在程序任意位置访问

#函数作用域
#在函数调用时创建，在调用结束后销毁
#在函数内部的都是函数作用域，局部变量就是在函数作用域中定义的变量，智能在函数调用时访问

#使用global 在函数内部声明变量是全局变量，作用于整个程序
#就近原则，内部可以调用外部变量，外部不能调用内部的变量

# def fn():
#     a=10
#     print(a)
#     def fn2():
#         a=1100
#         b=2
#         print(a,b)  #就近原则，内部可以调用外部，外部不能调用内部的变量
#         #1100 2
#     return fn2()
# fn()

# 四、命名空间
#命名空间实际上是一个字典，是一个专门用来存储变量的字典

# locals() 用来获取当前作用域的命名空间，返回值是一个字典
#若在全局作用域中调用locals()则获取的是全局命名空间，在函数作用域中调用，则是，函数的命名空间

# s=locals()  #获取全局的命名空间
# s['b']=100  #相当于在全局中创建了一个变量，哪怕报错都可以执行
# print(b)
# print(s)

# def fn():
#     a=10
#     # s=locals()  #获取函数的命名空间
#     # print(s)
#     space=globals()  #gloabals()函数可以用来在任意位置获取全局命名空间
#     print(space)
# fn()
