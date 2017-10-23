from django.shortcuts import render
from Library.models import *


def library(request):
    books = Book.objects.all()
    return render(request, 'library/library.html', locals())


def about_book(request, product_id):
    book = Book.objects.get(id=product_id)
    book_image = BookPicture.objects.get(id=product_id)
    return render(request, 'library/about_book.html', locals())
