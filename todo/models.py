from django.db import models
from datetime import datetime
import pytz
# Create your models here.
class TodoItem(models.Model):
    content = models.TextField()
    date = models.DateTimeField(default=datetime.utcnow)
