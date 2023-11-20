from django.db import models

# Create your models here.
class Quiz(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    answer = models.IntegerField()


class User_info(models.Model):
    id = models.CharField(max_length=30)
    pwd = models.CharField(max_length=30)
    Upoint = models.IntegerField()
    Uname = models.CharField(max_length=30)
    email = models.CharField(max_length=30)

