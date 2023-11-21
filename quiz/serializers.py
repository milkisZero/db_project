from rest_framework import serializers
from .models import *

# 모델의 데이터를 JSON으로 직렬화
# class QuizSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Quiz
#         fields = ('title', 'body', 'answer')

class UserInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ('title', 'body', 'answer')


class UserInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fileds = ('id', 'pwd', 'uname', 'email', 'upoint')

class ProblemInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProblemInfo
        filed = ('pno', 'sub', 'maker', 'plike', 'pstate', 'ptime')

class ProblemContentSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProblemContent
        filed = ('pno', 'problem_exlain', 'answer', 'ans_explain')

class SubjectsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Subjects
        filed = ('sid', 'sname')

class CommentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comments
        filed = ('pno', 'maker', 'comm', 'comm_time')