from django.shortcuts import render, redirect
from .models import Article
from .models import Comment

# Create your views here.
def index(request):
    articles = Article.objects.all()[::-1] # 정렬_내림차순
    context = {'articles':articles}
    return render(request,'articles/index.html', context)

# 사용자에게 게시글 작성 폼을 보여 주는 함수
# def new(request):
#     return render(request,'articles/new.html')

# 사용자로부터 데이터를 받아서 DB에 저장하는 함수
def create(request):

    # POST 요청일 경우 -> 게시글 생성 로직 수행
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        article = Article(title=title, content=content, image=image)
        article.save()
        return redirect('articles:detail',article.pk) # URL Namespace
    # GET 요청일 경우 -> 사용자에게 폼 보여주기
    else:
        return render(request,'articles/create.html')
        

    # .html 파일 내에서 '{% url %} 템플릿 태그' 사용했을 때(헷갈림 주의!!) 
    # <a href="{% url 'articles:detail' article.pk %}">


# 게시글 상세정보를 가져오는 함수
def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    # comments = Comment.objects.filter(article_id=article_pk)
    comments = article.comment_set.all() # 댓글 정보 가져오는 코드
    context = { # 딕셔너리 형태로 넘겨주기
        'article':article,
        'comments':comments,
        } 
    return render(request, 'articles/detail.html', context)


# 게시글 삭제하는 함수
def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    article.delete()
    return redirect('articles:index')

# 게시글 수정하는 함수 - 사용자한테 게시글 수정 폼을 전달
# def edit(request, article_pk):
#     article = Article.objects.get(pk=article_pk)
#     context = {'article':article}
#     return render(request, 'articles/edit.html', context)

# 수정 내용 전달받아서 DB에 저장(반영)
def update(request, article_pk):
    article = Article.objects.get(pk=article_pk) 
    
    # POST 요청 -> DB에 수정사항 반영
    if request.method == "POST":
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect('articles:detail', article_pk)
    # GET 요청 -> 사용자에게 수정 Form 전달
    else:
        context = {'article':article}
        return render(request, 'articles/update.html', context)

# 댓글 생성 뷰 함수
def comments_create(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
       # comment.article = request.POST.get('article')
       content = request.POST.get('content')
       comment = Comment(article=article, content=content)
       # comment.article = article
       comment.save()
       return redirect('articles:detail', article_pk)
    else:
        return redirect('articles:detail', article_pk)

# 댓글 삭제 뷰 함수
def comments_delete(request, article_pk, comment_pk):
    
    if request.method == 'POST':
        comment = Comment.objects.get(pk=comment_pk)
        comment.delete()
    return redirect('articles:detail', article_pk)
    #     return redirect('articles:detail', article_pk)
    # else:
    #     return redirect('articles:detail', article_pk)
    