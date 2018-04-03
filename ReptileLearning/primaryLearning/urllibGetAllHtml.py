# -*- coding: UTF-8 -*-
from urllib import request
import chardet

if __name__ == "__main__":
    response = request.urlopen("http://fanyi.baidu.com")
    html = response.read()
    charset = chardet.detect(html)#判断网页的编码并以字典方式返回---charset是字典格式的，当中有encoding
    print(charset)