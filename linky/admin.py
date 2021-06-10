from django.contrib import admin
from .models import LinkyItem


# Register your models here.
class LinkyAdmin(admin.ModelAdmin):
    list_display = ("id","content")

admin.site.register(LinkyItem, LinkyAdmin)