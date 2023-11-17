from rest_framework import serializers
from .models import Quiz

# 모델의 데이터를 JSON으로 직렬화
class QuizSerializers(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ('title', 'body', 'answer')