# 方法一：
#直接print()，然后才发现这是一个直角三角形（难受——）
# print('''* * * * *
# *     *
# *   *
# * *
# *
# ''')

# 方法二：
#通过观察找规律，发现只有第一行和倒数两行是没有空格分开的，其他行的都空格开了且只有首尾才有*
#得出空格space与行数i的关系space=2*i-3
#利用if语句重新构造str
#定义n控制三角形的高度

#倒三角（左边）
print('倒三角（左边）')
n=5
for i in range(n,0,-1):

    if 1<i<n:
        space=' '*(2*i-3)
        str='*'+space+'*'
    else:
        str = '* ' * i
    print(str)
print()

#倒三角（右边）
print('倒三角（右边）')
n=5
for i in range(n,0,-1):
    space1=' '*((2*n)-2*i)

    if 2<i<n:
        space=' '*(2*i-3)
        str=space1+'*'+space+'*'
    else:
        str = space1 + '* ' * i
    print(str)
print()

#正三角（左边）
print('正三角（左边）')
n=5
for i in range(1,n+1):
    str='* '*i
    if 1<i<n:
        space=' '*(2*i-3)
        str='*'+space+'*'
    print(str)
print()

#正三角（右边）
print('正三角（右边）')
n=5
for i in range(1,n+1):
    space1=' '*((2*n)-2*i)

    if 2<i<n:
        space=' '*(2*i-3)
        str=space1+'*'+space+'*'
    else:
        str = space1 + '* ' * i

    print(str)