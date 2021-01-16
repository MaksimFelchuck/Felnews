"""felchnews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from newspaper.views import *

urlpatterns = [
    path('', index, name="index"),
    path('news/pages<int:pages>/', main, name="main"),
    path('news-<int:news>/', news, name="news"),
    path('write/', write_news, name="write"),
    path('<int:news>/load_image/', load_image, name="load_image"),

]
