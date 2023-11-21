from django.test import TestCase
import pymysql

conn = pymysql.connect(host='database-1.czenntejef9p.ap-northeast-2.rds.amazonaws.com', 
                        user='admin', password='admin1234', db='db', charset='utf8')
curs = conn.cursor()

curs.execute(sql)

for i in range(curs.rowcount):
    print(curs.fetchone())

#rows = curs.fetchall()
#print (rows)

conn.close()
