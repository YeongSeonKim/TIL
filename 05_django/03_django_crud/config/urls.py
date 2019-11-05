"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
    path('students/', include('students.urls')),
    path('jobs/', include('jobs.urls')),
]

# static()
# 첫번째 인자 : 어떤 URL을 정적으로 추가할 지(Media file)
# 두번째 인자 : 실제 해당 미디어 파일은 어디에 있는지?

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)