import pymysql  # 导入 pymysql
import numpy
from sklearn import preprocessing
from sklearn.decomposition import PCA
# 打开数据库连接
db = pymysql.connect(host="localhost", user="root",password="root", db="graduationprojectyan", port=3306,charset="utf8")

# 使用cursor()方法获取操作游标
#cur = db.cursor(cursor=pymysql.cursors.DictCursor)
cur = db.cursor()

# 1.查询操作
# 编写sql 查询语句  user 对应我的表名
sql = "select * from list_of_journal"
cur.execute(sql)  # 执行sql语句

results = cur.fetchall()  # 获取查询的所有记录
total = numpy.array(results)
#total = list(results)
#print("id", "name", "password")

# 遍历结果将空值替换为np.nan
for row in total:
    for j in range(0,8):
        if row[j] == 'NULL':
            row[j]=numpy.nan
#删除前三个与数据无关的字段
shanchuwuguan = numpy.delete(total, 0, axis=1)
shanchuwuguan = numpy.delete(shanchuwuguan, 0, axis=1)
shanchuwuguan = numpy.delete(shanchuwuguan, 0, axis=1)
shanchuwuguan = numpy.delete(shanchuwuguan, -1, axis=1)


#进行插值
imp = preprocessing.Imputer(missing_values='NaN', strategy='mean', axis=0)
imp.fit(shanchuwuguan)
chazhijieguo = imp.transform(shanchuwuguan)

#数据标准化
biaozhunhua = preprocessing.scale(chazhijieguo)
#数据归一化
min_max_scale = preprocessing.MinMaxScaler()
guiyihua = min_max_scale.fit_transform(biaozhunhua)
#数据同趋化
for row in guiyihua:
    row[0] = 1-row[0]
    row[-1] = 1-row[-1]

#PCA主成分分析
pca = PCA()
pca.fit(guiyihua)
quanzhong = (pca.explained_variance_ratio_)
##得到权重后线性加权
jisuanquanzhong_in = numpy.ones(84)
guiyihua = numpy.c_[guiyihua,jisuanquanzhong_in]
for row in guiyihua:
    row[4] = row[0] * quanzhong[0]+ row[1] * quanzhong[1]+row[2] * quanzhong[2]+row[3] * quanzhong[3]

#填充id
guiyihua = numpy.c_[guiyihua,jisuanquanzhong_in]
for i in range(0,84):
    guiyihua[i][5] = total[i][0]


#print(quanzhong)
numpy.savetxt('outfile.csv', guiyihua, delimiter=',')
db.close()  # 关闭连接