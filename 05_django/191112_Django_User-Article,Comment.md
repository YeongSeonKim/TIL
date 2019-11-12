# User - Article & Comment

- **User 클래스 가져오는 법**

- `settings.AUTH_USER_MODEL`
- return str
 - models.py 에서 모델 정의할 때만 사용

 ```python
 # models.py
 
 from django.conf import settings
 settings.AUTH_USER_MODEL
 ```

- `get_user_model()`

   - return class 형태로 리턴됨
   - models.py 제외한 모든 곳에 사용

   ```python
   # models.py
   
   from django.contrib.auth import get_user_model 
   get_user_model()
   ```

   

## 1. User - Article

#### 1.1  Article 모델 클래스 수정 - user 추가해주기

```python
# models.py

from django.conf import settings

class Article(models.Model):
    ...
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
```

makemigrations

```bash
$ python manage.py makemigrations
You are trying to add a non-nullable field 'user' to article without a default; we can't do that (the database needs something to populate existing rows).
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit, and let me add a default in models.py
Select an option: 1
Please enter the default value now, as valid Python
The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now
Type 'exit' to exit this prompt
>>> 2
Migrations for 'articles':
  articles\migrations\0004_article_user.py
    - Add field user to article
(venv)
```
migrate
```bash
$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, articles, auth, contenttypes, sessions
Running migrations:
  Applying articles.0004_article_user... OK
(venv)
```

![image-20191112102833828](assets/image-20191112102833828.png)

#### 1.2 views.py - create 코드 수정

```python
# articles/views.py

@login_required # 데코레이트 지정
def create(request):
    
    ...
            article = form.save(commit=False)
            article.user = request.user
            article.save()
    ...
```

index.html - 사용자 추가 해주기

```django
<!-- index.html  -->

...
  {% for article in articles %}
  <p> 작성자 : {{ article.user }} </p>
...
```

![image-20191112100245459](assets/image-20191112100245459.png)



#### 1.3 views.py - Update, Delete 코드 수정

detail.html 코드수정

```django
<!-- detail.html -->
```

views.py 코드 수정 (update)

```python
# articles/views.py

@login_required
def update(request, article_pk):
    article = get_object_or_404(Article,pk=article_pk)
    # 지금 로그인한 사용자와 게시글 작성자 비교
    if request.user == article.user:
        ...
```

views.py 코드 수정 (delete)

```python
# articles/views.py

@require_POST
def delete(request, article_pk):
    # 지금 사용자가 로그인 되어 있는지?
    if request.user.is_authenticated:
        # 삭제할 게시글 가져오기
        article = get_object_or_404(Article,pk=article_pk)
        # 지금 로그인한 사용자와 게시글 작성자 비교
        if request.user == article.user:
            article.delete()    
        else:
            return redirect('articles:detail', article.pk)
    return redirect('articles:index')
```



## 2. User - Comment

#### 2.1 Comment 모델 클래스 코드수정 - user 추가해주기

```python
# articles/models.py

class Comment(models.Model):
    # Comment -> 이중 1:N 관계 (Article, User)
    ...
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ...
```

- 데이터 베이스에 반영
  - vvv



makemigrations

```bash
$ python manage.py makemigrations
You are trying to add a non-nullable field 'user' to comment without a default; we can't do that (the database needs something to populate existing rows).
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit, and let me add a default in models.py
Select an option: 1
Please enter the default value now, as valid Python
The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now
Type 'exit' to exit this prompt
>>> 2
Migrations for 'articles':
  articles\migrations\0005_comment_user.py
    - Add field user to comment
(venv)
```

migrate

```bash
$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, articles, auth, contenttypes, sessions
Running migrations:
  Applying articles.0005_comment_user... OK
(venv)
```

![image-20191112102911333](assets/image-20191112102911333.png)



#### 2.2 views.py  - comments_create 코드수정

```python
# articles/views.py

@require_POST
def comments_create(request, article_pk):
    # article = get_object_or_404(Article,pk=article_pk)
    if request.user.is_authenticated:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            # save 메서드 -> 선택 인자 : (기본값) commit=True -> DB에 저장
            # DB에 바로 저장되는 것을 막아준다. -> commit=False
            comment = comment_form.save(commit=False) 
            comment.user = request.user
            comment.article_id = article_pk # 장고가 만들어준 테이블 형식으로 불러오기
            comment.save()
        return redirect('articles:detail', article_pk)
```

detail.html 코드 수정 - 댓글 입력하는 폼에 if 문 추가 해주기

```django
<!-- detail.html -->

{% if user.is_authenticated %}
<!-- 댓글 입력하는 Form -->
  <form action="{% url 'articles:comments_create' article.pk %}" method="POST">
  {% csrf_token %}
  {% comment %} {{ comment_form }} {% endcomment %}
  {% bootstrap_form comment_form layout='inline' %}

  <div class="text-center">
      {% buttons submit='댓글입력' reset="초기화" %}
      {% endbuttons %}
  </div>
  </form>
{% else %}
  <a href="{% url 'accounts:login' %}">[댓글을 작성하려면 로그인 해주세요!]</a>
{% endif %}
```

로그아웃 했을 때 댓글에 삭제 보여주지 않기

![image-20191112110230721](assets/image-20191112110230721.png)

#### 2.3 views.py  - comments_delete 코드수정

```python
# articles/views.py


@require_POST
def comments_delete(request, article_pk, comment_pk):
    # 1. 로그인 여부 확인
    if request.user.is_authenticated:
        comment = Comment.objects.get(pk=comment_pk)
        # 2. 로그인한 사용자와 댓글 작성자가 같을 경우
        if request.user == comment.user:
            comment.delete()
    return redirect('articles:detail', article_pk)
```

detail.html 코드 수정 - 댓글 작성하는 사용자와 로그인한 사용자가 같은지 if문 추가해주기

```django
<!-- detail.html  -->

{% for comment in comments %}
...
{% if comment.user == request.user %}
  <form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST">
    {% csrf_token %}
  <div>
      {% buttons submit='댓글삭제' %}
      {% endbuttons %}
  </div>
  </form>
{% endif %}
<hr>
{% endfor %}
```

로그인 했을 때 댓글에 삭제 보여주기

![image-20191112110343409](assets/image-20191112110343409-1573524231718.png)



## [Movies 프로젝트 추가 개발]

#### - Authentication : 회원가입, 로그인, 로그아웃

#### - 댓글(User 정보 포함) 기능

