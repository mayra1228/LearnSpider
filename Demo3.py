#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2018/9/25 下午9:49
# @Author : mayra.zhao
# @File   : Demo3.py
'''
使用baidu的api完成英汉互译
'''
import urllib2
import urllib

#百度翻译的地址
url = 'https://fanyi.baidu.com/v2transapi'
param = {
"from": "zh",
"to": "en",
"query": "测试",
"transtype": "translang",
"simple_means_flag": "3",
"sign": "865709.644764",
"token": "d79849ca329459c4a6666292ee060a7c"
}
#将参数转码
param = urllib.urlencode(param)

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
#发送请求
request = urllib2.Request(url, data = param, headers = headers)
response = urllib2.urlopen(request)

#读取响应数据
data = response.read()
print data
print type(data)