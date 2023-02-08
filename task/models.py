from django.db import models

# Create your models here.

class User(models.Model):
    id = models.IntegerField("ID", unique=True, primary_key=True)
    name = models.IntegerField("имя", default=0)
    books = models.CharField("Книги", max_length=50)
    
    def __str__(self):
        return self.name
    
class Category(models.Model):
    id = models.IntegerField("ID", unique=True, primary_key=True)
    name = models.CharField("имя", max_length=50)
    
    def __str__(self):
        return self.name
    
class Tag(models.Model):
    id = models.IntegerField("ID", unique=True, primary_key=True)
    name = models.CharField("имя", max_length=50)
    
    def __str__(self):
        return self.name
    
class Book(models.Model):
    id = models.IntegerField("ID", unique=True, primary_key=True)
    name = models.CharField("имя", max_length=50)
    category_id = models.IntegerField("Категории ID", default=0)
    author_id = models.IntegerField("Автор книг", default=0)
    tags = models.ManyToManyField("Tag", verbose_name=("Теги"))
    
    def __str__(self):
        return self.name