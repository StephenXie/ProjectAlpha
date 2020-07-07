from django.urls import path
from . import views

urlpatterns = [
    path('',views.hi,name='home'),
]
