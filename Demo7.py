#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2018/9/26 下午4:01
# @Author : mayra.zhao
# @File   : Demo7.py
import  requests
#获取数据url
url= "https://www.baidu.com/img/bd_logo1.png?where=super"

#发送请求
response = requests.get(url)
print type(response)
print response.status_code
print response.headers
#print response.content

with open("baidu2.png","wb") as f:
    f.write(response.content)