from django.contrib import admin

# Register your models here.

from .models import DogsData

admin.site.register(DogsData)
