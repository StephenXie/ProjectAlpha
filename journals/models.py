from django.db import models
from datetime import datetime
import pytz
# Create your models here.
class JournalItem(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField()
    date = models.DateTimeField(blank=True, default=datetime.utcnow)
    content = models.TextField(blank=True)