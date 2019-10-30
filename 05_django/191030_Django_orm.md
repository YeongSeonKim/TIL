### 2019-10-30

# Database - Django Model (ORM)

-  ORM 이용하여 데이터 엑세스 

```bash
# 05_django
$ source ~/venv/Scripts/activate

$ cd 02_django_orm_crud/

# 05_django/02_django_orm_crud
$ django-admin startproject config .

$ python manage.py startapp articles

$ python manage.py makemigrations
```



## 1. Model

- 장고 MTV 패턴
  - Model
    - 특정한 데이터 구조(모양)에 대한 정보를 가지고 있다.
    - 하나의모델 클래스는 실제 DB에는 하나의 테이블로 매핑된다.
    - 컬럼에 대한 정보, 해당 데이터에 대한 정보를 정의하는 곳
  - Template
  - View
- **Model 로직**
  - 데이터베이스 컬럼(열)과 어떠한 타입으로 정의할 것인지에 대한 정보를 `django.db.models` 라는 곳에서 상속받아서 정의한다.
  - 모든 필드들은 `NOT NULL` 조건이 붙는다.
  - 각각의 클래스 변수는 데이터베이스 필드를 나타낸다.
- 실습

```python
# models.py

from django.db import models

# django.db.models.Model 클래스를 상속받아서 모델을 정의함
class Article(models.Model):
    # id(PK)는 인스턴스 생성과 함께 자동으로 부여된다

    # CharField에서 max_length는 필수인자
    # 장고 내부에서 데이터 유효성 검증을 할 때 사용
    title = models.CharField(max_length=30)
    # 긴 문자열은 TextField 사용
    context = models.TextField()
    # auto_now_add=True : 인스턴스 최초 생성 시각
    created_at = models.DateTimeField(auto_now_add=True)
    # auto_now=True : 인스턴스 최종 수정 시각 (업데이트됨)
    # updated_at = models.DateTimeField(auto_now=True)
```

![image](https://user-images.githubusercontent.com/50851249/67823102-23783700-fb05-11e9-8a44-105a128c74e0.png)

- makemigrations
  - 실제 데이터베이스 테이블을 만들기 전에 설계도를 그려보는 작업
  - migrations 폴더에서 확인해볼수 있다. (0001_initial.py...)
- 마이그레이션 파일 생성

```bash
# 05_django/02_django_orm_crud (master)
$ python manage.py makemigrations

#실행 결과
Migrations for 'articles':
  articles\migrations\0001_initial.py
    - Create model Article
(venv)
```

- sqlmigrate
  - 데이터베이스에 실제로 반영하기 전에 SQL문으로 바뀐 모습을 확인

```bash
# 05_django/02_django_orm_crud 
$ python manage.py sqlmigrate articles 0001
```

![image](https://user-images.githubusercontent.com/50851249/67821278-c75ee400-faff-11e9-98ac-d7467986c093.png)

- showmigrations
  - migration 설계도를 작성했는데, 이설계도가 실제 DB에 반영되었는지 **확인**

```bash
# 05_django/02_django_orm_crud 위치에서
$ python manage.py showmigrations
```

![image](https://user-images.githubusercontent.com/50851249/67820922-82867d80-fafe-11e9-8eb2-2134c3345ace.png)

![image](https://user-images.githubusercontent.com/50851249/67822381-8b2d8280-fb03-11e9-897d-a1092a9b253f.png)

![image](https://user-images.githubusercontent.com/50851249/67822401-9b456200-fb03-11e9-98b6-329069d03fda.png)

- migrate
  - makemigrations로 만든 설계도를 실제 데이터베이스(sqlite3)에 **반영**한다.
  - 모델의 변경사항과

```bash
# 05_django/02_django_orm_crud 위치에서
$ python manage.py migrate
```

![image](https://user-images.githubusercontent.com/50851249/67820942-9c27c500-fafe-11e9-9c3e-ba107dab09cb.png)

- sqlite 실행

```bash
$ sqlite db.sqlite3 # 안되서 밑에 그림으로 실행
```

![image](https://user-images.githubusercontent.com/50851249/67820978-b95c9380-fafe-11e9-8bba-c5fa3d43d039.png)

`ctrl + shift + p`

![image](https://user-images.githubusercontent.com/50851249/67821065-148e8600-faff-11e9-901d-22bc7eb348c0.png)

![image](https://user-images.githubusercontent.com/50851249/67821074-1c4e2a80-faff-11e9-913a-ff040f2a936d.png)

![image](https://user-images.githubusercontent.com/50851249/67821095-23753880-faff-11e9-875e-adee7722ee23.png)



## 2. ORM - CRUD

> 앞으로 데이터베이스에 `SQL 쿼리문`을 날려서 데이터를 조작하는 것이 아니라 `ORM`을 통해 **클래스의 인스턴스 객체로 데이터베이스를 조작**한다.

- 확장 툴 설치하기

```bash
# ipython 설치 05_django/02_django_orm_crud

$ pip install ipython

# shell 진입 확인
$ python manage.py shell

# shell 나가기
$ exit()
```

![image](https://user-images.githubusercontent.com/50851249/67821228-99799f80-faff-11e9-8fd0-509bd21f9ab2.png)

![image](https://user-images.githubusercontent.com/50851249/67821396-2ae91180-fb00-11e9-86c5-3cbdc0cd2073.png)

```sqlite
In []: from articles.models import Article

# 저장된 객체 확인
In []: Article.objects.all()
Out[]: <QuerySet []>

In []: article = Article()

In []: article
Out[]: <Article: Article object (None)>
```

- ORM 이 리턴되는 형식
  - QuerySet : 다수의 객체가 담김(파이썬 리스트 다루는 것과 비슷)
  - Query : 단일객체
- `모델명.object.명령`
  - objects : 모델 클래스 정보를 토대로 실제 데이터베이스에 쿼리(SQL)를 날려서 데이터 베이스와 의사소통하는 통역사(매니저) 역할
  - = 중간에서 자동으로 데이터베이스에 쿼리문을 자동으로 날려줌
- **우리가 ORM을 사용하는 이유?**
  - SQL문에 종속되지 않고 데이터를 객체 형태로 다루기 위해(프로그래밍 언어만 알아도 DB를 다룰 수 있음!!)



### 2.1 Create

```sqlite
# 첫번째 방법
In []: article = Article() #객체생성
In []: article
Out[]: <Article: Article object (None)>

# 저장방법
In []: article.title = 'title'

In []: article.content = 'django'

In []: article.title
Out[]: 'first'

In []: article.content
Out[]: 'django'

# 저장된 객체 확인
In []: Article.objects.all()
Out[]: <QuerySet []>

In []: article.save() # db에 저장

In []: article
Out[]: <Article: Article object (1)>

In []: Article.objects.all()
Out[]: <QuerySet [<Article: Article object (1)>]>

# 두번째 방법 : 함수에서 키워드 인자 넘겨주는 방식

In []: article = Article(title='second', content='django')

In []: article.save()

In []: Article.objects.all()
Out[]: <QuerySet [<Article: Article object (1)>, <Article: Article object (2)>]>


# 세번째 방법 : 쿼리셋 객체 

In []: Article.objects.create(title='third', content='django')
Out[]: <Article: Article object (3)>
```


```sqlite
# 유효성 검증

In []: article.full_clean()
```



**객체를 표시하는 형식 커스터마이징**

- models.py 수정

```python
from django.db import models

# django.db.models.Model 클래스를 상속받아서 모델을 정의함
class Article(models.Model):
    ...
    # auto_now=True : 인스턴스 최종 수정 시각 (업데이트됨)
    updated_at = models.DateTimeField(auto_now=True)

    # 객체를 표시하는 형식 커스터마이징
    def __str__(self):
         return f'[{self.pk}번글]: {self.title}|{self.content}'
```

- 수정을 한 후 shell을 종료 한 뒤 shell 재실행

```sqlite
In []: exit()

$ python manage.py shell
```


```sqlite
In []: from articles.models import Article

# 저장된 객체 확인 , 커스터마이징한 형식으로 출력 
In []: Article.objects.all()
Out[]: <QuerySet [<Article: [1번글]: first|django>, <Article: [2번글]: second|django>, <Article: [3번글]:
third|django>]>
```



### 2.2 Read

- filter()는 `QuerySet`으로 리턴된다.
- first()는 `Article` 형식으로 리턴된다.
- get() 데이터가 없으면 에러를 리턴된다.

```sqlite
# (파이썬 리스트와 비슷한) QuerySet 리턴
In []: articles = Article.objects.all()

# 저장된 객체 확인
In []: Article.objects.all()
Out[]: <QuerySet [<Article: [1번글]: first|django>, <Article: [2번글]: second|django>, <Article: [3번글]:
third|django>]>

# filter() 함수
In []: articles = Article.objects.filter(title='first')
In []: articles
Out[]: <QuerySet [<Article: [1번글]: first|django>]>

# first()함수
In []: articles = Article.objects.filter(title='first').first()
In []: articles
Out[]: <Article: [1번글]: first|django>

# get()함수
In []: articles = Article.objects.filter(title='first').get()
In []: articles
Out[]: <Article: [1번글]: first|django>

# 정렬-내림차순
In []: articles = Article.objects.order_by('-pk')

In []: articles
Out[]: <QuerySet [<Article: [3번글]: third|django>, <Article: [2번글]: second|django>, <Article: [1번글]: first|django>]>

In []: articles = Article.objects.all()[1:3]

In []: articles
Out[]: <QuerySet [<Article: [2번글]: second|django>, <Article: [3번글]: third|django>]>

# type 데이터 타입확인
In []: type(articles)
Out[]: django.db.models.query.QuerySet

# fir 문자가 포함된 데이터 검색
In []: article = Article.objects.filter(title__contains='fir')
In []: article
Out[]: <QuerySet [<Article: [1번글]: first|django>]>

# fir 문자로 시작하는 데이터 검색
In []: article = Article.objects.filter(title__startswith='fir')
In []: article
Out[]: <QuerySet [<Article: [1번글]: first|django>]>

# d 문자로 끝나는 데이터 검색
In []: article = Article.objects.filter(title__endswith='d')
In []: article
Out[]: <QuerySet [<Article: [2번글]: second|django>, <Article: [3번글]: third|django>]>
```



### 2.3 Update

```sqlite
# 1. 수정할 인스턴스 가져오기
In []: article = Article.objects.get(pk=3)

# 2. 인스턴스 값 수정하기
In []: article.title = 'hello'

# 3. 인스턴스 저장하기 
In []: article.save()
```



### 2.4 Delete

```sqlite
In []: article = Article.objects.get(pk=2)

In []: article.delete()
Out[]: (1, {'articles.Article': 1})
```

![image](https://user-images.githubusercontent.com/50851249/67826785-0f3a3700-fb11-11e9-82ba-14f674043c78.png)



### Django 관리자 페이지 커스터마이징

- 관리자페이지 계정생성 

```sqlite
# admin 추가 

$ python manage.py createsuperuser
사용자 이름 (leave blank to use 'student'): admin
이메일 주소:
Password:
Password (again):
비밀번호가 사용자 이름와 너무 유사합니다.
비밀번호가 너무 짧습니다. 최소 8 문자를 포함해야 합니다.
비밀번호가 너무 일상적인 단어입니다.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
(venv)
```
- http://127.0.0.1:8000/admin/ 접속하여 생성한 계정으로 로그인

```python
# admin.py

from django.contrib import admin

admin.site.register(Article)
```

![image](https://user-images.githubusercontent.com/50851249/67833573-5e3f9680-fb28-11e9-83c6-15337a270f50.png)

- admin.py 수정

```python
# admin.py

from .models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk','title','content','created_at','updated_at')
    list_display_links = ('content',) # 링크설정
    list_filter = ('created_at',)
    list_editable = ('title',)
    list_per_page = 2

admin.site.register(Article, ArticleAdmin)
```



### 2.5 Django - Extensions

> 기본 Django Shell은 직접 모델을 import 해주어야 하는 불편함이 있었지만 , `shell_plus`는 **필요한 모델을 자동으로 import 해주기 떄문에 편리**하다.

- 확장 툴 설치하기

```bash
# django-extensions 설치 05_django/02_django_orm_crud

$ pip install django-extensions
```

- 앱 등록하기
```python
# settings. py

INSTALLED_APPS = [
    ...
    # Third party apps
    'django_extensions',
    ...
]
```

- Shell 실행하기
```bash
# shell 실행하기 

$ python manage.py shell_plus
```

![image](https://user-images.githubusercontent.com/50851249/67830990-20d70b00-fb20-11e9-8ffe-8432528747cf.png)



