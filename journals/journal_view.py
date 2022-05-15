from django.shortcuts import render
from .serializers import JournalSerializer 
from rest_framework import viewsets      
from .models import JournalItem                 
from rest_framework.permissions import IsAuthenticated
class JournalView(viewsets.ModelViewSet):  
    permission_classes = (IsAuthenticated,)
    serializer_class = JournalSerializer    
    def get_queryset(self):
        return self.request.user.journals.all()
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)