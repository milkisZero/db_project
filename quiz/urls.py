# quiz_app의 url을 관리, myapi의 urls.py은 전체 프로젝트를 관리.
# myapi의 urls.py에 연결

from django.urls import path, include
from .views import helloAPI, randomQuiz

urlpatterns = [
    path("hello/", helloAPI),
    path("<int:id>/", randomQuiz),
]