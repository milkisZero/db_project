from django.test import TestCase
import pymysql

conn = pymysql.connect(host='database-1.czenntejef9p.ap-northeast-2.rds.amazonaws.com', 
                        user='admin', password='admin1234', db='db', charset='utf8')
curs = conn.cursor()

sql = """ 
SELECT *
FROM User_info
"""
curs.execute(sql)

rows = curs.fetchall()
print (rows)


conn.close()