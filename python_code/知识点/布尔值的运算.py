'''----知识：布尔值的运算----'''
a = 1
b = -1


if a==1 and b==1:    # and运算【b实际上是-1】
    print('True')
else:
    print('False')
#》》False



if a==1 or b==1:    # or运算【b实际上是-1】
    print('True')
else:
    print('False')
#》》True


if not 0:           # not运算
    print('True')
#》》True

    
list = [1,2,3,4,5]
a = 1
print(bool(a in list))    # in运算，判断“a是否在列表list之中”
#》》True


print(bool(a not in list))  # not in运算，判断“a是否不在列表list之中”
#》》False


'''总结：1.and需要条件都要成立（为真），才为真。
        2.or只要有一个为真都为真
        3.in,来判断元素、键是否在list、dic中'''
