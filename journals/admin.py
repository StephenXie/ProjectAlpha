from django.contrib import admin
from .models import JournalItem


# Register your models here.
class JournalAdmin(admin.ModelAdmin):
    list_display = ("id", "title")


admin.site.register(JournalItem, JournalAdmin)
