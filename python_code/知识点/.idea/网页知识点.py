'''---知识点：html了解---
    html(hyper text markup language):超文本标记语言'''

'''
<html>
    <head>   <!--网页头-->
        <meta charset="utf-8">    <!--网页编码格式-->
        <title>这个书苑不太冷</title>  <!--网页标题，浏览器上方的标签页中-->
        <style>
        .book{        <!--代表class book，其中class为属性，book为属性值-->
        float:left;   <!--控制元素浮动-->
        margin:5px;   <!--外边距为5像素-->
        padding:15px;  <!--内边距为15像素-->
        width:350px;   <!--宽度为350像素-->
        height:240px;  <!--高度为240像素-->
        border:3px solid #20b2aa;  <!--边框为3像素-->
        }
        </style>
    </head>
    <body>   <!--网页体-->
        <h1 style="color:#20b2aa;">这个书苑不太冷</h1>   <!--一级标题-->设置属性style规定h1元素中的内容字体颜色
        <h2>《奇点移民》</h2>      <!--二级标题-->
        <a herf="https://spidermen.cn" target="_blank">点这里看看</a>  
        <br>
        <h3>我是三级标题</h3>      <!--三级标题-->
        <div class="book">       <!--调用class属性-->
            <p>我是一个段落文本；一级标题，二级标题，三级标题，我们四个一起组成了body。
            </p>
        </div>
    </body>
</html>
'''
'''1.ctr+u 查看网页源代码（新标签页中显示源代码）
    2.ctr+shift+i 检查（可编辑源代码）
    3.标签<>、元素、结构（网页头head和网页体body）、属性，组成html文档
    4.尖括号中的字母叫标签，通常成对出现，<html>：是起始标签</html>：是结束标签；
    也有标签是单个的，比如：<meta charset="utf-8"(定义网页编码格式为 utf-8)
    5.开始标签+中间内容+结束标签=元素。如：<body> 内容 </body> 组成body元素
    6.<a>描述链接的文本</a>,  <div>其他元素或文本</div>
    7.html标签可以设置属性来为元素描述更多信息，常用属性如下：
    8.style属性：可以设置字体大小、颜色、间距、对齐方式等等
    9.href属性：用来添加链接，指向页面的URL，一般由<a>标签定义
    10.class属性：.book中的.对应class属性，而book则是属性值，可被调用多次，标识一系列元素
    11.id 属性：用于标识唯一的元素
    <div id="header">  顶部标题
    <div id="article">  中间的内容
        <div id="nav">  侧边栏
        <div id="main">  正文部分
    <div id="footer">   底部内容
    12.name属性，可用于定义跳转内部的链接名称<a name="type1">链接名称</a>
    13.网页修改只是在本地，不会上传到服务器上
    
'''