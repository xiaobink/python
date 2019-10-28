# list1=[1,2,3,4,5,6]
# print(list1[1:3])  #[2,3],左开右闭
# print(list1[:]) #复制列表
# [1, 2, 3, 4, 5, 6]

# print(list1[::2]) #步长为2
# [1, 3, 5]
#使用切片
# lst=['one','two','three']
# print(lst[::-1])  #使用切片可以反转列表

#.append() 添加元素
# list1=[1,2,3,4,5,6]
# list1.append('e')
# list1.append([7,8])
# print(list1)  #[1, 2, 3, 4, 5, 6, 'e', [7, 8]]

#.count(value)统计某个值在list中出现的次数
# list1=[1,2,3,4,5,6,2,2]
# print(list1.count(2))  #3

#.extend(seq)  在列表末尾一次性追加另一个序列的多个值，是把序列中的每个值添加进去，而.append()是将整个序列原封不动的添加进去
# list1=[1,2,3,4,5,6,2,2]
# list1.extend(['a','b','c'])
# print(list1)  #[1, 2, 3, 4, 5, 6, 2, 2, 'a', 'b', 'c']
#不能直接写成print(list1.extend(['a','b','c']) .append()也是，因为无返回值

# .insert(index,value)
# 将对象通过索引插入列表
# list1=[1,2,3,4,5,6,2,2]
# list1.insert(2,'hello')
# print(list1)  #[1, 2, 'hello', 3, 4, 5, 6, 2, 2]

#.copy() [:]浅拷贝，只复制值，不复制对象的id
# list1=[1,2,3,4,5,6,2,2]
# list2=list1.copy()
# print(list1,id(list1))  #[1, 2, 3, 4, 5, 6, 2, 2] 2474244330056
# print(list2,id(list2))  #[1, 2, 3, 4, 5, 6, 2, 2] 2474244330568

#.clear() 清空列表
# list1=[1,2,3,4,5,6,2,2]
# list1.clear()
# print(list1)
