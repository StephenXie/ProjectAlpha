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
from django.urls import path,include
from todo.views import todoView, addTodo, deleteTodo
from formatter.views import FormatterView,FormatterPost
from cryptic.views import CrypticView,CrypticPost
from GPAcal.views import GPAcal
from PasteX.views import PasteXView
from django.conf import settings
from django.views.static import serve
from django.conf.urls import url
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('AppX.urls')),
    path('formatter/',FormatterView),
    path('formatter/post',FormatterPost),
    path('cryptic/',CrypticView),
    path('cryptic/post',CrypticPost),
    path('GPAcal/',GPAcal),
    path('todo/',todoView),
    path('addTodo/',addTodo),
    path('deleteTodo/<int:todo_id>/', deleteTodo),
    path('pastex/',PasteXView),
    path('pastex/<str:my_id>/',PasteXView),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),

]
