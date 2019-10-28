'''----知识：for...in...循环----'''

for i in [1,2,3,4,5]:  #遍历list
   print(i,end='  ')
#》》1  2  3  4  5

for i in range(0,5,2):  #遍历range()函数（生成一个从0到4且步长为2的整数序列,）
    print(i,end='  ')
#》》0  2  4


dict = {'日本':'东京','英国':'伦敦','法国':'巴黎'}

for i in dict:            #遍历字典的键
    print(i,end='  ')
#》》日本  英国  法国


for i in range(5):
    print('111',end='  ')
    if i==3:                  # 当i等于3的时候触发
        break                 # 结束循环
      
   
#》》111  111  111  111


for i in range(5):
    
    if i==3:                  # 当i等于3的时候触发
        continue              # 回到循环开头,不执行后面的语句
    print('123',end='  ')
#》》123  123  123  123
    

'''总结：1.for循环常用于循环次数已确定的题目中。
        2.可与else结合使用，二者不是互斥关系，在for循环结束后，运行else,若for循环被提前中止，则不运行else语句
        3.布尔值：True 和 False
        4.常见的假的有False，0，'',[],{},None
        5.常见的真的有True,1,1.0,'小千'，[1,2,3],{1:23,2:45}
        6.break一般与if连用，后不接else，执行到break时，结束循环
        7.continue一般与if连用,后不接else,回到循环开头进行下一次循环,不执行后面的语句
        8.pass语句，跳过当前位置，往下继续执行
        9.else语句，当循环中没有碰到break语句，就会执行循环后面的else语句，否则就不会执行'''

