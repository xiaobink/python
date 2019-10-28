'''----随机函数random----'''

import random   #调用随机函数模块

num=random.randint(1,500)  #在1-500之间随机生成一个整数
print(num)


num=random.choice(['小明',20,168])   #在list中随机选择一个元素(注意括号)
print(num)

