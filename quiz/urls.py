# quiz_app의 url을 관리, myapi의 urls.py은 전체 프로젝트를 관리.
# myapi의 urls.py에 연결

from django.urls import path, include
from .views import *

urlpatterns = [
    path("all/<int:loadcnt>/<int:sortmode>", AllProblemListSortby),
    path("subj/<int:Sid>/<int:loadcnt>/", SubjectProblemListSortbyTime),
    path("detail/<int:pno>/", ProblemDetails),
    path("comm/<int:pno>/", CommentsInfo),
    path("update/cnt/<int:spno>/<int:isAC>/", UpdateCnts),
    path("update/like/<int:spno>/<str:uid>/", UpdateLike),
    path("update/point/<str:uid>/<int:mod>/", UpdatePoint),
    path("update/pstate/<int:spno>/", UpdatePstate),
    path("make/pi/", postProblemInfo),
    path("make/pc/", postProblemContent),
    path("make/comm/", postComments),
    path("make/ui/", postUserInfo),
    path("check/user/", UserCheck),
    path("get/pnum/", getLastPNum),
    path("pay/point/<str:uid>/", payPoint),
    path("get/point/<str:uid>/", getPoint),
]