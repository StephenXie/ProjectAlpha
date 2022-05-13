"""ProjectX URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from rest_framework import routers  
from todo.views import todoView, addTodo, deleteTodo
from todo import todo_view
from journals import journal_view
from formatter.views import FormatterView
from cryptic.views import CrypticView, CrypticPost
from GPAcal.views import GPAcal
from GPAcal.views_test import api_GPAcal
from PasteX.views import PasteXView
from linky.views import LinkyView
from django.conf import settings
from django.views.static import serve
from django.conf.urls import url

router = routers.DefaultRouter()                   
router.register(r'todos', todo_view.TodoView, 'todo')  
router.register(r'journals', journal_view.JournalView, 'journal') 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls),), 
    path('', include('AppX.urls')),
    path('formatter/', FormatterView),
    path('formatter/post', FormatterView),
    path('cryptic/', CrypticView),
    path('cryptic/post', CrypticPost),
    path('GPAcal/', GPAcal),
    path('apiGPAcal/',api_GPAcal),
    path('todo/', todoView),
    path('addTodo/', addTodo),
    path('deleteTodo/<int:todo_id>/', deleteTodo),
    path('pastex/', PasteXView),
    path('pastex/<str:my_id>/', PasteXView),
    path('linky/', LinkyView),
    path('linky/<str:my_id>/', LinkyView),
    url(r'^media/(?P<path>.*)$', serve,
        {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,
        {'document_root': settings.STATIC_ROOT}),

]