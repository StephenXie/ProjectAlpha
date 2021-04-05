from django.db import models

# Create your models here.
class PasteXItem(models.Model):
    content = models.TextField()