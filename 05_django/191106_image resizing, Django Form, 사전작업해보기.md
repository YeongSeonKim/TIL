### 2019-11-06

# Django Form

## Image Resizing(ProcessedImageField)

> 이미지 업로드를 통해 사용자로부터 이미지를 받을 때, 과도한 크기의 이미지가 업로드 되면 서버의 부하를 야기시킨다. 또 Thumbnail 크기가 너무 커지기 때문에 조절이 필요하다.

**djangi-imagekit을 활용해서 이미지 업로드 이미지 크기를 조절해보자!**

- 사용자로부터 이미지를 업로드 받는 그 순간에 조절된 이미지 크기를 받을 수 있다. 
- READ 로직을 수행할 때에도 일정하고 동일한 크기로 이미지를 보일 수 있다.

### 1.라이브러리 설치

```bash
$ pip install Pillow
$ pip install pilkit
$ pip install django-imagekit
```

#### [ Pillow ]

- PIL (Python Image Library) 프로젝트에서 fork 되어 나온 라이브러리
- Python3을 지원하지 않기 때문에 Pillow를 많이 쓴다.

![image-20191106111013942](assets/image-20191106111013942.png)

#### [ pilkit ]

- Pillow를 쉽게 쓸 수 있도록 도와주는 라이브러리
- 다양한 Processsors 지원
  - Thumbnail
  - Resize
  - Crop ...

![image-20191106110727713](assets/image-20191106110727713.png)

#### [ django-imagekit ]

- 이미지 썸네일 Helper

![image-20191106111219219](assets/image-20191106111219219.png)

- 라이브러리 설치 확인

  ![image-20191106111318445](assets/image-20191106111318445.png)

### 2. App 등록

#### INSTALLED_APPS 등록

- settings.py

  ```python 
  INSTALLED_APPS = [
      'articles',
      'students',
      'jobs',
      .
      .
  
      'imagekit',
      
      .
      .
      .
  ]
  ```



### 3. Modeling

- models.py 코드 수정

  ```python 
  from django.db import models
  from imagekit.models import ProcessedImageField
  from imagekit.processors import Thumbnail
  # improt 추가 - ProcessedImageField, Thumbnail
  
  class Article(models.Model):
      title = models.CharField(max_length=40)
      content = models.TextField()
      
  	# 이미지 - ProcessedImageField를 활용하는 코드로 변경
      image = ProcessedImageField(
          processors=[Thumbnail(200,300)],    # 처리할 작업
          format='JPEG',                      # 이미지 포맷
          options={                           # 각종 추가 옵션
              'quality' : 90
          },
          upload_to = 'articles/image'        # 저장 위치
          # 실제 경로 : MEDIA_ROOT/articles/image
      )
  
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
  
      # 객체 표시 형식 수정 
      def __str__(self):
        return f'[{self.pk}번글]: {self.title}|{self.content}'
  ```
  
  

### 4. Migration

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

![image-20191106112415929](assets/image-20191106112415929.png)

![image-20191106112445814](assets/image-20191106112445814.png)

- ProcessedImageField의 인자로 들어가는 옵션들은 수정을 하더라도 다시 migration 하지 않아도 **바로바로 적용**이 된다.

![image-20191106112513424](assets/image-20191106112513424.png)



## 구현 해보기

### 1. 사전 준비

> Django Form을 적용하기 전, 이때까지 우리가 학습했던 HTML Form으로 앱을 구현해보자.

- **프로젝트 생성**

  ```bash
  $ mkdir 04_django_form
  $ cd 04_django_form
  ```
  
  ![image-20191106114410609](assets/image-20191106114410609.png)

  ```bash
  $ django-admin startproject config .
  ```

![image-20191106122738528](assets/image-20191106122738528.png)

- **앱 생성**

  ```bash
  $ python manage.py startapp articles
  ```

![image-20191106122638485](assets/image-20191106122638485.png)

![image-20191106122757324](assets/image-20191106122757324.png)

- **Article Model**

  ```python
  # models.py
  
  from django.db import models
  
  class Article(models.Model):
      title = models.CharField(max_length=40)
      content = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
  
      # 객체 표시 형식 
      def __str__(self):
           return f'[{self.pk}번글]: {self.title}|{self.content}'
  
  ```

모델 설정하고 makemigrations 

![image-20191106125226766](assets/image-20191106125226766.png)

showmigrations

![image-20191106125319432](assets/image-20191106125319432.png)

migrate

![image-20191106125340751](assets/image-20191106125340751.png)

- **admin 설정**

  ```bash
$ python manage.py createsuperuser
  ```

![image-20191106125526086](assets/image-20191106125526086.png)

- **URL 설정**

  ```python
  # config/urls.py
  
  from django.contrib import admin
  from django.urls import path, include
  
  urlpatterns = [
      path('articles/', include('articles.urls')),
      path('admin/', admin.site.urls),
  ]
  ```

  ```python
  # articles/urls.py
  
  from django.urls import path
  from . import views
  
  app_name = 'articles'
  
  urlpatterns = [
      path("", views.index, name='index'),
      path("create/", views.create, name='create'),
      path("<int:article_pk>/", views.detail, name='detail'),
  
  ]
  ```

- **base.html 생성** (부트스트랩 적용X)

- **Index 페이지** (-> 모든 게시글 보여주기)

  ```python
  # views.py
  
  def index(request):
      pass
  ```

  ```html
  <!-- index.html -->
  ```

- **Create 페이지**

  ```python
  # views.py
  
  def create(request):
      pass
  ```

  ```html
  <!-- create.html -->
  ```

- **Detail 페이지**

  ```python
  # views.py
  
  def detail(request, article_pk):
      pass
```
  
  ```html
  <!-- detail.html -->
  ```

 

## Django Form

> Django에서 제공하는 Form 클래스를 이용해서 편리하게 폼 정보를 관리하고 유효성 검증을 진행하고, 비유효 fileId에 대한 에러 메세지를 결정한다.
>
> 즉, HTML으로 Form 입력을 관리하던 것을 Django에서 제공하는 Form 클래스로 바꿔보는 작업을 해보자.

- **Form 의 장점(->자동화)**
  - `blank=True`와 같은 옵션을 따로 지정해주지 않았으면, HTML 태그에 required 옵션이 자동으로 붙는다.
  - 기존에 max_length와 같은 조건을 어길 경우 에러 페이지를 출력했는데,  Django Form을 써서 

```
In [1]: form
Out[1]: <ArticleForm bound=True, valid=Unknown, fields=(title;content)>

In [2]: request.POST
Out[2]: <QueryDict: {'csrfmiddlewaretoken': ['hDIVifOjEGF9GSPPWGp51l4LqEDk0FPkhTdLumU3AhCoGAbf95kqAbUbDXeGJERc'], 'title': ['제모고고고'], 'content': ['ㅇㄴㅇㄴㅇㄴㅇㄴ']}>

In [3]: form.is_valid()
Out[3]: True

In [4]: form
Out[4]: <ArticleForm bound=True, valid=True, fields=(title;content)>
```

- `get_object_or_404`
  - 500

- forms.py 파일을 04_django_form/articles 에 생성한다.

```python
# articles/forms.py

from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField(
        max_length=30,
        # HTML Tag와 동일
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class':'title',
                'placeholder':'제목을 입력해 주세요...!',
            }
        )
    )
    content = forms.CharField(
        label='내용',
        # widget : Input Type 지정 -> Textarea / 알맞은 속성값 부여
        widget=forms.Textarea(
            attrs={
                'class':'content',
                'placeholder':'내용을 입력해 주세요오오오옹',
                'rows':5,
                'cols':30,
            }
        )
    )
```

