from django.shortcuts import render
from .serializers import JournalSerializer 
from rest_framework import viewsets      
from .models import JournalItem                 
from rest_framework.permissions import IsAuthenticated
class JournalView(viewsets.ModelViewSet):  
    permission_classes = (IsAuthenticated,)
    serializer_class = JournalSerializer   
    queryset = JournalItem.objects.all()  