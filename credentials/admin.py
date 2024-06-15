from django.contrib import admin

# # Register your models here.
# from django.contrib import admin
from .models import Interest,Purpose

# admin.site.register(customuser)
admin.site.register(Interest)
admin.site.register(Purpose)