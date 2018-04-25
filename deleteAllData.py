# -*- coding: UTF-8 -*-
import pymysql

if __name__ == "__main__":
    # 打开数据库连接
    db = pymysql.connect(host="localhost",user="root",password="root",db="graduationprojectyan",port=3306,charset="utf8")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    sql = "TRUNCATE list_of_journal"
    # 执行sql语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
    # 关闭数据库连接
    db.close()
