'''---知识：if语句---'''

if stonenumber>=6:  #单向判断
    print('你拥有了毁灭宇宙的力量')


if stonenumber>=6:  #双向判断
    print('你拥有了毁灭宇宙的力量')
else:
    print('带着卡魔拉去沃弥尔星寻找灵魂宝石')


if stonenumber>=6:   #多向判断，elif后可不接else
    print('你拥有了毁灭宇宙的力量')
elif 0<stonenumber<=5:
    print('绯红女巫需要亲手毁掉幻视额头上的心灵宝石')

else:
    print('需要惊奇队长逆转未来')


'''总结：1.缩进要么4个空格，要么一个Tab，二者不可混用，否则报错
        2.if语句中可以不要else
        3.if可以嵌套多重if各向结构，else下也可以嵌套if的各向结构
        4.if、elif、else三者是互斥关系
        5.单向if可与break结合使用，可中止并跳出当前循环'''

