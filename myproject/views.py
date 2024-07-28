from django.shortcuts import render


def maintenance(request):
    return render(request, "503.html")
