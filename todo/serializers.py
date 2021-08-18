from rest_framework import serializers
from .models import TodoItem
from datetime import datetime
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem

        fields = ('id','text' ,'date')

        