from django.test import TestCase
import pymysql

conn = pymysql.connect(host='database-1.czenntejef9p.ap-northeast-2.rds.amazonaws.com', 
                        user='admin', password='admin1234', db='db', charset='utf8')
curs = conn.cursor()
sql = """ 
SELECT U.id, P.PTime
FROM User_info AS U, Problem_info AS P
WHERE U.id = P.maker_id
"""
Sid = 7
loadcnt = 4

sql = """
    SELECT PI.PTime, PI.Pno, PI.Plike, PI.Pstate, U.Upoint, U.Uname 
    FROM Problem_info AS PI, User_info AS U
     WHERE  PI.Sub_id=""" + str(Sid) + """ && PI.maker_id=U.id
    ORDER BY PI.Ptime DESC
    LIMIT """ + str(loadcnt)

curs.execute(sql)

for i in range(curs.rowcount):
    rows = curs.fetchone()
    print(rows)

#rows = curs.fetchall()
#print (rows)
conn.close()
