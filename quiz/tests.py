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
Sid = 1
loadcnt = 0

sql = """
        SELECT PI.PTime, PI.Pno, PI.Plike, PI.Pstate
        FROM Problem_info AS PI, Subjects AS S
        WHERE  PI.Sub_id={Sidstr}
        ORDER BY PI.Ptime DESC 
        LIMIT {loadcntstr}""".format(Sidstr=str(Sid), loadcntstr=(str(loadcnt) + "," + str(loadcnt+10)))

sql = """
        SELECT *
        FROM Problem_info
        ORDER BY Ptime DESC
"""
curs.execute(sql)

print(curs.fetchall())

#for i in range(curs.rowcount):
    #rows = curs.fetchone()
   # print(rows)

#rows = curs.fetchall()
#print (rows)

conn.close()
