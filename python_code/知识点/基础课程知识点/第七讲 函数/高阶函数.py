#!/Python37/python
# -*- coding: utf-8 -*-
# @Time : 2019/10/19 20:00
# @Author : xiaobink
# @File : 高阶函数.py
# @Software: PyCharm

#一、高阶函数
#接收函数作为参数，将函数作为返回值的函数就是高阶函数
#当我们使用一个函数作为参数时，实际上就是把指定的代码传给了目标函数


#定义一个函数，用来检测任意数的偶数
# def fn1(i):
#     if i %2 ==0:
#         return True
#     return False
#
# #定义一个函数 用来检测指定数字是否大于3
# def fn2(n):
#     if n>3:
#         return True
#     return False
#
# #定义一个高阶函数，将函数作为参数传入
# def fn(f,lst):
#     new_list=[]
#     for n in lst:
#         if f(n):  #调用其他函数，注意是调用，加了括号，同时n作为函数的参数
#             new_list.append(n)
#     return new_list
#
# l=[1,2,3,4,5,6]
# print(fn(fn2,l))

#二、匿名函数 lambda
#匿名函数一般都是作为参数使用，其他地方不用
#lambada函数表达式是用来创建一些简单的函数，它是函数创建另外一种方式
#语法：lambda 参数列表：返回值

#filter() 可以从序列中过滤出符合条件的元素，保存到一个新的序列中
#参数：1.函数，根据该函数来过滤序列（可迭代结构）
#       2.需要过滤的序列（可迭代结构）
#       3.返回值 过滤后新的序列
# print(list(filter(fn2,l)))


#匿名函数最大好处是只调用一次，用完之后会从内存中消失
# def fn3(a,b):
#     return a+b
# print((lambda a,b:a+b)(1,2))  #使用lambda来实现相同的结果
#
# r=filter(lambda i:i%3==0,l)
# print(list(r))

#map()
#map()函数可以对可迭代对象中所有元素做指定操作，然后将其添加到一个新的对象中返回

# l=[1,2,3,4,5,6]
# r=map(lambda i :i+1,l)
# print(list(r))

#sort() 函数 可以对列表中的元素进行排序（是一个高阶函数）
#关键字参数key排序:需要一个函数作为参数
# lst=['bb','aaa','c','dddddd','eeee','1']
# # lst.sort(key=len)
# # print(lst)   #['c', '1', 'bb', 'aaa', 'eeee', 'dddddd']
# print(sorted(lst,key=len))  #会返回一个新的列表,不是修改原列表


# 三、闭包  不希望被一些变量别人修改时可以采用闭包（出现变量同名时）
# 将函数作为返回值返回，也是一种高阶函数
#通过闭包可以创建一些只有当前函数才能访问的对象，还可以将一些私有的数据藏到闭包中

#行程闭包的条件
#1.函数嵌套
#2.将内部函数作为返回值返回
#3.内部函数必须使用要外部函数的变量
# def fn5():
#     def fn2():
#         a=10
#         print('我是fn2',a)
#     return fn2
# # print(fn5())
# a=1
# r=fn5()
# r()

#求多个数的平均值
# nums=[1,2,3,4,5,6,7,8]
#
# def new_avg():
#     nums=[]
#     def avg(n):
#         #将元素添加到列表中
#         nums.append(n)
#         return sum(nums)/len(nums)
#     return avg
# nums=123
# a=new_avg()
# print(a(10))


#四、装饰器的引入
def add(a,b):
    return a+b

def mul(a,b):
    return a*b

#产生的问题：
#1修改的函数很多
#2不方便后期的维护
#3会违反开闭原则（ocp) 程序设计 要求对程序的扩展，但是要关闭对程序的修改

#创建一个新的函数，来对原函数进行扩展

#对add（）函数进行扩展
# def new_add(a,b):
#     print('函数开始执行')
#     r=add(a,b)
#     print('函数执行结束')
#     return r
# r=new_add(1,2)
# print(r)


#五、装饰器的使用

def start_end(old):
    # 参数old 是要扩展的函数对象
    # 用来对其他函数进行扩展， 函数开始执行，函数执行结束

    # 创建一个新的函数
    def new_function(*args,**kwargs):
        print('函数开始执行')
        result=old(*args,**kwargs)
        print('函数执行结束')
        #返回函数执行结果
        return result
    #返回新函数
    return new_function
# f=start_end(add)
# r=f(1,2)
# print(r)

#类似于start_end(old)这样的函数其实就是一个装饰器
#通过装饰器可以在不修改原函数的情况下对函数进行扩展
#在开发当中，都是通过装饰器来扩展函数的功能


# @start_end
# def say_byebye():
#     print('byebye')
# say_byebye()



