

### 2019-10-30

# Django CRUD 구현

## 0. 사전작업

#### 0.1 프로젝트 생성

```bash
# 가상환경 진입
# 05_django
$ source ~/venv/Scripts/activate

$ cd 03_django_crud/

# 05_django/03_django_crud/
$ django-admin startproject config .
```
```python
# settings.py

INSTALLED_APPS = [
    'articles',
   	...
]

...

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'
```

#### 0.2 애플리케이션 생성

```bash
# 애플리케이션 생성
$ python manage.py startapp articles
```

#### 0.3 URL 로직 분리(위임)

- 사용자가 articles/ 라는 경로로 접근할 경우, articles 애플리케이션의 'urls.py'에서 처리하도록 로직 수정

**03_django_crud > config > urls.py**

```python
# 03_django_crud/config/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('articles/', include('articles.urls')),
    path('admin/', admin.site.urls),
]
```
**03_django_crud > articles > urls.py 파일 생성** 

```python
# urls.py 파일 생성
# 03_django_crud/articles/urls.py

from django.urls import path
from . import views

urlpatterns = [
   path('', views.index),
]
```
#### 0.4 템플릿 경로 커스터마이징 + `base.html` 만들기

- 장고는 Default로 애플리케이션 내부의 templates를 바라보도록 설정되어 있습니다.
- 앞으로 config 폴더 안에 있는 templates 폴더를 바라보도록 경로를 커스터마이징 해주세요.

**config > templates 파일 생성 > articles 폴더 생성** 

```python
# settings.py 
# TEMPLATES > 'DIRS' 경로설정 해줘야한다!!!

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'config', 'templates')], # 수정(경로설정)
        ...
    },
]
```

![image-20191030173216638](assets/image-20191030173216638.png)

**views.py 코드 추가**

```python
# views.py

from django.shortcuts import render

def index(request):
    return render(request,'articles/index.html')
```

**articles 폴더에 index.html 파일 추가**

```html
<!-- index.html -->

<h2> INDEX 페이지 </h2>
```



**templates 폴더에 base.html 파일 추가**

Bootstrap 이용 - https://getbootstrap.com/docs/4.3/getting-started/introduction/ 

```html
<!-- base.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>장고 CRUD</title>

  <!-- Bootstrap CSS -->
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

</head>
<body>

  <div class = "container">
    {% block body %}
    {% endblock body %}
  </div>


  <!-- Bootstrap JS -->
  <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>

</body>
</html>
```

#### 0.5 데이터베이스 모델링

**models.py 코드 추가**

```python
# models.py

from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 객체 표시 형식 수정 
    def __str__(self):
        return f'[{self.pk}] {self.title}'
```

`makemigrations` **: 설계도 만들기** 

```bash
$ python manage.py makemigrations
```

```bash
# 파일 구조

03_django_crud/
    config/
    articles/
        migrations/
            0001_initial.py
```

`migrate` **: 실제 DB에 반영하기**

```bash
$ python manage.py migrate
```

**추가 정보**

- `showmigrations` : makemigrations를 통해 만든 설계도가 실제 DB에 반영된 상태인지 아닌지 확인

- `sqlmigrate` : 실제 DB에 반영하기 전 SQL 쿼리문으로 바뀐 모습 확인

  ```bash
  $ python manage.py sqlmigrate articles 0001
  ```



## 1. CREATE

- 기본적으로 두 개의 뷰 함수로 구성된다.
  1. 사용자에게 HTML Form을 던져줄 함수
  2. HTML Form에서 데이터를 전달받아서 실제 DB에 저장하는 함수
- **일단 GET 요청을 통해 구현해보자!**

```python
# 03_django_crud
# articles/views.py

from django.shortcuts import render
from .models import Article

# 사용자에게 게시글 작성 폼을 보여 주는 함수
def new(request):
    return render(request,'articles/new.html')

# 사용자로부터 데이터를 받아서 DB에 저장하는 함수
def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')

    article = Article(title=title, content=content)
    article.save()
    return render(request,'articles/index.html')
```

```html
<!-- articles/new.html -->

<!-- 상속 받는 코드 -->
{% extends 'base.html' %}

{% block body %}
<h1 class="text-center">NEW</h1>
<form action="/articles/create/" method="GET">
  TITLE: <input type="text" name="title"><br>
  CONTENT: <textarea name="content" cols="30" rows="10"></textarea><br>
  <input type="submit">
</form>
<hr>
<a href="/articles/">[BACK]</a>
{% endblock %}
```

```html
<!-- articles/create.html -->

<!-- 상속 받는 코드 -->
{% extends 'base.html' %}

{% block body %}
<h2> 글 작성이 완료되었습니다.! </h2>
{% endblock body %}
```

- 데이터가 정상적으로 저장됐는지 확인하기 위해 admin 페이지로 들어가보기.

  - admin 계정 생성

  ```bash
  $ python manage.py createsuperuser
  ```
  
  - admin.py 코드 추가
  
  ``` python
  # admin.py
  
  from django.contrib import admin
  from .models import Article
  
  class ArticleAdmin(admin.ModelAdmin):
      list_display = ('pk', 'title', 'content', 'created_at', 'updated_at',)
  
  admin.site.register(Article, ArticleAdmin)
  ```
  
 - 메인 페이지에서 게시글 목록이 나오게 해보기 **(Read - Index 로직)** 

```python
# 03_django_crud
# articles/views.py

from django.shortcuts import render
from .models import Article

def index(request):
    articles = Article.objects.all()[::-1] # 정렬_내림차순
    context = {'articles':articles}
    return render(request,'articles/index.html', context)
```

```html
<!-- articles/index.html -->

<!-- 상속 받는 코드 -->
{% extends 'base.html' %}

{% block body %}
<h1 class="text-center">Articles</h1>
<a href="/articles/new/">[NEW]</a>
<hr>
{% for article in articles %}
  <p>글 번호: {{ article.pk }}</p>
  ...
  <p>수정 시각: {{ article.updated_at }}</p>
  <hr>
{% endfor %}
{% endblock %}
```

- 게시글 작성 요청 방식을 `GET`에서 `POST` 방식으로 바꾸기
  - 지금은 GET 요청으로 보내고 있어서 쿼리 스트링에 데이터가 노출되고 있다. 이는 우리 서버의 데이터 구조가 노출될 위험도 있고, URL 경로로만 게시글 작성이 가능하면 서버 폭파의 위험성이 증가한다.
  - POST 요청으로 바꾸어 HTTP body에 내용을 숨기고 작성자의 신원을 확인하는 절차를 거치도록 한다.

```python
# 03_django_crud
# articles/views.py

from django.shortcuts import render
from .models import Article

# 사용자에게 게시글 작성 폼을 보여 주는 함수
def new(request):
    return render(request,'articles/new.html')

# 사용자로부터 데이터를 받아서 DB에 저장하는 함수
def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    article = Article(title=title, content=content)
    article.save()
    return render(request,'articles/index.html')
```

```html
<!-- articles/new.html -->

<!-- 상속 받는 코드 -->
{% extends 'base.html' %}

{% block body %}
<h1 class="text-center">NEW</h1>
<form action="/articles/create/" method="POST">
<!-- POST 요청할 때 반드시 설정 -->
{% csrf_token %} 
  TITLE: <input type="text" name="title"><br>
  CONTENT: <textarea name="content" cols="30" rows="10"></textarea><br>
  <input type="submit">
</form>
<hr>
<a href="/articles/">[BACK]</a>
{% endblock %}
```

- 지금은 게시글 작성을 완료한 뒤 "게시글 작성이 완료됐어요"라는 어색한 로직으로 구현되어 있다.
  - **데이터베이스에 게시글 작성이 완료되면 메인 페이지로 `redirect` 시켜버리자.**

  ```python
  # 03_django_crud
  # articles/views.py
  
  from django.shortcuts import render, redirect
  from .models import Article
  
  # 사용자로부터 데이터를 받아서 DB에 저장하는 함수
  def create(request):
      title = request.POST.get('title')
      content = request.POST.get('content')
  
      article = Article(title=title, content=content)
      article.save()
      # return render(request,'articles/index.html')
      return redirect('/articles/')
  ```

  

## 2. READ(Detail 페이지)

 게시글 목록이 출력되는 메인 페이지에서 글 내용, 수정 시각 등 모든 정보를 보여줄 필요는 없다. **메인 페이지에선 글 번호, 글 제목과 같은 기본적인 내용만 보여주고, 사용자가 클릭했을 때 게시글 상세정보 페이지로 이동**하도록 만들어보자. 

```python
# 03_django_crud
# articles/views.py


# 게시글 상세정보를 가져오는 함수

# Variable Routing 적용
# 사용자가 요청을 보낸 URL로부터 게시글 PK 값을 건네받는다.
def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {'article':article} # 딕셔너리 형태로 넘겨주기
    return render(request, 'articles/detail.html', context)
```

```python
# 03_django_crud/articles/urls.py

# Variable Routing 적용
# 사용자가 게시글을 조회할 때 articles/1, articles/2 처럼 게시글들 중에 1번 게시글, 게시글들 중에 2번 게시글과 같은 모습으로 접근하는 것이 자연스럽다.

from django.urls import path
from . import views

urlpatterns = [
    path('<int:article_pk>/', views.detail),
    ...
]
```

```html
<!-- detail.html -->

<!-- 상속 받는 코드 -->
{% extends 'base.html' %}

{% block body %}
<h1 class="text-center">DETAIL</h1>
<p>글 번호 : {{ article.pk }}</p>
<p>글 제목 : {{ article.title }}</p>
<p>글 내용 : {{ article.content }}</p>
<p>생성 시각 : {{ article.created_at }}</p>
<p>수정 시각 : {{ article.updated_at }}</p>
<hr>
<a href="/articles/">[BACK]</a>
{% endblock %}
```

```html
<!-- articles/index.html -->

<!-- 상속 받는 코드 -->
{% extends 'base.html' %}

{% block body %}
  <h1 class="text-center">Articles</h1>
  <a href="/articles/new">[NEW]</a>
  <hr>
  {% for article in articles %}
  <p> [{{article.pk }}] {{ article.title }}</p>
    <a href="/articles/{{article.pk }}">[DETAIL]</a>
  <hr>
  {% endfor %}
{% endblock body %}
```



### 2019-10-31



## 3. UPDATE

```python
# 03_django_crud
# articles/views.py

# 게시글 수정하는 함수 - 사용자한테 게시글 수정 폼을 전달
def edit(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {'article':article}
    return render(request, 'articles/edit.html', context)

# 수정 내용 전달받아서 DB에 저장(반영)
def update(request, article_pk):
    # 1. 수정할 게시글 인스턴스 가져오기
    article = Article.objects.get(pk=article_pk) 

    # 2. 폼에서 전달받은 데이터 덮어쓰기
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    
    # 3.DB에 저장
    article.save()

    # 4. 저장 끝났으면 게시글 Datail로 이동시키기
    return redirect('articles:detail', article_pk)
```
```html
<!-- edit.html -->

<!-- 상속 받는 코드 -->
{% extends 'base.html' %}

{% block body %}
<h1 class="text-center">EDIT</h1>
{% comment %} <form action="/articles/{{ article.pk }}/update/" method="POST"> {% endcomment %}
<form action="{% url 'articles:update' article.pk %}" method="POST">
<!-- POST 요청할 때 반드시 설정 -->
{% csrf_token %} 
  <label for = "title">제목</label> 
  <!--value를 지정해줘야지 수정가능함-->
  <input type="text" name="title" value="{{ article.title }}"><br> 
  <label for = "content">내용</label>
  <textarea name="content" cols="30" rows="10" >
  {{ article.content}}
  </textarea><br>
  <input type="submit">
</form>
<hr>
<a href="{% url 'articles:detail' article.pk %}">[BACK]</a>
{% endblock %}
```

```html
<!-- detail.html -->

<!-- 상속 받는 코드 -->
{% extends 'base.html' %}

...
<a href="{% url 'articles:edit' article.pk %}">[EDIT]</a>
...

{% endblock %}
```

```python
# articles/urls.py

from django.urls import path
from . import views

# app name을 지정해줄 수 있음 - 다른 애플리케이션에서 중복되지 않게 해줌
app_name = 'articles'

urlpatterns = [             # name = '' : 일반적으로 view이름이랑 같게 설정
    ...
    path('<int:article_pk>/edit/', views.edit, name='edit'), # UPDATE Logic - 폼 전달
    path('<int:article_pk>/update/', views.update, name='update'), # UPDATE Logic - DB 저장
    
]
```



## 4. DELETE


```python
# 03_django_crud
# articles/views.py

# 삭제 페이지
def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    article.delete()
    return redirect('/articles/')
```

```html
<!-- detail.html -->

<!-- 상속 받는 코드 -->
{% extends 'base.html' %}
...

<a href="/articles/{{ article.pk }}/delete/">[DELETE]</a>
{% endblock %}
```

```python
# 03_django_crud/articles/urls.py

from django.urls import path
from . import views

urlpatterns = [
    ...
	path('<int:article_pk>/delete/', views.delete), # DELETE Logic - 삭제
    ...
]
```

```python
# articles/urls.py

from django.urls import path
from . import views

# app name을 지정해줄 수 있음 - 다른 애플리케이션에서 중복되지 않게 해줌
app_name = 'articles'

urlpatterns = [             # name = '' : 일반적으로 view이름이랑 같게 설정
    ...
    path('<int:article_pk>/', views.detail, name='detail'),  # READ Logic - Detail
    path('<int:article_pk>/delete/', views.delete, name='delete'), # DELETE Logic - 삭제
    ...
    
]
```



## + urls.py -> app_name,path(...,name='') 

- `app_name`

  모든 앱의 urls.py 에서 `app_name`을 지정해주면 다른 앱들과의 충돌을 막아 에러가 나는 일을 줄여줄 수 있다.

- `path(...,name=' ')`

  모든 앱의 urls.py에서 `name`은 보통 views.py 에서 생성한 `view`함수명을 사용한다. 

- 모든 html, views.py에서 `URL Namespace`를 사용하는 것이 바람직하다!!

