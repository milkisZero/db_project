# quiz_app의 url을 관리, myapi의 urls.py은 전체 프로젝트를 관리.
# myapi의 urls.py에 연결

from django.urls import path, include
from .views import *

urlpatterns = [
    path("all/<int:loadcnt>/<int:sortmode>", AllProblemListSortby),
    path("subj/<int:Sid>/<int:loadcnt>/", SubjectProblemListSortbyTime),
    path("detail/<int:pno>/", ProblemDetails),
    path("comm/<int:pno>/", CommentsInfo),
    path("make/pi/", postProblemInfo),
    path("make/pc/", postProblemContent),
    path("make/comm/", postComments),
    path("make/ui/", postUserInfo),
    path("check/ui/", UserCheck),
]