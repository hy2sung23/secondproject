from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    #문자열로 정의되어 있는 형식을 타이틀로 정의하겠다. 길이는 최대 200
    pub_date = models.DateTimeField('date published')
    #날짜와 시간을 나타내는 데이터를 date published를 적어 pub_date로 정의하겠다.
    body = models.TextField()
    #긴 문자 형식을 body로 정의하겠다.
    def __str__(self):
        return self.title