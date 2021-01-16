from django.contrib import admin
from newspaper.models import *


# Register your models here.

@admin.register(News, Image)
class PersonAdmin(admin.ModelAdmin):
    pass
