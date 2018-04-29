import pymysql
import numpy
import matplotlib as mpl
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
yingxiangyinzi = total[:,13]
sousuozhishu = total[:,14]
fawenliang = total[:,15]
beiyinliang = total[:,16]
citationsperdocument = total[:,17]
selfcites = total[:,18]
externalcitesperdoc = total[:,19]
citesperdoc = total[:,20]

#开始画图
colors = ['r','y','g','b','k','c','m','m','m']
label = ["value", "yingxiangyinzi", "sousuozhishu", "fawenliang", "beiyinliang", "citationsperdocument", "selfcites", "externalcitesperdoc", "citesperdoc"]
x = range(len(names))
plt.figure(figsize=(40,20))
plt.plot(x, value, 'o-',color = 'r',label='value')
plt.plot(x, yingxiangyinzi, 'o-',color = 'y',label='yingxiangyinzi')
plt.plot(x, sousuozhishu, 'o-',color = 'g',label='sousuozhishu')
plt.plot(x, fawenliang, 'o-',color = 'b',label='fawenliang')
plt.plot(x, beiyinliang, 'o-',color = 'k',label='beiyinliang')
plt.plot(x, citationsperdocument, 'o-',color = 'c',label='citationsperdocument')
plt.plot(x, selfcites, 'o-',color = 'm',label='selfcites')
plt.plot(x, externalcitesperdoc, '--',color = 'm',label='externalcitesperdoc')
plt.plot(x, citesperdoc, 'v-.',color = 'm',label='citesperdoc')
plt.xticks(x, names, rotation=45)
plt.margins(0.08)
plt.subplots_adjust(bottom=0.15)
plt.legend(label, loc = 0, ncol = 2)
plt.title("期刊评估各指标折线图")
plt.ylabel("各指标归一化后的值")
plt.show()