from django.shortcuts import render
from os.path import join
from django.http import HttpRequest, HttpResponseRedirect
from django.contrib import messages
from .forms import ContactForm
# Create your views here.


def home_view(request: HttpRequest):
    return render(request, "index.html")


def about_view(request: HttpRequest):
    return render(request, "about.html")


def contact_view(request: HttpRequest):
    if request.POST:
        form = ContactForm(data=request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.name = "unknown"
            new_form.save()
            messages.add_message(request=request, level=messages.SUCCESS, message="Message sent successfully")
            return HttpResponseRedirect("/contact")
        else:
            messages.add_message(request=request, level=messages.ERROR, message="Sending message failed")
            return HttpResponseRedirect("/")
    else:
        form = ContactForm()
    return render(request, "contact.html", context={"form": form})
