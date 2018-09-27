#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2018/9/27 下午7:14
# @Author : mayra.zhao
# @File   : JanDanSpider.py
'''
通过正则表达式下载煎蛋网图片
'''
import requests
import re
import hashlib
import base64

class Spider:
    def __init__(self):
        pass

     #下载html代码数据
    def DownPageHtml(self):
        pass

    #处理html代码数据
    def GetDataFromHtml(self):
        pass

    #存储数据
    def SaveData(self):
        pass

    #开始爬虫
    def BeginSpider(self):
        self.DownPageHtml()

if __name__='__main__':
    spider = Spider()
    spider.BeginSpider()
