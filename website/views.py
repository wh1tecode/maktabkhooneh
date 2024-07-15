from django.shortcuts import render
from os.path import join

# Create your views here.


def home_view(request):
    return render(request, "index.html")


def about_view(request):
    return render(request, "about.html")


def contact_view(request):
    return render(request, "contact.html")
