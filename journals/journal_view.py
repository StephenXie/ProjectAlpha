from django.shortcuts import render
from .serializers import JournalSerializer 
from rest_framework import viewsets      
from .models import JournalItem                 

class JournalView(viewsets.ModelViewSet):  
    serializer_class = JournalSerializer   
    queryset = JournalItem.objects.all()  