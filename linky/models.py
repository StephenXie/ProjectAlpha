from django.db import models

# Create your models here.


class LinkyItem(models.Model):
    id = models.CharField(max_length=30, primary_key=True)
    content = models.TextField()
