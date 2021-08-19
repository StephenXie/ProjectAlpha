from django.db import models
from datetime import datetime
import pytz
# Create your models here.
class TodoItem(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField()
    date = models.DateTimeField(blank=True, default=datetime.utcnow)