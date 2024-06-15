from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=100,default=None)

class SubMenu(models.Model):
    name = models.CharField(max_length=100,default=None)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

class SubSubMenu(models.Model):
    name = models.CharField(max_length=100,default=None)
    submenu = models.ForeignKey(SubMenu, on_delete=models.CASCADE)

# def __str__(self):
#      return f"{self.name} - {self.submenu.menu.name}"
