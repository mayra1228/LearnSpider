 #!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2018/9/25 下午5:34
# @Author : mayra.zhao
# @File   : Demo1.py
'''
获取一个网页数据
'''
import urllib2
#获取需要获取数据的URL
url = "http://baidu.com"
#通过urllib获取数据
response = urllib2.urlopen(url)
#读取数据
html = response.read()
#print(type(data))
#print data
#将html存入文件中
with open("baidu.html",'w') as f:
    f.write(html)

#浏览器访问http://127.0.0.1:63342/SpiderLearn/baidu.html可以看到该页面