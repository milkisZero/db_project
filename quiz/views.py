from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view, parser_classes
from django.http import JsonResponse
from django.views import View
from .models import *
from .serializers import *
import random
import pymysql
import json

# Create your views here.
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
                "ptime" : row[0],
                "pno" : row[1],
                "plike" : row[2],
                "pstate" : row[3],
                "trycnt" : row[4],
                "accnt" : row[5],
                "problem_explain" : row[6],
                "upoint" : row[7],
                "uname" : row[8],
                "sid" : row[9],
                "sname" : row[10],
            } for row in rows
    ]

    return JsonResponse(json_data, safe=False)


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
        SELECT PI.PTime, PI.Pno, PI.Plike, PI.Pstate, PI.TryCnt, PI.AcCnt, PC.problem_explain, U.Upoint, U.Uname, S.Sid, S.Sname
        FROM Problem_info AS PI, Problem_content AS PC, User_info AS U, Subjects AS S
        WHERE  PI.Sub_id=S.Sid && PI.maker_id=U.id && PI.Pno=PC.Pno
        ORDER BY PI.{orderby} DESC 
        LIMIT {loadcntstr} """.format(orderby = order, loadcntstr=str(loadcnt) + ", 10")
    
    
    curs.execute(sql)
    rows = curs.fetchall()
    conn.close()

    json_data = [
            {
                "ptime" : row[0],
                "pno" : row[1],
                "plike" : row[2],
                "pstate" : row[3],
                "trycnt" : row[4],
                "accnt" : row[5],
                "problem_explain" : row[6],
                "upoint" : row[7],
                "uname" : row[8],
                "sid" : row[9],
                "sname" : row[10],
            } for row in rows
    ]

  
    return JsonResponse(json_data, safe=False)


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

    return JsonResponse(json_data, safe=False)


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
    
    return JsonResponse(json_data, safe=False)

@api_view(['GET'])
def UserCheck(request):
    print(request)
    conn = pymysql.connect(host='database-1.czenntejef9p.ap-northeast-2.rds.amazonaws.com',
                        user='admin', password='admin1234', db='db', charset='utf8')
    print(0)
    curs = conn.cursor()
    pwd = """SELECT pwd    FROM User_info    WHERE id={sid}""".format(sid = str(request.id))
    print(1)
    if (pwd == request.pwd):
        print(2)
        sql = """SELECT *    FROM User_info    WHERE id={sid}""".format(sid = str(request.id))
        serializers = UserInfoSerializers(data=sql.data)
        conn.close()
        return JsonResponser(serializers, safe=False)
    else:
        print(3)
        conn.close()
        return Response(status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def UpdateCnts(request, spno, isAC):
    updateRow = ProblemInfo.objects.get(pno=spno)
    
    updateRow.trycnt += 1
    if(isAC):
        updateRow.accnt += 1
    updateRow.save()
    return Response(status=status.HTTP_201_CREATED)

@api_view(['POST'])
@parser_classes([JSONParser])
def postProblemInfo(request):
    reqData = request.data
    serializer = ProblemInfoSerializers(data=reqData)
    if serializer.is_valid():    
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@parser_classes([JSONParser])
def postProblemContent(request):
    reqData = request.data
    serializer = ProblemContentSerializers(data=reqData)
    if serializer.is_valid():    
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@parser_classes([JSONParser])
def postComments(request):
    reqData = request.data
    serializer = CommentsSerializers(data=reqData)
    if serializer.is_valid():    
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@parser_classes([JSONParser])
def postUserInfo(request):  
    serializer = UserInfoSerializers(data=request.data)
    if serializer.is_valid():    
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)