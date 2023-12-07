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
from datetime import datetime

# Create your views here.
@api_view(['GET'])
def SubjectProblemListSortbyTime(request, Sid, loadcnt):
    conn = pymysql.connect(host='database-1.czenntejef9p.ap-northeast-2.rds.amazonaws.com',
                        user='admin', password='admin1234', db='db', charset='utf8')
    curs = conn.cursor()
    loadcnt *= 10
    sql = """
         SELECT PI.PTime, PI.Pno, PI.Plike, PI.Pstate, PI.TryCnt, PI.AcCnt, PI.maker_id, PC.Problem_explain, U.Upoint, U.Uname, S.Sid, S.Sname
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
                "maker_id" : row[6],
                "problem_explain" : row[7],
                "upoint" : row[8],
                "uname" : row[9],
                "sid" : row[10],
                "sname" : row[11],
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
        SELECT PI.PTime, PI.Pno, PI.Plike, PI.Pstate, PI.TryCnt, PI.AcCnt, PI.maker_id, PC.problem_explain, U.Upoint, U.Uname, S.Sid, S.Sname
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
                "maker_id" : row[6],
                "problem_explain" : row[7],
                "upoint" : row[8],
                "uname" : row[9],
                "sid" : row[10],
                "sname" : row[11],
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
        SELECT C.maker_id, C.comm, C.comm_time, U.Uname
        FROM Comments AS C, User_info AS U
        WHERE C.Pno={spno} && C.maker_id=U.id
        ORDER BY C.comm_time DESC
        """.format(spno = str(pno))
    
    curs.execute(sql)
    rows = curs.fetchall()
    conn.close()

    json_data = [
            {   
                'pno' : pno,
                'maker_id' : row[0],
                'comm' : row[1],
                'comm_time' : row[2],
                'uname' : row[3]
            } for row in rows
    ]
    
    return JsonResponse(json_data, safe=False)
    
    
@api_view(['GET'])
def UpdateCnts(request, spno, isAC):
    updateRow = ProblemInfo.objects.get(pno=spno)
    
    updateRow.trycnt += 1
    if(isAC):
        updateRow.accnt += 1
    updateRow.save()
    return Response(status=status.HTTP_201_CREATED)

@api_view(['GET'])
def UpdateLike(request, spno, uid):
    updatePI = ProblemInfo.objects.get(pno=spno)
    updateUser = UserInfo.objects.get(id=uid)

    updatePI.plike += 1
    updateUser.upoint += 1
    updatePI.save()
    updateUser.save()
    return Response(status=status.HTTP_201_CREATED)

@api_view(['GET'])
def UpdatePoint(request, uid, mod):

    updateRow = UserInfo.objects.get(id=uid)

    if(mod == 0):
        updateRow.upoint += 10
    else:
        updateRow.upoint += 1

    updateRow.save()
    return Response(status=status.HTTP_201_CREATED)

@api_view(['GET'])
def payPoint(request, uid):
    updateRow = UserInfo.objects.get(id=uid)

    if(updateRow.upoint > 50):
        updateRow.upoint -= 50
        updateRow.save()
        return Response(status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def getPoint(request, uid):
    updateRow = UserInfo.objects.get(id=uid)
    data = updateRow.upoint
    return JsonResponse(data, safe=False)


@api_view(['GET'])
def UpdatePstate(request, spno):
    updateRow = ProblemInfo.objects.get(pno=spno)

    if(updateRow.pstate):
        updateRow.pstate = False
    else:
        updateRow.pstate = True
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
    dateData = reqData.get('comm_time')
    reqData['comm_time'] = datetime.strptime(dateData, '%Y-%m-%dT%H:%M:%S')

    serializer = CommentsSerializers(data=reqData)

    print(serializer)
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


@api_view(['POST'])
def UserCheck(request):
    input_data = request.data
    uid = input_data.get('id', '')
    upwd = input_data.get('pwd', '')
    try: 
        user = UserInfo.objects.get(id=uid, pwd=upwd)
    except UserInfo.DoesNotExist:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    serializers = UserInfoSerializers(user)
    return JsonResponse(serializers.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def getLastPNum(reques):
    problem = ProblemInfo.objects.order_by('-pno').first()
    pnum = problem.pno + 1
    return Response(pnum)