from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.index, name="index"),
    path("acerca/", views.about, name="about"),
    path("bienvenido/", views.welcome, name="welcome"),
    path("contacto/", views.contacto, name="contacto"),
    path("exito/", views.exito, name="exito"),
    path("accounts/login/", auth_views.LoginView.as_view(), name="login"),
    path("accounts/logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("flan/<int:id>/", views.flan_detail, name="flan_detail"),
    path("testimonios/", views.testimonios, name="testimonios"),
]
