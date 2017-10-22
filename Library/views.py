from django.shortcuts import render
from Library.models import *


def library(request):
    books = Book.objects.all()
    return render(request, 'library/library.html', locals())

#
# def book(request):
#     return render(request, 'homes/home.html', locals())
