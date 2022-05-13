from rest_framework import serializers
from .models import JournalItem
from datetime import datetime
class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = JournalItem
        fields = ('id','title' ,'date', 'content')
        