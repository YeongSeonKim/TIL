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

   

#### **User - Article**

models.py - Article에 user 추가해주기

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

views.py - create 코드 수정

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





#### **User - Comment**

