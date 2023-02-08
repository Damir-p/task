from django.db import models

# Create your models here.

class User(models.Model):
    id = models.IntegerField(_(""))
    name = models.IntegerField(_(""))
    books = models.CharField(_(""), max_length=50)
    
    
class Category(models.Model):
    id = models.IntegerField(_(""))
    name = models.CharField(_(""), max_length=50)
    
    
    
class Tag(models.Model):
    id = models.IntegerField(_(""))
    name = models.CharField(_(""), max_length=50)
    
    
class Book(models.Model):
    id = models.IntegerField(_(""))
    name = models.CharField(_(""), max_length=50)
    category_id = models.CharField("")
    author_id = models.CharField("")
    tags = models.ForeignKey("app.Model", verbose_name=_(""), on_delete=models.CASCADE)