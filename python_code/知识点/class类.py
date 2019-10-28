'''----知识：类(class)----'''
'''1.在Python的术语里，我们把类的个例就叫做实例 (instance)，可理解为“实际的例子”。
    2.Python中的对象等于类和实例的集合：即类可以看作是对象，实例也可以看作是对象，
    比如列表list是个类对象，[1,2]是个实例对象，它们都是对象。
    3.属性（attribute）：第一种是描述事物是怎样的，有什么特征
    4.方法(mothod)：第二种是描述事物能做什么，有哪些行为和作用
    5.第一点：只要在类中用def创建方法时，就必须把第一个参数位置留给 self，并在调用方法时忽略它（不用给self传参）。
    第二点：当在类的方法内部想调用类属性或其他方法时，就要采用self.属性名或self.方法名的格式。
    6.self会接收实例化过程中传入的数据，当实例对象创建后，实例便会代替 self，在代码中运行'''

class Computer:
    screen = True   #属性

    def start(self):      #方法
        print('电脑正在开机中……')

my_computer = Computer()       #实例名=类名()
print(my_computer.screen)      #实例.属性
my_computer.start()             #实例.方法

class Chinese:

    def greeting(self):
        print('很高兴遇见你')

    def say(self):        #在方法中调用其他方法
        self.greeting() 
        print('我来自中国')

person = Chinese()
person.say()

class Chinese:
    def __init__(self):    #初始化方法，
        print('很高兴遇见你，我是初始化方法')
person=Chinese()      #方法初始化后，无需再调用改方法，会自动运行方法内的代码


class Chinese:  # 类的创建
    eye = 'black'  # 类属性的创建

    def __init__(self,hometown):  # 类的初始化方法
        self.hometown = hometown  # 实例属性的创建
        print('程序持续更新中……')  # 初始化中的语句
    
    def born(self):  # 实例方法的创建
        print('我生在%s。'%(self.hometown))  # 方法的具体语句

wufeng = Chinese('广东')  # 类的实例化
print(wufeng.eye)  # 打印实例的属性（从类传递的）
wufeng.born()  # 实例方法的调用
