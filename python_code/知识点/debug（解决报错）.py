'''----debug----'''

'''
1.SyntaxError：语法错误
    eg1：File "/home/python-class/classroom/apps-1-id-5cd9765e19bbcf00015547b8/26/main.py",
        line 2
        if a == '123456'^                  
    SyntaxError: invalid syntax（无效的语法）

    （1）line 2代表这个bug出现在第2行。
    （2）^代表bug发生的位置，这里指出的位置是第二行末尾。
    （3）这一行写的是错误类型，SyntaxError指的是语法错误。

    eg2:
    def __init__(self,name,job='programmer',time):            ^
    SyntaxError: non-default argument follows default argument
    语法错误：无默值参数跟在有默认值参数后边（无默认值的参数要放在有默认值参数的前面）

    eg3:
    def __init__(self,book_name,author,recommend，state):
                                                     ^
    SyntaxError: invalid character in identifier
    语法错误：有无效的字符（符号）在标识符中

2.IndexError：索引错误。
    eg1：sunday = week[7]
    IndexError（索引错误）: list index out of range（范围）

3.TypeError:'类'错误
    eg1：
    a.append ('C',123)
    TypeError:append() takes exactly one argument (2 given)
    类错误：append（）只接受一个参数（给定2个）

    eg2:
    toss = random.choice['正面','反面']
    TypeError: 'method' object is not subscriptable(可通过下标访问的)
    类错误：random.choice这个函数对象是不可索引的(少了括号)
    method解释：是与类相关的函数，比如:random函数中有range,choise等这些称之为类（method）

    eg3：
    toss = random.randint('正面','反面')
    TypeError: can only concatenate str (not "int") to str
    类错误：只能将str（而不是“int”）连接到str

    eg4:
    num = [1,2,3,1.5,'6']
    for x in num:
        print (6/x)
    TypeError: unsupported operand type(s) for /: 'int' and 'str'
    类错误:对于/（除法）来说：int/str是不支持的运算数类型

    eg5:
    student2 = Programmer('李雷')
    TypeError: __init__() missing 1 required positional argument: 'time'
    类型错误：初始化中丢失了一个必要的位置参数：time
    
    eg6:
    print('书名：%s,价格：%s,星星评分：'%(name['title'],price.text,star['class'][1]))
    TypeError: not all arguments converted during string formatting
    类型错误：str在format格式化中不是所有的参数都被覆盖（参数给多了，或者替代符%s漏了）
    
    eg7:
    def get_url():
    
    def news(url_list):
    
    news(get_url)
    TypeError: 'function' object is not iterable
    Type错误：“函数”对象不是可迭代的
    
    eg8:
    import base64
    s='肖分斌'
    a=base64.b64encode(s)
    print(a)
    TypeError: a bytes-like object is required, not 'str'
    类型错误：需要的是一个类似字节型对象，而不是字符串
    （因为python3.x版本中字符都为unicode编码，而b64encode函数的参数为byte类型，所以必须先转码）
    
4.AttributeError: 属性错误
    eg1:
    toss = random.choise('正面','反面')
    AttributeError: module 'random' has no attribute 'choise'
    属性错误：模块'random'没有属性去choise（选择）

    eg2:
    student1.coun_time(10,0.8)
    AttributeError: 'Student' object has no attribute 'coun_time'
    属性错误：Student这个对象中没有coun_time这个属性

5.ValueError:值错误
    ag1:
    age = int(input('你今年几岁了？'))
    输入了“hh”
    ValueError: invalid literal for int() with base 10: 'hh'
    值错误：无效的字面意思，'hh'对int来讲是无效值

    ag2:
    x = input('请你输入被除数：')
    y = input('请你输入除数：')
    z = float(x)/float(y)
    输入了字母
    ValueError: could not convert string to float: 'l'
    值错误：不能把字符串转化成浮点数

6.UnboundLocalError: 全局变量报错(解除绑定局部错误)
    eg1:
    scores = {'语文':89, '数学':95, '英语':80}
    sum_score = 0
    def get_average(scores):
        for subject, score in scores.items():
            sum_score += score
            print('现在的总分是%d'%sum_score)
    get_average(scores)
    
    UnboundLocalError: local variable 'sum_score' referenced before assignment
    全局变量报错：局部变量 'sum_score'在赋值之前被引用

    如果内部函数有引用外部函数的同名变量或者全局变量,并且对这个变量有修改.那么python会认为它是一个局部变量,又因为函数中没有sum的定义和赋值，所以报错

7.TabError: Tab键错误
    eg1：
    try:
       ^
    TabError: inconsistent use of tabs and spaces in indentation
    Tab键错误：缩进中制表符和空格的使用不一致（二者是不能混用的）

8.IndentationError:缩进错误
    eg1：
    def __init__ (self):
    ^
    IndentationError: unexpected indent
    缩进错误：意想不到的缩进

    eg2：
    class Chinese:
        ^
    IndentationError: expected an indented block
    缩进错误：这一块需要缩进

9.FileNotFoundError: 文件未找到错误
    FileNotFoundError: [Errno 2] No such file or directory: 'Users/Bin/Desktop/test/abc.txt'
     文件未找到错误：没有这样的文件或目录：“users/bin/desktop/test/abc.txt”

10.UnicodeDecodeError: 万国码解码错误
    eg1:
    file1=open(r'C:\Users\fenbin\Desktop\test\abc.txt','r',encoding='utf-8')
    UnicodeDecodeError: 'utf-8' codec can't decode byte 0xc3 in position 2: invalid continuation byte
    万国码解码错误：utf-8的编解码器不能解码位置2中的字节0xc3：无效延续字节
    解决方法：打开记事本之后，选择头部菜单的“文件–》另存为”，可以看到文件的默认编码格式为ANSI
    
11.bs4.FeatureNotFound:  bs4.功能未找到.
    eg1:
    soup=BeautifulSoup(ygdy,'parser')
    bs4.FeatureNotFound: Couldn't find a tree builder with the features you requested: parser.
    bs4.功能未找到：找不到您请求的解析器：parser
    
12.KeyError: 'data-code':关键词错误：data-code   
    eg1：
    for postnames1 in postnames[:1]:
        a=postnames1.find_all('a')
        for name in a:
            print(name['data-code'])
    File "C:\Python37\lib\site-packages\bs4\element.py", line 971, in __getitem__
    return self.attrs[key]
    就是有一个或多个地方的a标签中是没有data-code这个属性的，故不能返回其对应值而报错
    
13.PermissionError:权限错误
    Permission denied: '知乎张佳玮.csv'，拒绝访问：: '知乎张佳玮.csv'（就是我已经在本地 打开了该文件）
    
14.UnsupportedOperation:不支持的操作
    eg1:
        with open('各大网站热搜榜top15.txt','wb') as file:
        attach1_data=file.read()    #获取txt文档中的数据
    UnsupportedOperation:read()   上边写的wb,下边用read(),低级错误

15.UnboundLocalError: 变量绑定的位置错误
    UnboundLocalError: local variable 'name_list' referenced before assignment
    局部变量：name_list 定以前被引用
'''
