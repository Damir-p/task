from django.db import models

# Create your models here.
from category.models import Category, Tag
from accounts.models import User

class Book(models.Model):
    book_name = models.CharField(max_length=255, null=True, blank=True, verbose_name="Название книги")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='book_category', verbose_name='Категория')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author', verbose_name="Автор Книги")
    books_tag = models.ManyToManyField(Tag, related_name='tags')
    
    def __str__(self):
        return f"{self.book_name} - {self.author}"

    class Meta:
        verbose_name = ("Книга")
        verbose_name_plural = ("Книги")
        ordering = ('-id',)
 
