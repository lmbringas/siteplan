from django.contrib import admin

# Register your models here.
from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Task

admin.site.register(Task, MPTTModelAdmin)