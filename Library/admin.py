from django.contrib import admin
from .models import *


class BookAdmin (admin.ModelAdmin):
    list_display = ('name', 'author', 'genre', 'price')
    list_filter = ['name', 'author', 'genre']
    search_fields = ['name', 'author', 'genre']

    fields = ['name', 'author', 'genre', 'price', 'description']

    class Meta:
        model = Book

admin.site.register(Book, BookAdmin)


class AuthorAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Author._meta.fields]
    search_fields = ['sur_name', 'genre']

    fields = ["name", "sur_name"]

    class Meta:
        model = Author

admin.site.register(Author, AuthorAdmin)


class GenreAdmin (admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ['name']
    search_fields = ["name"]

    fields = ["name"]

    class Meta:
        model = Genre

admin.site.register(Genre, GenreAdmin)