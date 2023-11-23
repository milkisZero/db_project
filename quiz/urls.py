# quiz_app의 url을 관리, myapi의 urls.py은 전체 프로젝트를 관리.
# myapi의 urls.py에 연결

from django.urls import path, include
from .views import *

urlpatterns = [
    path("hello/", helloAPI),
    #path("<int:id>/", randomQuiz),
    path("all/<int:loadcnt>/<int:sortmode>", AllProblemListSortby),
    path("subj/<int:Sid>/<int:loadcnt>/", SubjectProblemListSortbyTime),
    path("detail/<int:pno>/", ProblemDetails),
    path("comm/<int:pno>/", CommentsInfo),
    path("make/pi/", MakeProblemInfo.as_view(), name = "makepi"),
    path("make/pc/", MakeProblemContent.as_view(), name = "makepc"),
    path("make/comm/", MakeComment.as_view()),
    path("test/", PostTest.as_view())
]