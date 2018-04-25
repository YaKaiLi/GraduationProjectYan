# -*- coding: UTF-8 -*-
from urllib import request
import chardet
import re
import pymysql

if __name__ == "__main__":
    # 打开数据库连接
    db = pymysql.connect(host="localhost",user="root",password="root",db="graduationprojectyan",port=3306,charset="utf8")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    #取得html
    req = request.Request("http://xueshu.baidu.com/usercenter/data/journal?query=&category=2%2C0&journal_db=4&journal_name=%E4%B8%AD%E5%9B%BD%E7%A7%91%E6%8A%80%E6%A0%B8%E5%BF%83%E6%9C%9F%E5%88%8A&page=3")
    response = request.urlopen(req)
    html = response.read()
    charset = chardet.detect(html)#判断网页的编码并以字典方式返回---charset是字典格式的，当中有encoding
    html = html.decode(charset['encoding'])
    #进行正则匹配
    pattern = re.compile('<div class="journal_right">\n.*?<a.*?</a>')
    items = re.findall(pattern, html)
    for item in items:
        temp = item.replace('\n', '')
        temp = temp.replace(' ', '')
        temp = temp.replace('"', '')
        temp = temp.replace("'", '')
        temp = temp.replace("<divclass=journal_right><ahref=/usercenter/data/journal?cmd=journal_page&entity_id=", '')
        temp = temp.replace("target=_blankclass=journal_titleLOG_WRdata-click=titledata-log={actblock:journal_jump,type:according_journal_name}>", '')
        temp = temp.replace('</a>', '')
        # SQL 插入语句
        sql = "INSERT INTO list_of_journal(name,baidusid) VALUES ('"+temp[32:]+"','"+temp[:32]+"')"
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        print(temp[32:])
    # 关闭数据库连接
    db.close()

