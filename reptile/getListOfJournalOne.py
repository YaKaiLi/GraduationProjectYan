# -*- coding: UTF-8 -*-
from urllib import request
import chardet
import re

if __name__ == "__main__":
    #取得html
    req = request.Request("http://xueshu.baidu.com/usercenter/data/journal?cmd=journal_search&journal_db=4&journal_name=%E4%B8%AD%E5%9B%BD%E7%A7%91%E6%8A%80%E6%A0%B8%E5%BF%83%E6%9C%9F%E5%88%8A&category=10%2C0")
    response = request.urlopen(req)
    html = response.read()
    charset = chardet.detect(html)#判断网页的编码并以字典方式返回---charset是字典格式的，当中有encoding
    html = html.decode(charset['encoding'])
    #进行正则匹配
    pattern = re.compile('<div class="journal_right">\n.*?<a.*?</a>')
    items = re.findall(pattern, html)
    for item in items:
        print(item)