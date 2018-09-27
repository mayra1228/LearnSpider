#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2018/9/25 下午6:09
# @Author : mayra.zhao
# @File   : Demo2.py
'''
获取指定的数据（图片，网页，pdf文档）
'''
import urllib2
#获取数据的URL
url="https://www.baidu.com/img/bd_logo1.png?where=super"
#下载数据，获取响应的response
#reponse = urllib2.urlopen(url)
#创建请求对象
request = urllib2.Request(url)
response = urllib2.urlopen(request)
# 读取数据
#data = response.read()
#将数据存入到图片文件中
#with open("baidu2.png",'wb') as f:
#    f.write(data)
#获取相应的数据
#获取请求数据的URL
print response.geturl()
#服务器响应数据信息
print response.info()
#获取响应的返回码
print response.getcode()