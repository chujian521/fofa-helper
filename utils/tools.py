#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# @Time    : 2023/03/27 11:10:12
# @Author  : chujian521
# @File    : tools.py
import re
import hashlib
import requests

def searchkey_to_filename(searchkey: str) -> str:
    """
    @description : 将搜索的关键字转换为文件名
    ---------
    @param  : searchkey: 搜索关键字
    -------
    @Returns : 本次查询保存的文件名
    -------
    """
    def correct_filename(filename): # 去除文件名的特殊字符
        error_set = ['/', '\\', ':', '*', '?', '"', '|', '<', '>']
        for c in filename:
            if c in error_set:
                filename = filename.replace(c, '')
        return filename
    #print(searchkey)
    filename = ''
    keywords = re.findall(r"=(.*?)[ |&|\|]",searchkey)
    if keywords:
        for index in range(len(keywords)):
            keywords[index] = correct_filename(keywords[index])
        filename = "_".join(keywords[:3])
        if len(filename) > 30: # 文件名太长，截断
            filename = filename[:30]
    else:
        m = hashlib.md5()
        m.update(searchkey.encode("utf8"))
        filename = m.hexdigest()
    return filename

#print(searchkey_to_filename('host=".gov.cn////" && country="CN" && status_code="200"'))
 
 
def check_url_valid(url :str) -> bool:
    """
    @description : 检查url是否有效可访问
    ---------
    @param  : url: 网站
    -------
    @Returns : bool
    -------
    """
    
    url = url.strip()
    if 'http' in url or 'https' in url:
        url1 = url
        url2 = None
    else:
        url1 = f'http://{url}'
        url2 = f'https://{url}'
    try:
        ok = requests.get(url1, timeout=(5, 8), allow_redirects=True)
        if ok.status_code == 200:
            #print(url1, ok.status_code)
            return True
        else:
            ok_1 = requests.get(url2, timeout=(5, 8), allow_redirects=True)
            if ok_1.status_code == 200:
                #print(url2, ok_1.status_code)
                return True
            else:
                #print(url2, ok.status_code)
                return False
    except:
        try:
            ok2 = requests.get(url2, timeout=(5, 8), allow_redirects=True)
            if ok2.status_code == 200:
                #print(url2, ok2.status_code)
                return True
            else:
                #print(url2, ok2.status_code)
                return False
        except:
            # print(f"{url2} URL无效")
            return False