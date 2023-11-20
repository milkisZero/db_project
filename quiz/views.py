from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Quiz
from .serializers import QuizSerializers
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
<<<<<<< HEAD
    return Response(serializer.data) 


@api_view(['GET'])
def ProblemListSortedbyTime(request, Subject):

    conn = pymysql.connect(host='database-1.czenntejef9p.ap-northeast-2.rds.amazonaws.com', 
                        user='admin', password='admin1234', db='db', charset='utf8')
    curs = conn.cursor()
    # 아직 테이블이 다 안 만들어져서 실행 안됨
    sql = """
    SELECT PI.Pno, PI.Plike, PI.Pstate, PI.Ptime, PC.problem_explain, S.Sid, S.Sname, U.Upoint, U.Uname
    FROM Problem_info As PI, Problem_content, PC, Subjects AS S, User AS U
    WHERE PI.Pno=PC.Pno && PI.Pno=S.Pno && PI.Pmaker=U.id
    ORDER BY PI.Ptime DESC
    """
    curs.execute(sql)

    for i in range(min(curs.rowcount, 10)):
        print(curs.fetchone())
    
    return Response()
=======
    return Response(serializer.data)
>>>>>>> 0ef5e7c (trash)
