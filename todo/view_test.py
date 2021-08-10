from django.shortcuts import render
from .serializers import TodoSerializer 
from rest_framework import viewsets      
from .models import TodoItem                 

class TodoView(viewsets.ModelViewSet):  
    serializer_class = TodoSerializer   
    queryset = TodoItem.objects.all()     