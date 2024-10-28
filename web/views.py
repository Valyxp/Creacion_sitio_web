from django.shortcuts import render
from .models import Flan
from django.http import HttpResponseRedirect
from .forms import ContactFormForm
from .models import ContactForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


def index(request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    return render(request, "index.html", {"flanes": flanes_publicos})


def about(request):
    return render(request, "about.html")


@login_required
def welcome(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    return render(request, "welcome.html", {"flanes": flanes_privados})


def contacto(request):
    if request.method == "POST":
        form = ContactFormForm(request.POST)
        if form.is_valid():
            # Crear un nuevo registro en la base de datos usando form.cleaned_data
            ContactForm.objects.create(
                customer_email=form.cleaned_data["customer_email"],
                customer_name=form.cleaned_data["customer_name"],
                message=form.cleaned_data["message"],
            )
            # Redirigir a la página de éxito tras el envío exitoso del formulario
            return HttpResponseRedirect("/exito/")
    else:
        form = ContactFormForm()

    return render(request, "contactus.html", {"form": form})


def exito(request):
    return render(request, "exito.html")


def flan_detail(request, id):
    flan = get_object_or_404(Flan, id=id)
    return render(request, "flan_detail.html", {"flan": flan})
