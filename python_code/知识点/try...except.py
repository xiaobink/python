'''----知识：try...except----'''

while True:
    try:
        age = int(input('你今年几岁了？'))  #输入不是整数时候会报错，不会执行下一行代码，直接转到except
        break
    except ValueError:
        print('你输入的不是数字！')

if age < 18:
    print('不可以喝酒噢')

#》》你今年几岁了？解决  你输入的不是数字！你今年几岁了？  12  不可以喝酒噢
