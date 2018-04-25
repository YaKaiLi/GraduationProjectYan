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
shanchuwuguan = numpy.delete(shanchuwuguan, -1, axis=1)

#for ceshi in shanchuwuguan:
#    print(ceshi)
#exit(0)
#进行插值
#imp = preprocessing.Imputer(missing_values='NaN', strategy='mean', axis=0)
#imp.fit(shanchuwuguan)
#chazhijieguo = imp.transform(shanchuwuguan)

#数据标准化
biaozhunhua = preprocessing.scale(shanchuwuguan)
#数据归一化
min_max_scale = preprocessing.MinMaxScaler()
guiyihua = min_max_scale.fit_transform(biaozhunhua)
#数据同趋化
#for row in guiyihua:
#    row[0] = 1-row[0]
#    row[-1] = 1-row[-1]

#PCA主成分分析
pca = PCA()
pca.fit(guiyihua)
quanzhong = (pca.explained_variance_ratio_)
##得到权重后线性加权
jisuanquanzhong_in = numpy.ones(guiyihua.shape[0])
guiyihua = numpy.c_[guiyihua,jisuanquanzhong_in]
for row in guiyihua:
    #print(row)
    row[8] = row[0] * quanzhong[0]+ row[1] * quanzhong[1]+row[2] * quanzhong[2]+row[3] * quanzhong[3]+row[4] * quanzhong[4]+row[5] * quanzhong[5]+row[6] * quanzhong[6]+row[7] * quanzhong[7]

#填充id
guiyihua = numpy.c_[guiyihua,jisuanquanzhong_in]
for i in range(0,guiyihua.shape[0]):
    guiyihua[i][9] = total[i][0]


#numpy.savetxt('outfile.csv', guiyihua, delimiter=',')
#for x in guiyihua:
#    print(x)
for i in range(0,guiyihua.shape[0]):
    sql_update = "update list_of_journal set yingxiangyinzi = "+str(guiyihua[i][0])+",sousuozhishu = "+str(guiyihua[i][1])+",fawenliang = "+str(guiyihua[i][2])+",beiyinliang = "+str(guiyihua[i][3])+",citationsperdocument = "+str(guiyihua[i][4])+",selfcites = "+str(guiyihua[i][5])+",externalcitesperdoc = "+str(guiyihua[i][6])+",citesperdoc = "+str(guiyihua[i][7])+",value = "+str(guiyihua[i][8])+" where id = "+str(guiyihua[i][9])
    cur.execute(sql_update)  # 像sql语句传递参数
    db.commit()

db.close()  # 关闭连接