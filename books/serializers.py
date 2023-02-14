from .models import Book
from rest_framework import serializers

class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('-id', 'book_name', 'author', 'category', 'book_tag')