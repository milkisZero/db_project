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

# @api_view(['GET'])
# def SubjectProblemListSortbyTime(request, Sid, loadcnt):

#     sql = """
#         SELECT PI.PTime, PI.Pno, PI.Plike, PI.Pstate, PC.Problem_explain, U.Upoint, U.Uname, S.Sname
#         FROM Problem_info AS PI, Problem_content AS PC, User_info AS U, Subjects AS S
#         WHERE  PI.Sub_id={Sidstr} && PI.maker_id=U.id && PI.Pno=PC.Pno
#         ORDER BY PI.Ptime DESC 
#         LIMIT {loadcntstr} """.format(Sidstr=str(Sid), loadcntstr=str(loadcnt) + "," + str(loadcnt+10))
    
#     tmp = ProblemPage.objects.raw(sql)
#     serializer = ProblemPageSerializers(tmp, many = True)
#     return Response(serializer.data)


@api_view(['GET'])
def AllProblemListSortbyTime(request, loadcnt):
    conn = pymysql.connect(host='database-1.czenntejef9p.ap-northeast-2.rds.amazonaws.com',
                        user='admin', password='admin1234', db='db', charset='utf8')
    curs = conn.cursor()
    sql = """
        SELECT PI.PTime, PI.Pno, PI.Plike, PI.Pstate, U.Upoint, U.Uname, S.Sname
        FROM Problem_info AS PI, User_info AS U, Subjects AS S
        WHERE  PI.Sub_id=S.Sid && PI.maker_id=U.id 
        ORDER BY PI.Ptime DESC 
        LIMIT {loadcntstr} """.format(loadcntstr=str(loadcnt) + "," + str(loadcnt+10))
    curs.execute(sql)
    rows = curs.fetchall()
    conn.close()

    json_data = [
            {
                'ptime' : row[0],
                'pno' : row[1],
                'plike' : row[2],
                'pstate' : row[3],
                'upoint' : row[4],
                'uname' : row[5],
                'sname' : row[6],
            } for row in rows
    ]

    return Response(json_data)

    # tmp = ProblemPage.objects.raw(sql)
    # serializer = ProblemPageSerializers(tmp, many = True)
    # return Response(serializer.data) 
