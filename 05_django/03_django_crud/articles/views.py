from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()[::-1] # 정렬_내림차순
    context = {'articles':articles}
    return render(request,'articles/index.html', context)

# 사용자에게 게시글 작성 폼을 보여 주는 함수
def new(request):
    return render(request,'articles/new.html')

# 사용자로부터 데이터를 받아서 DB에 저장하는 함수
def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    article = Article(title=title, content=content)
    article.save()
    # return render(request,'articles/index.html')
    return redirect('/articles/')

# 게시글 상세정보를 가져오는 함수
def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {'article':article} # 딕셔너리 형태로 넘겨주기
    return render(request, 'articles/detail.html', context)