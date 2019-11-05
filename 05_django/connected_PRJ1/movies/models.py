from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100) # String 영화명
    title_en = models.CharField(max_length=100) # String 영화명(영문)
    audience = models.IntegerField() # Integer 누적 관객수
    open_date = models.TextField()# Date 개봉일
    genre = models.CharField(max_length=50) # String 장르
    watch_grade = models.CharField(max_length=50) # String 관람등급
    score = models.FloatField() # Float 평점
    poster_url = models.TextField() # Text 포스터 이미지 URL
    description = models.TextField() # Text 영화 소개

    # 객체 표시 형식 수정 
    def __str__(self):
        return f'[{self.pk}번]: {self.title}|{self.score}'

class Comment(models.Model):

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Model Level에서 Metadata 설정
    class Meta:
        ordering = ['-pk',]

    def __str__(self):
        return self.content