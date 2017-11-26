from django.shortcuts import render
from django.views.generic import TemplateView


class AboutView(TemplateView):
    template_name = "abouts/about.html"



#
# def about(request):
#     return render(request, "abouts/about.html", locals())