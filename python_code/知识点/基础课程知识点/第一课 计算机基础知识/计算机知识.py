'''---知识点：计算机基础---'''

'''
    一、计算机基本概念
    ##1.1概念：计算机俗称电脑，是一种用于高速计算的电子计算器
    包括数值计算，逻辑计算，存储记忆功能等
    
    ##1.2组成：
    硬件：鼠标、键盘、显示器，硬盘，cpu等看得见的
    软件：qq,等等应用...看不见；是一系列按照特定顺序组织的计算机的数据和特定指令的集合
    
    二、计算机语言
    ##2.1 计算机语言的概念
    数字 字符 和语法规则 组成了计算机中的各种指令（或语句）
    是用于人与计算机之间通讯的语言
    ## 2.2 发展
    ->机器语言0,1二进制数据
    ->汇编语言
    ->高级计算机语言（c,java,python...)
    (根据转换的时机不同，高级计算机语言又分为：编译型语言，解释型语言）
    编译型：C  类似食堂吃饭
    x(源码)-->编译-->y(编译后的机器码)
    特点：执行速度快，跨平台比较差
    解释型：Java，Python  类似饭店吃饭
    x(源码)-->解释器-->解释执行
    特点：执行速度较慢，跨平台较好
    
    三、交互方式
    ##3.1 交互方式种类
    ->命令行的交互方式    TUI I(interface:接口)
    ->图形界面化的交互方式 GUI
    
    交互模式的打开方式
    TUI win:win+R->cmd 回车
    
    ##3.2常见的Dos命令
    .当前文件夹
    ..上一级文件夹
    *.txt:当前路径中的txt文件
    dir:显示当前路径文件，文件夹
    cd:进入文件夹
    rd:删除文件，文件夹
    md:创建文件，文件夹
    
    四、文本文件和字符集

    文本一般分为两种：
    纯文本  只可保存单一内容（图片，字体颜色...)
    富文本  可保存文本以外的内容太（有道笔记，word文档...）
    
    开发时用纯文本开发
    将字符转换成二进制的过程称为 编码
    将二进制转换成字符的过程称为 解码
    
    编码和解码所采用的规则称为字符集
    常见字符集
    ASCII表
    使用7位来对美国常用的字符进行编码 包含128个字符
    
    ISO-8859-1表
    欧洲人 使用8位 包含256个字符
    
    GBK
    国标码 中国的编码
    
    Unicode
    万国码 包含世界上所有的语言和符号
    有很多种实现方式：utf-8(最常用) utf-16
    utf-8 范围1-5字节 utf-16 2-4个字节
    
    字节（byte）
    计算机用于计量存储和传输容量的一种计量单位
    1字节=8位二进制
    一个英文字母（不区分大小写）占一个字节空间
    一个中文汉字占两个字节空间
    
    符号 英文标点占一个字节，中文标点占两个字节
    
    字符：指计算机中使用的字母、数字、字和符号
    
    五、进制
   
    生活中：十进制
    计算机：二进制
    问、为什么要出现其他形式的进制？
    答、进制越大表现形式越短 更方便表示数据
    ##5.1进制间转换
    十进制->二进制
     原理：对十进制进行除2运算 反之则乘2运算
     
    ##5.2进制的计数
    十进制：满十进一，一共10个数字
    十进制计数：0,1,2,3,4,5,6...11,12,13,14...
    
    二进制：满二进一  一共2个数字
    二进制计数 0,1,10,100,101,110...
    
    八进制：满八进一 一共8个数字
    0,1,2,3,4,5,6,7,10,11,12...17,20,21...30
    
    十六进制：满十六进一 一共10个数字个6个字母（a-f）
    十六进制计数：0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f,10,11...1e,1f,20
    
    ##5.3数据间的换算
    bit:是计算机中最小的存储单位
    byte：是我们可以操作的最小单位
    1byte=8bit
    1kb(千字节)=1024bye
    mb(兆字节) gb(吉字节) tb(太字节)
    
    六：环境变量（environment variable）
    ##6.1环境变量值是操作系统中的一些变量
      1.查看环境变量，右击我的电脑，属性，高级设置，环境变量
      2.一个环境变量可以多个值，用英文分号分隔开
      
      ##6.2 path环境变量
      path 环境变量：保存的是一个一个的路径
      我们在命令行输入一个命令（或访问一个文件时）
      系统会在当前目录下寻找，如果没有，则去path环境变量中依次寻找，若找不到则报错。
      
    
    
    
'''