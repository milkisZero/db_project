from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
import random
import pymysql

# Create your views here.
@api_view(['GET'])
def helloAPI(request):
    return Response("hello world!")

@api_view(['GET'])
def randomQuiz(request, id):
    totalQuizs = Quiz.objects.all()
    randomQuiz = random.sample(list(totalQuizs), id)
    serializer = QuizSerializers(randomQuiz, many=True)
    return Response(serializer.data) 

# @api_view(['GET'])
# def AllProblemListSortbyTime(request, loadcnt):
#     conn = pymysql.connect(host='database-1.czenntejef9p.ap-northeast-2.rds.amazonaws.com',
#                         user='admin', password='admin1234', db='db', charset='utf8')
#     curs = conn.cursor()
#     sql = """
#         SELECT PI.PTime, PI.Pno, PI.Plike, PI.Pstate, PC.Problem_explain, U.Upoint, U.Uname, S.Sname
#         FROM Problem_info AS PI, Problem_content AS PC, User_info AS U, Subjects AS S
#         WHERE  PI.Sub_id=S.Sid && PI.maker_id=U.id && PI.Pno=PC.Pno
#         ORDER BY PI.Ptime DESC 
#         LIMIT {loadcntstr} """.format(loadcntstr=str(loadcnt) + "," + str(loadcnt+10))
#     curs.execute(sql)
#     rows = curs.fetchall()
#     conn.close()

#     json_data = [
#             {
#                 'ptime' : row[0],
#                 'pno' : row[1],
#                 'plike' : row[2],
#                 'pstate' : row[3],
#                 'upoint' : row[4],
#                 'uname' : row[5],
#                 'sname' : row[6],
#             } for row in rows
#     ]

#     return Response(json_data)

@api_view(['GET'])
def SubjectProblemListSortbyTime(request, Sid, loadcnt):
    conn = pymysql.connect(host='database-1.czenntejef9p.ap-northeast-2.rds.amazonaws.com',
                        user='admin', password='admin1234', db='db', charset='utf8')
    curs = conn.cursor()
    loadcnt *= 10
    sql = """
         SELECT PI.PTime, PI.Pno, PI.Plike, PI.Pstate, PC.Problem_explain, U.Upoint, U.Uname, S.Sid, S.Sname
         FROM Problem_info AS PI, Problem_content AS PC, User_info AS U, Subjects AS S
         WHERE  PI.Sub_id={Sidstr} && PI.maker_id=U.id && PI.Pno=PC.Pno && PI.Sub_id=S.Sid
         ORDER BY PI.Ptime DESC 
         LIMIT {loadcntstr} """.format(Sidstr=str(Sid), loadcntstr=str(loadcnt) + ", 10")
    
    curs.execute(sql)
    rows = curs.fetchall()
    conn.close()

    json_data = [
            {
                'ptime' : row[0],
                'pno' : row[1],
                'plike' : row[2],
                'pstate' : row[3],
                'problem_explain' : row[4],
                'upoint' : row[5],
                'uname' : row[6],
                'sid' : row[7],
                'sname' : row[8],
            } for row in rows
    ]

    return Response(json_data)


@api_view(['GET'])
def AllProblemListSortby(request, loadcnt, sortmode):
    conn = pymysql.connect(host='database-1.czenntejef9p.ap-northeast-2.rds.amazonaws.com',
                        user='admin', password='admin1234', db='db', charset='utf8')
    curs = conn.cursor()
    loadcnt *= 10

    order = ""
    if(sortmode == 0):
        order = "Ptime"
    else:
        order = "Plike"

    sql = """
        SELECT PI.PTime, PI.Pno, PI.Plike, PI.Pstate, PC.problem_explain, U.Upoint, U.Uname, S.Sid, S.Sname
        FROM Problem_info AS PI, Problem_content AS PC, User_info AS U, Subjects AS S
        WHERE  PI.Sub_id=S.Sid && PI.maker_id=U.id && PI.Pno=PC.Pno
        ORDER BY PI.{orderby} DESC 
        LIMIT {loadcntstr} """.format(orderby = order, loadcntstr=str(loadcnt) + ", 10")
    
    curs.execute(sql)
    rows = curs.fetchall()
    conn.close()

    json_data = [
            {
                'ptime' : row[0],
                'pno' : row[1],
                'plike' : row[2],
                'pstate' : row[3],
                'problem_explain' : row[4],
                'upoint' : row[5],
                'uname' : row[6],
                'sid' : row[7],
                'sname' : row[8],
            } for row in rows
    ]

    return Response(json_data)

    # tmp = ProblemPage.objects.raw(sql)
    # serializer = ProblemPageSerializers(tmp, many = True)
    # return Response(serializer.data) 
@api_view(['GET'])
def ProblemDetails(request, pno):
    conn = pymysql.connect(host='database-1.czenntejef9p.ap-northeast-2.rds.amazonaws.com',
                        user='admin', password='admin1234', db='db', charset='utf8')
    curs = conn.cursor()
    
    sql = """
        SELECT answer, ans_explain
        FROM Problem_content
        WHERE Pno={p}
    """.format(p=str(pno))

    curs.execute(sql)
    rows = curs.fetchall()
    conn.close()

    json_data = [
            {
                'answer' : row[0],
                'ans_explain' : row[1]
            } for row in rows
    ]

    return Response(json_data)

@api_view(['GET'])
def CommentsInfo(request, pno):
    conn = pymysql.connect(host='database-1.czenntejef9p.ap-northeast-2.rds.amazonaws.com',
                        user='admin', password='admin1234', db='db', charset='utf8')
    curs = conn.cursor()
    
    sql = """
        SELECT maker_id, comm, comm_time
        FROM Comments
        WHERE Pno={spno}
        ORDER BY comm_time DESC
        """.format(spno = str(pno))
    
    curs.execute(sql)
    rows = curs.fetchall()
    conn.close()

    json_data = [
            {
                'maker_id' : row[0],
                'comm' : row[1],
                'comm_time' : row[2],
            } for row in rows
    ]

    return Response(json_data)
