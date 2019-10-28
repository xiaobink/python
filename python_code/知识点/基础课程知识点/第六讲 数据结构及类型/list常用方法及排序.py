
#len() 判断list的长度
list1=[1,5,2,3]
# print(len(list1))  #3

#返回list中的最大值、最小值
# print(max(list1))  #3
# print(min(list1))  #1

#list(seq) 强制类型转换，将序列转化为list
# print(list('str'))

#list排序和反转 改变的是原始列，返回值为空
#反转.reverse()  IN PLACE:修改本身  reverse:颠倒，反转
# list1.reverse()
# print(list1)   #[3, 2, 1]

#使用切片可以反转列表
# lst=['one','two','three']
# print(lst[::-1])

#排序.sotr() 改变的是原始列，返回值为空
# list1.sort()
# print(list1)  #[1, 2, 3, 5]

# list1.sort(reverse=True)
# print(list1)  #[5, 3, 2, 1]

# list2=[1,'str',2]
# list2.sort()
# print(list2)   #报错 不能讲int 和str进行排序，但str与str可以通过ASCII码来判断

#使用enumerate()获取列表下标和数据,返回的是元组
lst=['one','two','three']
for i,n in enumerate(lst):
    pass
    print(i,n)