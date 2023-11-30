from rest_framework import serializers
from .models import *

# 모델의 데이터를 JSON으로 직렬화
class UserInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ('id', 'pwd', 'uname', 'email', 'upoint')

class ProblemInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProblemInfo
        fields = ('ptime', 'pno', 'sub', 'maker', 'plike', 'pstate', 'trycnt', 'accnt')

class ProblemContentSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProblemContent
        fields = ('pno', 'problem_explain', 'answer', 'ans_explain')

class SubjectsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Subjects
        fields = ('sid', 'sname')

class CommentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('pno', 'maker', 'comm', 'comm_time')