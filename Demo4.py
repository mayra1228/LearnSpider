#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2018/9/26 上午9:51
# @Author : mayra.zhao
# @File   : Demo4.py
import  urllib2
import ssl
#请求的URL
url = "https://www.csdn.net"
headers = {
"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
}
context = ssl._create_unverified_context()
#创建请求对象
request = urllib2.Request(url, headers = headers )

#发送请求
response = urllib2.urlopen(request, context = context)

#读取数据
data_P = response.read().decode("utf8")

print data