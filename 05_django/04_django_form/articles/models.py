from django.db import models
from django.conf import settings

class Article(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # 객체 표시 형식 
    def __str__(self):
         return f'[{self.pk}번글]: {self.title}|{self.content}'

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE) 
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Model Level에서 메타데이터 옵션 설정 => 정렬 기능 사용
    class Meta:
        ordering = ['-pk',]

    # 객체 표현 방식
    def __str__(self):
        return self.content
