from django.contrib import admin
from . models import Menu ,SubMenu,SubSubMenu

# Register your models here.
admin.site.register(Menu)
admin.site.register(SubMenu)
admin.site.register(SubSubMenu)