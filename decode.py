#!/usr/local/bin/python2.7
# -*- coding:utf-8 -*-
# @Time   : 2018/9/27 下午4:30
# @Author : mayra.zhao
# @File   : decode.py

import hashlib
import base64

# noinspection PyTypeChecker
def get_imgurl(m, r='', d=0):
    '''解密获取图片链接'''
    e = "DECODE"
    q = 4
    r = _md5(r)
    o = _md5(r[0:16])
    n = _md5(r[16:32])
    l = m[0:q]
    c = o + _md5(o + l)
    m = m[q:]
    k = _base64_decode(m)
    url = ''
    url = k.decode('utf-8', errors='ignore')
    url = '//w' + url
    return url

def _md5(value):
    '''md5加密'''
    m = hashlib.md5()
    m.update(value.encode('utf-8'))
    return m.hexdigest()

def _base64_decode(data):
    '''bash64解码，要注意原字符串长度报错问题'''
    return base64.b64decode(data + (4 - len(data) % 4) * '=')

m = "Ly93dzMuc2luYWltZy5jbi9tdzYwMC8wMDZYTkVZN2d5MWZ2bzNpd3VpOHdqMzA4ejBjbmdtay5qcGc="
r = "MAtwsoYqDOMfbxgCwo0FZMxdOvxgw2Uj"

print get_imgurl(m,r)