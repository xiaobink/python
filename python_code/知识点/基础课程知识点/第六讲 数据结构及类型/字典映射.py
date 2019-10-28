
#字典是一种新的数据结构，称之为映射（mapping）
#作用：是用来存储对象的容器

#list存储数据性能好，但查询数据性能差
#dict中每个元素有唯一的键，通过key可以快速找到指定元素
#通过key来查找value

#value可以重复，但key是唯一的,若重复，则后面的键值会替换前边所有重复的
#value可以是任意对象，key是可以任意不可变对象（int,string,bool,tuple...)

#创建字典方法
#1、{} 2、dict()
# d={'name':'葫芦娃','age':10,'name':'钢铁侠'}
# print(d)   #{'name': '钢铁侠', 'age': 10}

# d=dict(name='葫芦娃',age=20)
# print(d)   #{'name': '葫芦娃', 'age': 20}

#双值序列 序列中只有两个值[3,4] ('name','hello') 'xy'
#子序列：如果序列中的元素也是序列，那么我们就成这个元素为子序列
d=dict([('name','葫芦娃'),('age',20)])
# print(d)           #{'name': '葫芦娃', 'age': 20}

#len() 获取长度

# in 检查字典中是否包含指定的键
# print('name' in d)         #True

# get(key[,default)     根据键来获取字典的值，若键不存在，则返回一个None
# print(d.get('hello'))       #None

#修改值
#如果键存在则覆盖，不存在则添加
# d['name']='黑猫警长'
# print(d)     #{'name': '黑猫警长', 'age': 20}

# d.setdefault(key[,default] 可以用来向字典中添加键值对
#若key存在则返回key的值，若key不存在，则向字典当中添加这个键值对
# d.setdefault('name1','黑猫警长')
# print(d)                   #{'name': '葫芦娃', 'age': 20, 'name1': '黑猫警长'}

# update() 将其他字典中的键值对添加到当前字典中 ,有重复则覆盖
# d1={'a':1,'b':2}
# d.update(d1)
# print(d)      {'name': '葫芦娃', 'age': 20, 'a': 1, 'b': 2}

#del() 删除
# del d['name']
# print(d)       #{'age': 20}

# #popitem() 随机删除一个键值对，一般删除最后一个，并将键值对以元组形式返回
# d.popitem()
# print(d)

# pop(key[,default])
# 根据key删除字典中的键值对 ，返回删除的value值
#如果删除不存在的key,则会抛出异常，但可以赋初值来解决异常
# result=d.pop('123','键不存在')
# print(result)      #键不存在

#.clear() 清空字典
# d.clear()
# print(d)