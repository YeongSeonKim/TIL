from django.db import models

# Create your models here.
# django.db.models.Model 클래스를 상속받아서 모델을 정의함
class Student(models.Model):
    name = models.TextField()
    age = models.IntegerField()
    email = models.EmailField()
    # auto_now_add=True : 인스턴스 최초 생성 시각
    created_at = models.DateTimeField(auto_now_add=True)
    # auto_now=True : 인스턴스 최종 수정 시각 (업데이트됨)
    updated_at = models.DateTimeField(auto_now=True)

     # 객체를 표시하는 형식 커스터마이징
    def __str__(self):
         return f'[{self.pk}번 학생]: {self.name}|{self.age}|{self.email}'