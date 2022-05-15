from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import pytz
# Create your models here.
class JournalItem(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name="journals", on_delete=models.CASCADE, null=True)
    title = models.TextField()
    date = models.DateTimeField(blank=True, default=datetime.utcnow)
    content = models.TextField(blank=True)