from django.shortcuts import render
from django.views.generic import TemplateView
from templates import *


def home(request):
    return render(request, "homes/home.html", locals())
