from django.db import models


# Create your models here.
class FormatterItem(models.Model):
    content = models.TextField()
