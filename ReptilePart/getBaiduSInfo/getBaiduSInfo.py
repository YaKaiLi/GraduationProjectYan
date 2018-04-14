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
    sql = "select * from list_of_journal"
    cursor.execute(sql)  # 执行sql语句
    results = cursor.fetchall()  # 获取查询的所有记录
    for row in results:
        #取得html
        req = request.Request("http://xueshu.baidu.com/usercenter/data/journal?cmd=journal_page&entity_id="+row[2])
        response = request.urlopen(req)
        html = response.read()
        charset = chardet.detect(html)#判断网页的编码并以字典方式返回---charset是字典格式的，当中有encoding
        html = html.decode(charset['encoding'])
        #进行正则匹配
        #选出影响因子
        yingxiangyinzipa = re.compile('<span class="label">影响因子</span><span.*?</span>')
        items = re.findall(yingxiangyinzipa, html)
        for item in items:
            item = item.replace('"', '')
            item = item.replace('<span class=label>影响因子</span><span class=>', '')
            item = item.replace('</span>', '')
            yingxiangyinzi = item
        #选出搜索指数
        sousuozhishupa = re.compile('<span class="label">搜索指数</span><span.*?</span>')
        items = re.findall(sousuozhishupa, html)
        for item in items:
            item = item.replace('"', '')
            item = item.replace('<span class=label>搜索指数</span><span class=>', '')
            item = item.replace('</span>', '')
            sousuozhishu = item
        #选出发文量
        fawenliangpa = re.compile('<span class="label">发文量</span><span.*?</span>')
        items = re.findall(fawenliangpa, html)
        for item in items:
            item = item.replace('"', '')
            item = item.replace('<span class=label>发文量</span><span class=>', '')
            item = item.replace('</span>', '')
            fawenliang = item
        #选出被引量
        beiyinliangpa = re.compile('<span class="label">被引量</span><span.*?</span>')
        items = re.findall(beiyinliangpa, html)
        for item in items:
            item = item.replace('"', '')
            item = item.replace('<span class=label>被引量</span><span class=>', '')
            item = item.replace('</span>', '')
            beiyinliang = item
        #选出ISSN
        issnpa = re.compile('<span class="label">ISSN</span><span.*?</span>')
        items = re.findall(issnpa, html)
        for item in items:
            item = item.replace('"', '')
            item = item.replace('<span class=label>ISSN</span><span class=>', '')
            item = item.replace('</span>', '')
            issn = item
        sql_update = "update list_of_journal set yingxiangyinzi = "+str(yingxiangyinzi)+",sousuozhishu = "+str(sousuozhishu)+",fawenliang = "+str(fawenliang)+",beiyinliang = "+str(beiyinliang)+",issn = \""+str(issn)+"\" where id = "+str(row[0])
        cursor.execute(sql_update)  # 像sql语句传递参数
        db.commit()
        print(yingxiangyinzi+"**"+sousuozhishu+"**"+fawenliang+"**"+beiyinliang+"**"+issn)