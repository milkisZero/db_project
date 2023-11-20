from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Quiz
from .serializers import QuizSerializers
import random

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
def ProblemListSortedbyTime(request, Subject):

    strSql = """
    SELECT PI.Pno, PI.like, PI.Pstate, PI.Ptime, PC.problem_explain, S.Sid, S.Sname, U.Point, U.name
    WHERE Problem_info As PI, Problem_content, PC, Subject AS S, User AS U
    FROM PI.Pno=PC.Pno && PI.Pno=S.Pno && PI.Pmaker=U.id
    """
