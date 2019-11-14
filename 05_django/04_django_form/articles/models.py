from django.db import models
from django.conf import settings

# Article 클래스에서 Hashtag 모델을 사용하기 때문에 Hashtag 클래스를 Article 클래스보다 위에다 작성
class Hashtag(models.Model):
    content = models.TextField(unique=True)

class Article(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # article1.like_users
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles', blank=True)
    # 해시태그가 없어도 작성될수 있게 blank=True
    hashtags = models.ManyToManyField(Hashtag, blank=True)


    # 객체 표시 형식 
    def __str__(self):
         return f'[{self.pk}번글]: {self.title}|{self.content}'

class Comment(models.Model):
    # Comment -> 이중 1:N 관계 (Article, User)
    article = models.ForeignKey(Article, on_delete=models.CASCADE) 
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Model Level에서 메타데이터 옵션 설정 => 정렬 기능 사용
    class Meta:
        ordering = ['-pk',]

    # 객체 표현 방식
    def __str__(self):
        return self.content
