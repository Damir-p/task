from django.db import models

class User(models.Model): 
    name = models.CharField(max_length=250, blank=True, null=True, verbose_name="Имя")
    books = models.ManyToManyField('self',related_name='books')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name= 'Имя'
        verbose_name_plural = 'Имя'
        ordering = ('-id',)
