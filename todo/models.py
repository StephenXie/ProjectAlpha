from django.db import models
from datetime import datetime
import pytz
def getDate():
    tz = pytz.timezone('US/Pacific')
    d = datetime.now(tz)
    return d
# Create your models here.
class TodoItem(models.Model):
    content = models.TextField()
    date = models.DateTimeField(default=getDate)
