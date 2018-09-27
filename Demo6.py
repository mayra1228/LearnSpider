#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2018/9/26 下午3:20
# @Author : mayra.zhao
# @File   : Demo6.py.py

import requests

# 获取访问的URL
url = "http://www.baidu.com"
# 发送请求
response = requests.get(url)

data = str(response.content)

# 将数据存入文件
with open("baidu3.html", 'w') as f:
    f.write(data)
