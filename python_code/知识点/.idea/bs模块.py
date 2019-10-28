
'''---知识点：BeautifulSoup模块；解析提取网页中的数据---pip install BeautifulSoup4'''

import requests
from bs4 import BeautifulSoup
res=requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html')
html1=res.text
print(res.status_code)
soup=BeautifulSoup(html1,'html.parser')  #BeautifulSoup解析数据的用法（要解析的文本，'解析器')数据类型是<class 'bs4.BeautifulSoup'>
'''item=soup.find('div')
print(type(item))    #<class 'bs4.element.Tag'>是一个Tag对象
print(item)'''
print('---------------------------------------------')
items=soup.find_all(class_='books')
print(type(items))     #<class 'bs4.element.ResultSet'>是一个Resultset对象，相当于把Tag以列表机构储存起来
for item in items:
    kind=item.find('h2')  #在列表中每个元素里，匹配标签<h2>提取出数据
    title=item.find(class_='title')  #匹配属性class_='title'提取数据
    brief=item.find(class_='info')
    print(kind.text,'\n',title.text,'\n',title['href'],'\n',brief.text)


'''1.BeautifulSoup中的文本参数必须是字符串类型
    2.提取数据用find(),find_all()和Tag对象
    3.find（），find_all()这两个方法可以匹配html的标签和属性
    4.find()：提取满足要求的首个数字soup.find('div',class_='books')
    5.find_all():提取所有满足要求的数据soup.find('div',class_='books')
    6.find()检索中的参数:标签和属性混用，class_,style
    7.先看我们要爬的数据，找到所对应的源代码，找出源代码中相同的点来搜索
    8.soup和Tag都有find()andfind_all()
    9.Tag.find():提取Tag中的Tag;Tag.text:提取Tag中的文字；Tag['属性名']:提取Tag中这个属性的值
    
    
'''
