#!/Python37/python
# -*- coding: utf-8 -*-
# @Time : 2019/10/17 19:05
# @Author : xiaobink
# @File : 遍历dict.py
# @Software: PyCharm

# 遍历字典
# keys()
# values()
#items()

#keys() 该方法会返回一个序列,序列中保存字典最外层所有的键
# d={'a':{'name':'葫芦娃','a':1,'b':2}}
# print(d.keys()) #dict_keys(['a']
# for i in d.keys():
#     print(i)   #a

# values() 返回一个序列，序列中保存字典的值
# print(d.values())
# for i in d.values():
#     print(i) #{'name': '葫芦娃', 'a': 1, 'b': 2}

# 返回字典中所有项，返回一个序列，序列中包含双值子序列，双值分别是字典中的键值
d={'name':'葫芦娃','a':1,'b':2}
print(d.items())  #dict_items([('name', '葫芦娃'), ('a', 1), ('b', 2)])
for k,v in d.items():
    print(k,v)
# name 葫芦娃
# a 1
# b 2