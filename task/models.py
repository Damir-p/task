from django.db import models

# Create your models here.

# class User(models.Model):
#     id = models.IntegerField("ID", unique=True, primary_key=True)
#     name = models.IntegerField("имя", default=0)
#     books = models.CharField("Книги", max_length=50)
    
#     def __str__(self):
#         return self.name
    
    

class Category(models.Model): 
    name = models.CharField(max_length=250, blank=True, null=True, verbose_name="Называния")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_= 'Категории'
        verbose_name = plural = 'Категория'
        ordering = (-id)
        
class Tag(models.Model): 
    tag_name = models.CharField(max_length=250, blank=True, null=True, verbose_name="Называния")
    
    def __str__(self):
        return self.tag_name
    
    class Meta:
        verbose_name_= 'Категории'
        verbose_name = plural = 'Категория'
        ordering = (-id)
            
    def __str__(self):
        return self.name
    
class Book(models.Model): 
    tag_name = models.CharField(max_length=250, blank=True, null=True, verbose_name="Называния")
     
    category_id = models.IntegerField("Категории ID", default=0)
    author_id = models.IntegerField("Автор книг", default=0)
    tags = models.ManyToManyField("Tag", verbose_name=("Теги"))   
    
    def __str__(self):
        return self.tag_name
    
    class Meta:
        verbose_name_= 'Категории'
        verbose_name = plural = 'Категория'
        ordering = (-id)
            
    def __str__(self):
        return self.name

    
   
  