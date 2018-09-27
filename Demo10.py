#!/usr/local/bin/python2.7
# -*- coding:utf-8 -*-
# @Time   : 2018/9/27 下午3:04
# @Author : mayra.zhao
# @File   : Demo10.py
'''
通过正则表达式下载煎蛋网图片
'''
import requests
import re
import hashlib
import base64
import os

if not os.path.exists("images"):
    os.makedirs("images")

currentpage = -1

#url = 'http://jandan.net/pic/234#comments'
#js_url = "http://cdn.jandan.net/static/min/91798e4c623fa60181a31d543488217eRi4hG4o3.19100001.js"
m = "Ly93dzMuc2luYWltZy5jbi9tdzYwMC8wMDZYTkVZN2d5MWZ2bzNpd3VpOHdqMzA4ejBjbmdtay5qcGc="
r = "MAtwsoYqDOMfbxgCwo0FZMxdOvxgw2Uj"

'''md5加密'''
def _md5(value):
    m = hashlib.md5()
    m.update(value.encode('utf-8'))
    return m.hexdigest()

'''bash64解码，要注意原字符串长度报错问题'''
def _base64_decode(data):
    return base64.b64decode(data + (4 - len(data) % 4) * '=')

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


'''获取关键字符串'''
def get_r(js_url):
    data = requests.get(js_url)
    js = data.content
    _r = re.findall('c=[\d\w]+\(e,"([\w\d]+)"\)' , js)[0]
    return _r

'''获取一个页面所有图片的链接'''

def get_urls(url, page):
    path = "images/{}".format(page)
    if not os.path.exists(path):
        os.makedirs(path)

    # 设置请求头数据
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
    }
    # 下载发送请求
    response = requests.get(url, headers=headers)
    # 解析数据
    html = response.content

    #获取js url
    js_url = 'http:' + re.findall('<script src="(//cdn.jandan.net/static/min/[\w\d]+\.\d+\.js)"></script>', html)[-1]
    _r = get_r(js_url)
    tags = re.findall('"img-hash">([\w\d]+)', html)
    for tag in tags:
        img_hash = tag
        img_url = 'http:' + get_imgurl(img_hash,_r)

        response = requests.get(img_url)
        data = response.content
        ImageName =  img_url.split("/")[-1]
        ImagePath = "images/{}/{}".format(page, ImageName)
        with open(ImagePath,'wb') as f:
            f.write(data)

if __name__ == '__main__':
    for page in range(1,10):
        page = str(page)
        url = 'http://jandan.net/pic/'+ page + '#comments'
        print url
        get_urls(url, page)


