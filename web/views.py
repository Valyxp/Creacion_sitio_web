from django.shortcuts import render
from .models import Flan


def index(request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    return render(request, "index.html", {"flanes": flanes_publicos})


def about(request):
    return render(request, "about.html")


def welcome(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    return render(request, "welcome.html", {"flanes": flanes_privados})
