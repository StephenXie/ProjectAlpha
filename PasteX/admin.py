from django.contrib import admin
from .models import PasteXItem


# Register your models here.
class PasteXAdmin(admin.ModelAdmin):
    list_display = ("id", "content", "language")

admin.site.register(PasteXItem, PasteXAdmin)
