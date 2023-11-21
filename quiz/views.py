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


@api_view(['GET'])
def ProblemListSortedbyTime(request):

    strSql = """
    SELECT PI.Pno, PI.Plike, PI.Pstate, PI.Ptime, PI.maker_id, PI.Sub_id
    FROM Problem_info As PI
    ORDER BY PI.Ptime DESC
    LIMIT 0,9
    """

    tmp = ProblemInfo.objects.raw(strSql)
    serializers = ProblemInfoSerializers(tmp, many = True)
    return Response(serializers.data)

