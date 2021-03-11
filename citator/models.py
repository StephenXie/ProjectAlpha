from django.db import models


# Create your models here.
class CitatorItem(models.Model):
    content = models.TextField()
