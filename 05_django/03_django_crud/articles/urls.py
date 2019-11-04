from django.urls import path
from . import views

# app name을 지정해줄 수 있음 - 다른 애플리케이션에서 중복되지 않게 해줌
app_name = 'articles'

urlpatterns = [             # name = '' : 일반적으로 view이름이랑 같게 설정
    path('', views.index, name='index'),  # READ Logic - Index
    # path('new/', views.new , name='new'), # CREATE Logic - 사용자에게 폼 전달 
    # GET(new) / POST(create) 
    path('create/', views.create, name='create'),  # CREATE Logic - 데이터베이스에 저장
    path('<int:article_pk>/', views.detail, name='detail'),  # READ Logic - Detail
    path('<int:article_pk>/delete/', views.delete, name='delete'), # DELETE Logic - 삭제
    # path('<int:article_pk>/edit/', views.edit, name='edit'), # UPDATE Logic - 폼 전달
    # GET(edit) / POST(update)
    path('<int:article_pk>/update/', views.update, name='update'), # UPDATE Logic - DB 저장
    
]
