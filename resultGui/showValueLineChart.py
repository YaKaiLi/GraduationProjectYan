import pymysql
import numpy
import matplotlib.pyplot as plt
from pylab import *                                 #支持中文
mpl.rcParams['font.sans-serif'] = ['SimHei']

db = pymysql.connect(host="localhost", user="root", password="root", db="graduationprojectyan", port=3306,
                     charset="utf8")
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
sql = "select * from list_of_journal order by `value` "
cursor.execute(sql)  # 执行sql语句
results = cursor.fetchall()  # 获取查询的所有记录
total = numpy.array(results)
names = total[:,1]
value = total[:,11]

for i in range(0,value.shape[0]):
    value[i] = value[i][0]+value[i][1]+value[i][2]+value[i][3]

plt.figure(figsize=(40,5))
plt.xticks(range(len(names)), names, rotation=45)
plt.bar(range(len(value)), value,color='rgb',tick_label=names)
plt.xlabel("期刊名称") #X轴标签
plt.ylabel("综合评价值") #Y轴标签
plt.title("期刊评估折线图") #标题
plt.show()