# Like, Profile, Follow

## 1. Like

> `User`는 여러개의 `Article`에 좋아요 표시를할 수 있고, `Article`은 여러명의 `User`에게 좋아요를 받을수 있다.

### 1.1 Model 설정

- `blank=True`
  - 최초 작성되는 글에는 좋아요가 없고, 글이 작성되더라도 좋아요를 받지 못할 수 도 있다.
  - 이 옵션을 줘서 유효성 검사를 통과한다.
  - 실제 데이터베이스는 null이 들어가는게아니라 빈 스트링(`''`)의 형태로 들어간다.

```python
# 04_django_form/articles/models.py

class Article(models.Model):
    ...
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # article1.like_users
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles', blank=True)

```

임의의 테이블이 생성되었다.

![1573604741770](assets/1573604741770.png)

![1573610028367](assets/1573610028367.png)

- 현재 상황에서 `related_name`설정은 필수
  - `like_users` 필드에 `related_name`을 쓰지 않으면 User 입장에서 article_set을 사용할 경우 user 필드를 갖고올지 like_users 필드를 갖고 올지 인식을 하지 못한다.
  - `related_name` 설정과 함께 해당필드는 article_set과 같은 방식으로 호출하지 못하고 `like_users `방식으로 호출해야 한다.
- 사용할 수 있는 `ORM` 기능(명령어)
  - `user.article_set.all()` : 유저가 작성한 게시글 전부
  - `user.like_articles.all()` : 유저가 좋아요 누른 게시글 전부
  - `article.user` : 게시글 작성한 유저 - 1:N
  - `article.like_users` : 게시글 좋아요 누른 유저 전부 - M:N

### 1.2 View & URL

- `exists()` & `filter()`
  - `filter()` :  특정한 조건에 맞는 레코드들을 가져온다. 
  - `exists()` : 최소한 하느의 레코드가 존재하는지 여부를 말해준다.
- `get()`vs `filter()` -> 데이터가 없는 경우 에러여부 
  - `get()`은 에러가나고 `filter()` 는 에러가 나지 않는다.

```python
# 04_django_form/articles/views.py


```









### 1.3 Template

#### 1.3.1 Template 분리 (`artilce.html`)

- 모듈화한 템플릿은 제목 앞에 언더스코어(`_`)를 붙여주는 것이 코딩 컨벤션!!

```
articles/
	templates/
		articles/
			_article.html
			index.html
			...
```

![1573609282647](assets/1573609282647.png)

- Bootstrap Card 컴포넌트를 사용해서 예쁘게 꾸며보자.
  - Bootstrap 공식 홈페이지 -> Documentation -> Cards

```django
<!-- articles/index.html -->


```

```django
<!-- articles/_articles.html -->


```

#### 1.3.2 Font- Awesome 아이콘 적용 및 분기

>  https://fontawesome.com/  들어가서 가입 후  Kits로 들어가서 코드 복사

![1573607564250](assets/1573607564250.png)

```django
<!-- base.html -->

<!DOCTYPE html>
  ...
  <!-- FontAwesome -->
  <script src="https://kit.fontawesome.com/ kits 코드번호.js" crossorigin="anonymous"></script>
</head>
```

```django
<!-- articles/_articles.html -->



```





## 2. Profile 페이지

> 각 유저마다 프로필 페리지를 만들어주자.

- User에 대해서 CRUD 로직을 구현한다고 생각하면,  READ(Detail)에 속한다.

#### 2.1 View & URL

- User에 대한 CRUD 로직 대부분을 accounts 앱에서 구현했으므로, Profile 페이지 역시 accounts 앱에 구현해보자.

```python
# accounts/views.py


```

```python
# accounts/urls.py

from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
   	...
    # url 패던에서 str을 사용하면 맨아래에 위치해서 마지막에 탐색되게 해야한다. 조건을 붙일경우에는 위치상관없음
    path('<str:username>/', views.profile, name='profile'),

]
```



