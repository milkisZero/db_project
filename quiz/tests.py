from django.test import TestCase
import pymysql

conn = pymysql.connect(host='database-1.czenntejef9p.ap-northeast-2.rds.amazonaws.com', 
                        user='admin', password='admin1234', db='db', charset='utf8')
curs = conn.cursor()

sql = """
    SELECT PI.PTime, PI.Pno, PI.Plike, PI.Pstate, S.Sid, S.Sname, U.Upoint, U.Uname 
    FROM Problem_info AS PI, Subjects AS S, User_info AS U
     WHERE  PI.Sub_id=S.Sid && PI.maker_id=U.id
    ORDER BY PI.Ptime DESC
"""
curs.execute(sql)

rows = curs.fetchall()
print (rows)


conn.close()