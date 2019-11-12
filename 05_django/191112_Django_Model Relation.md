# Model Relation

## 1.Many to one

```bash
# 05_model_relation 폴더 만들기
$ mkdir 05_model_relation

$ cd 05_model_relation/

$ django-admin startproject config .
# manytoone app 만들기
$ python manage.py startapp manytoone
```

settings.py - 앱등록

```python
# 05_model_relation/config/settings.py

INSTALLED_APPS = [
    'manytoone',
    ...
]
```

manytoone/models.py - 클래스 추가

```python
# manytoone/models.py 

from django.db import models

class User(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.name}'

class Article(models.Model):
    title = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'

class Comment(models.Model):
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.content}'
```



- 현재 User와 Article의 관계는 `User : Article = 1 : N`이다.
  - [참조] `article.user`
  - [역참조] `user.article_set`
- 관점을 조금 바꿔서, `User : Article = M : N`으로 설정하고 다시 생각해보자. 유저와 게시글 관계에서 서로 좋아요를 표현할 수 있다고 생각해보자.
  - User는 여러 개의 게시글에 Like (좋아요)를 할 수 있고,
  - Article은 여러 명의 User로부터 Like (좋아요)를 받을 수 있다.



makemigrations / migrate

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```



- **쿼리 실습**
  
  ```bash
  $ python manage.py shell_plus
  ```
  실습데이터
  ```shell
  user1 = User.objects.create(name='Kim')
  user2 = User.objects.create(name='Lee')
  article1 = Article.objects.create(title='1글', user=user1)
  article2 = Article.objects.create(title='2글', user=user1)
  article3 = Article.objects.create(title='3글', user=user2)
  c1 = Comment.objects.create(content='1글1댓글', user=user1, article=article1)
  c2 = Comment.objects.create(content='1글2댓글', user=user2, article=article1)
  c3 = Comment.objects.create(content='1글3댓글', user=user1, article=article1)
  c4 = Comment.objects.create(content='1글4댓글', user=user2, article=article1)
  c5 = Comment.objects.create(content='2글1댓글', user=user1, article=article2)
  c6 = Comment.objects.create(content='!1글5댓글', user=user2, article=article1)
  c7 = Comment.objects.create(content='!2글2댓글', user=user2, article=article2)
  ```
  
  **ORM이 자동으로 DB에 요청해서 결과를 가져온다.**
  
  - 결과 데이터가 유일한 값 : **get**
  - 결과 데이터가 하나도 없을 수 있는 경우 : **filter**
  
  
  
  문제 풀어보기!!
  
  1. 1번 사람이 작성한 게시글을 다 가져오기
  
     ```powershell
     In [3]: user1.article_set.all()
     Out[3]: <QuerySet [<Article: 1글>, <Article: 2글>]>
     ```
  
  2. 1번 사람이 작성한 모든 게시글에 달린 댓글 가져오기
  
     ```powershell
     In [5]: for article in user1.article_set.all():
        ...:     for comment in article.comment_set.all():
        ...:         print(comment.content)
        ...: 
     1글1댓글
     1글2댓글
     1글3댓글
     1글4댓글
     !1글5댓글
     2글1댓글
     !2글2댓글
     ```
  
  3. 2번 댓글을 작성한 User는? 
  
     ```powershell
     In [6]: c2.user.pk
     Out[6]: 2
     ```
  
  
  4. 2번 댓글을 작성한 User의 이름은?
  
     ```powershell
  In [7]: c2.user.name
Out[7]: 'Lee'
     ```
  
  5. 2번 댓글을 작성한 사람의 모든 게시글은?
  
     ```powershell
     In [8]: c2.user.article_set.all()
     Out[8]: <QuerySet [<Article: 3글>]>
     ```
  
  6. 1번 글의 첫번째 댓글을 작성한 사람의 이름은?
  
     ```powershell
     In [9]: article1.comment_set.first().user.name
     Out[9]: 'Kim'
     ```
  
7. 1번 글의 2번째부터 4번째 까지 댓글 가져오기
  
     ```powershell
     In [10]: article1.comment_set.all()[1:4]
   Out[10]: <QuerySet [<Comment: 1글2댓글>, <Comment: 1글3댓글>, <Comment: 1글4댓글>]>
     
     In [11]: print(article1.comment_set.all()[1:4].query)
   SELECT "manytoone_comment"."id", "manytoone_comment"."content", "manytoone_comment"."article_id", "manytoone_comment"."user_id" FROM "manytoone_comment" WHERE "manytoone_comment"."article_id" = 1  LIMIT 3 OFFSET 1
   ```
  
  8. 1번 글의 첫번째, 두번째 댓글 가져오기
  
     ```powershell
     In [12]: article1.comment_set.all()[0:2]
     Out[12]: <QuerySet [<Comment: 1글1댓글>, <Comment: 1글2댓글>]>
     ```

  9. 1번 글의 두번째 댓글을 작성한 사람의 첫번째 게시물의 작성자의 이름은?
  
     ```powershell
     In [13]: article1.comment_set.all()[1].user.article_set.all()[0].user.name
      Out[13]: 'Lee'
     ```
  
  10. 1번 댓글의 user 정보만 가져오면?
  
      ```powershell
      In [14]: Comment.objects.values('user').get(pk=1)
      Out[14]: {'user': 1}
      ```
  
  11. 2번 사람이 작성한 댓글을 pk 내림차순으로 가져오면?
  
      ```powershell
      In [15]: user2.comment_set.order_by('-pk')
      Out[15]: <QuerySet [<Comment: !2글2댓글>, <Comment: !1글5댓글>, <Comment: 1글4댓글>, <Comment: 1글2댓글>]>
      ```

    ```
      
    ```
12. 제목이 '1글'이라는 게시글을 전부 가져오면?
  
    ```shell
    In [16]: Article.objects.filter(title='1글')
      Out[16]: <QuerySet [<Article: 1글>]>
    ```



## 2. Many to Many

```bash
$ python manage.py startapp manytomany
```

settings.py - 앱등록

```python
# 05_model_relation/config/settings.py

INSTALLED_APPS = [
    ...
    'manytomany',
    ...
]
```

#### 2.1 1:N의 한계

#### 2.2  중개 모델 생성

- 1:N으로만 구현하려니 예약 정보 시스템을 표현하기가 어렵다.
  - 예를 들어 Patient가 다른 Doctor에게 진료를 받고자 할 때, 기존 기록을 지우지 않으려면 새로운 Patient 인스턴스를 생성해야 한다.
- 중개 모델(class Reservation)을 만들어서 Doctor와  Patient를 이어주는 예약 정보를 담아보자.

manytomany/models.py - 클래스 추가

```python
# manytomany/models.py

from django.db import models

class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'

class Patient(models.Model):
    name = models.TextField()
    doctors = models.ManyToManyField(Doctor, through='Reservation')

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'
# 중개모델
class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.doctor.id}의사의 {self.patient.id}번 환자'
```

#### 2.3 through 옵션

- Patient 입장에서 중개 모델을 거쳐서 `reservation_set`형태로 예약 정보를 가져오는 것은 너무 불편하다.
  - 마찬가지로 Doctor도 `reservation_set`형태로 예약 정보를 먼저 불러온 뒤에 Patient의 정보를 꺼내 올 수 있다.
- Doctor 정보를 중개 모델을 거치지 않고, 다이렉트로 가져와보자.

```python
# manytomany/models.py

class Doctor(models.Model):
    name = models.TextField()
    
class Patient(models.Model):
    name = models.TextField()   
    doctors = models.ManyToManyField(Doctor, through='Reservation')
```

#### 2.4 `related_name`

- 이제 Patient의 입장에서는 `patient.doctors.all()`과 같은 형태로 쉽게 Doctor 정보를 가져올 수 있다.
- 마찬가지로 Doctor의 입장에서도 `doctor.patients.all()`과 같은 형태로 Patient의 정보를 가져올 수 있게끔, `related_name`옵션을 사용해 보자.

```python
# manytomany/models.py

class Doctor(models.Model):
    name = models.TextField()

class Patient(models.Model):
    name = models.TextField()
    doctors = models.ManyToManyField(Doctor, through='Reservation', related_name="patients")
```

#### 2.5 Many To Many

- 단순히 Doctor와 Patient를 이어줄 생각이라면 , 굳이 중개모델이 필요 없다. `ManyToManyField`만 사용하면 장고가 자동으로 중개 테이블을 만들어준다.

```python
# manytomany/models.py

class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'

class Patient(models.Model):
    name = models.TextField()
    # doctor = models.ManyToManyField(Doctor, through='Reservation', related_name='patients')
    doctor = models.ManyToManyField(Doctor,related_name='patients')

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'

```

- 중개모델을 만들지 않았지만 DB를 확인해보면 임의의 테이블을 자동으로 생성해준 것을 확인 할 수 있다.

![image-20191112163615635](assets\image-20191112163615635.png)

- **실습**

ex) 1:N ( 의사 : 환자 )

```bash
$ python manage.py shell_plus
```

```shell
In [1]: doctor1 = Doctor.objects.create(name='도현')

In [2]: doctor2 = Doctor.objects.create(name='은애')

In [3]: patient1 = Patient.objects.create(name='민승')

In [4]: patient2 = Patient.objects.create(name='세환')

In [5]: Reservation.objects.create(doctor=doctor1, patient=patient2)
Out[5]: <Reservation: Reservation object (1)>

In [6]: Reservation.objects.create(doctor=doctor2, patient=patient2)
Out[6]: <Reservation: Reservation object (2)>

In [7]: Reservation.objects.get(pk=1)
Out[7]: <Reservation: 1의사의 2번 환자>
```



삭제하기

![image-20191112162411396](assets\image-20191112162411396.png)

마이그레이션에 있는  0001도 삭제

![image-20191112162641969](assets\image-20191112162641969.png)



다시 makemigration, migrate



```bash
$ python manage.py shell_plus
```

```shell
In [1]: Doctor.objects.create(name='은애')
Out[1]: <Doctor: 1번 의사 은애>

In [2]: Doctor.objects.create(name='도현')
Out[2]: <Doctor: 2번 의사 도현>

In [3]: doctor1 = Doctor.objects.get(pk=1)

In [4]: doctor2 = Doctor.objects.get(pk=2)

In [5]: patient1 = Patient.objects.create(name='세환')

In [6]: patient2 = Patient.objects.create(name='민승')

In [7]: doctor1.patients.all()
Out[7]: <QuerySet []>

In [8]: doctor2.patients.all()
Out[8]: <QuerySet []>

In [9]: doctor1.patients.add(patient1)

In [10]: doctor1.patients.all()
Out[10]: <QuerySet [<Patient: 1번 환자 세환>]>

In [11]: doctor1.patients.add(patient2)

In [12]: doctor1.patients.all()
Out[12]: <QuerySet [<Patient: 1번 환자 세환>, <Patient: 2번 환자 민승>]>

In [13]: doctor1.patients.remove(patient1)

In [14]: doctor1.patients.all()
Out[14]: <QuerySet [<Patient: 2번 환자 민승>]>
```

![image-20191112163458597](assets\image-20191112163458597.png)