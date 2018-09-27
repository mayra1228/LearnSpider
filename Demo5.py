#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2018/9/26 下午2:55
# @Author : mayra.zhao
# @File   : Demo5.py
import urllib2

url =  "http://www.baidu.com"
#创建handler
proxyHander = urllib2.ProxyHandler({"https  ": "222.221.11.119:3128"})
#创建opener
openner = urllib2.build_opener(proxyHander)

#install openner
urllib2.install_opener(openner)

#发起网络请求
response = openner.open(url)

data = response.read()

with open("baidu2.html","wb") as f:
    f.write(data)
#print data