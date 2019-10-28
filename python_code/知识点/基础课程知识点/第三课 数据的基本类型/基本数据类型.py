'''----知识：数据类型----'''

#函数：分为内置函数 自定义函数
#Python语言由什么组成？

#1.关键字 2.标志符 3.注释 4.变量和数值 5.运算符 6.语句 7.函数 8.序列

#1.1关键字：import keyword 不能随便更改
#1.2标志符：我们自己定义的一些符合的名称 例如 变量名，类名，函数
   #组成：由26英文字母 数字0-9 符号
   #规则：标识符可以包含数字，字母，下划线，但不可以使用数字开头
        #python中不可以使用关键字和保留字作为标志符
    #命名方式：驼峰命名法
    #小驼峰：第一个单词以小写字母开始，第二个单词首字母大写
    #大驼峰：每个单词首字母都大写
    #下划线命名法：用下划线来连接两个有含义的单词
    #命名尽量：见名识意


#整数都是int类型
#当遇到比较大的数字可以使用下划线进行分割，方便观看
print(5000000000000) #python3.6版本才开始支持500_000_000_000
print(123)  #整数（int）,包括零，负数
#》》123

#小数float类型
print(0.14+0.3)  #浮点数（float）,会有点点误差，不是精确的
#》》3.44

#布尔值：True False 做逻辑运算 bool类型
#布尔值实际上也属于整型，True相当于1  False相当于0
#None常量 既不是0也不是1，代表空的数据

#字符串 str类型
#字符串是由数字、字母、下划线组成的一串字符
#在程序中则是用一对单引号或者双引号包裹的内容就是字符串
print('小千')  #字符串（str）,被引号括起来的
#》》小千

#字符串其他操作:
##字符串长度 len()
##判断一个字符是否在另一个字符串中 in
if '123' in '1234':
    print('属于')  #属于
##判断字符串中的最大值与最小值 max(),min()，对于英文的字母则通过ASCII码来判断
print(max('python'))  #y
print(min('python'))  #h

##ord()函数返回值是ASCII码对应十进制数
print(ord('y'))  #121
print(ord(' '))   #32

# .split() 分割字符串 得到的是list
print('1 34 56'.split())  #['1', '34', '56']

# .join() 拼接字符串
print(','.join('123'))  #1,2,3

# .strip()  去掉一个字符左右两边的空格
# .lstrip()  去掉一个字符左边的空格
# .rstrip() 去掉一个字符右边的空格
print('  python   '.strip()) #python
print('  python   '.lstrip()) #python  #
print('  python   '.rstrip()) #  python

#字符串的大小写
#upper()  全部大写
#lower()  全部小写
#capitalize() 首字母大写
#isupper() islower() 判断是否全是大写 小写
a='I love China'
print(a.upper())  #I LOVE CHINA
print(a.lower())   #i love china
print('xiaobink'.capitalize())  #Xiaobink
print(a.isupper())   #False
print(a.islower())   #False

'''总结：注意字符串与其他类型的数据不能在同一个print()中输出,
        即print('小千今年'+6+'岁')这样是错误的'''
