'''----知识：while循环----'''

i = 0
while i<5:
    
    i = i+1
    if i==3:    # 当i等于3的时候触发break
        break
    print('明日复明日',end='  ')
 
#》》明日复明日  明日复明日 


i = 0
while i<5:
    
    i = i+1
    if i==3:    # 当i等于3的时候触发break
        continue
    print('123',end='  ')
#》》123  123  123  123



'''总结：1.for循环和while循环都可以帮我们完成重复性的劳动。
        2.while循环用于循环次数不确定的情况下。
        3.while True:即：当条件为真时才会执行循环
        4.break一般与if连用，后不接else，执行到break时，结束循环
        5.continue一般与if连用,后不接else,回到循环开头进行下一次循环,不执行后面的语句.
        6.pass语句，跳过当前位置，往下继续执行
        7.else语句，当循环中没有碰到break语句，就会执行循环后面的else语句，否则就不会执行
        8.外层循环控制高度，内层循环控制宽度
         
'''
