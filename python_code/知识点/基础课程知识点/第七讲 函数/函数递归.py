#!/Python37/python
# -*- coding: utf-8 -*-
# @Time : 2019/10/17 21:18
# @Author : xiaobink
# @File : 函数递归.py
# @Software: PyCharm

# 一、递归

# 递归简单理解就是自己调用自己
# 递归式函数：在函数中自己调用自己

# 递归式函数有两个条件
##1、基线条件
# 问题可以被分解为最小的问题，当满足基线条件的时候，递归就不在执行
##2、递归条件
# 可以将问题分解的条件

# 练习1 求任意数的阶乘
# def fn(n):
#
#     #基线条件 判断n是否为1
#     if n==1:
#         return 1
#
#     #递归条件
#     return n*fn(n-1)
#
# print(fn(10))

# #无穷递归 类似于死循环
# def fn():
#     fn()
# fn()

# 练习2 创建一个函数来为任意数字做幂运算
# def fn(n,i):
#     if i==1:
#         return n
#
#     return n*fn(n,i-1)
#
# print(fn(2,100))

# 练习3

# def fn1(s):
#
#     #基线条件
#     if len(s)<2:
#         return True
#     elif s[0]!=s[-1]:
#         return False
#
#     return fn1(s[1:-1])
#
# print(fn1('1221'))

# 练习4 斐波那契数列
# def fn2(n):
#     if n==1:
#         return 1
#     elif n<1:
#         return 0
#
#     return fn2(n-1)+fn2(n-2)
# print(fn2(5))

# 练习5 汉诺塔
# def fn3(n,x='a',y='b',z='c'):
#     if n==1:
#         print(x + '--->' +z)
#         return 1
#
#
#     return 2*fn3(n-1)+1
# print(fn3(5))

# 练习6 将输入的字符反转
# def fn4(s):
#     #基线条件
#     if len(s)<=1:
#         # print(s)
#         return s
#     # print(s[-1])
#     return s[-1]+fn4(s[:-1])
# print(fn4('abcd'))

# 练习7 欧几里得算法求两个数的最大公约数
# def fn5(n1,n2):
#     result = n1 % n2
#     #基线条件
#     if result==0:
#         return n2
#
#     return fn5(n2,result)
# print(fn5(100,2000))

# 练习8 猴子吃桃(逆向递归）
# def fn6(day):
#     #基线条件
#     if day==10:
#         return 1
#     return (fn6(day+1)+1)*2
#
# print(fn6(1))

# def fn(n):
#     if n==1:
#         return 10
#     return fn(n-1)+2
# print(fn(6))


def get_index(lst, str, lower, upper):
    if lower == upper:
        return upper
    else:
        middle = (lower + upper) // 2
        if str in lst[lower:middle + 1]:  # 注意：切片操作的终止位置是截取不到的，所以要+1才能正常判断。
            return get_index(lst, str, lower, middle)
        else:
            return get_index(lst, str, middle + 1, upper)

lst=[1,2,3,4,5,6,7]
print(get_index(lst, input('请输入姓名：'), 0, len(lst)))