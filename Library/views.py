from django.shortcuts import render


def library(request):
    return render(request, 'library/library.html', locals())
