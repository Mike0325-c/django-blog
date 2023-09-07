"""jjy2 URL Configuration

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
from django.urls import path, re_path
from app1 import views as one


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',one.home),
    path('index/', one.index),
    path('login/', one.login),
    path('regist/', one.regist),
    path('userlist/', one.userlist),
    path('edit/', one.edit),
    path('delete/', one.delete),
    # re_path(r'^$', one.home)
    # re_path('home/(\d+)/(\w+)',one.home),
    re_path('test/(\d+)/(\d+)', one.test, name='ooo'),  # /test/数字/
    # re_path('testadd/(?P<year>\d+)/', one.testadd, name='ooo'),
    re_path('testadd/(?P<year>\d+)/(?P<month>\d+)', one.testadd, name='xxx'),
    re_path('^$', one.home),
    path('json/', one.indexjson),
    path('file/', one.file),
    path('login6/', one.Login6.as_view()),  # views.view
    path('test6/', one.test6)
]
