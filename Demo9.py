#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2018/9/26 下午5:21
# @Author : mayra.zhao
# @File   : Demo9.py
import re

# 字符集的匹配
# a = re.match(r'[0-9]',"123456")
# print a.group()
#from typing import Match

# . 表示任一字符，除了\n
# a = re.match(r'...','123')
# print a.group()

a = re.match(r'[0-8]?[0-9]','95')
print a.group()
b = re.match(r'[A-Z][a-z]*', "XasssssX123")
print b.group()
c = re.match(r'\d{6,12}@qq\.com','2545620930@qq.com')
print c.group()

d = re.match(r'[0-9][a-z]*','9abcdef')
print d.group()

e = re.match(r'[0-9][a-z]*?','9abcdef')
print e.group()
f = re.match(r'[0-9][a-z]+?','9abcdef')
print f.group()

content = "nick\nnjenny\nsuo"
a = re.search(r'^s.*', content, re.M  )
print a.group()

