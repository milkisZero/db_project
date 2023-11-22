from rest_framework import serializers
from .models import *

# 모델의 데이터를 JSON으로 직렬화
class QuizSerializers(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ('title', 'body', 'answer')


class UserInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ('id', 'pwd', 'uname', 'email', 'upoint')

class ProblemInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProblemInfo
        fields = ('ptime', 'pno', 'sub', 'maker', 'plike', 'pstate')

class ProblemContentSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProblemContent
        fields = ('pno', 'problem_exlain', 'answer', 'ans_explain')

class SubjectsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Subjects
        fields = ('sid', 'sname')

class CommentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('pno', 'maker', 'comm', 'comm_time')

# class ProblemPageSerializers(serializers.Serializer):
#      class Meta:
#         model = ProblemPage
#         fields = ( 'ptime', 'pno', 'plike', 'pstate', 'problem_exlain' ,'upoint', 'maker', 'sub')

