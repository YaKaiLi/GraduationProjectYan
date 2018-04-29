# -*- coding: UTF-8 -*-
import pymysql
import numpy
import tkinter
from tkinter import ttk  # 导入内部包


db = pymysql.connect(host="localhost", user="root", password="root", db="graduationprojectyan", port=3306,
                     charset="utf8")
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
sql = "select * from list_of_journal order by `value` DESC"
cursor.execute(sql)  # 执行sql语句
results = cursor.fetchall()  # 获取查询的所有记录
total = numpy.array(results)
names = total[:,1]
value = total[:,11]

for i in range(0,value.shape[0]):
    value[i] = value[i][0]+value[i][1]+value[i][2]+value[i][3]

win = tkinter.Tk()
win.title("期刊评估排名")
tree = ttk.Treeview(win,height=20, show="headings")  # 表格
tree["columns"] = ("期刊名称", "综合评价值", "排名")
tree.column("期刊名称", width=120)  # 表示列,不显示
tree.column("综合评价值", width=100)
tree.column("排名", width=50)

tree.heading("期刊名称", text="期刊名称")  # 显示表头
tree.heading("综合评价值", text="综合评价值")
tree.heading("排名", text="排名")

for i in range(0,value.shape[0]):
    tree.insert("", 'end', values=(names[i], value[i], str(i+1)))  # 插入数据，

tree.pack()
win.mainloop()