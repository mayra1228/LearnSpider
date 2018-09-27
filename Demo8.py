#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2018/9/26 下午4:11
# @Author : mayra.zhao
# @File   : Demo8.py

import  requests

content = raw_input("请输入需要翻译的中文： ")
url = "https://fanyi.baidu.com/v2transapi"
form = {
"from": "zh",
"to": "en",
"query": content,
"transtype": "translang",
"simple_means_flag": "3"
}

#发送请求
response = requests.post(url,data=form)

data = str(response.content)
print data