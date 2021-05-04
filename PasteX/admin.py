from django.contrib import admin
from .models import PasteXItem


# Register your models here.
class PastexAdmin(admin.ModelAdmin):
    list_display = ("content", "id", "language")

admin.site.register(PasteXItem, PastexAdmin)
