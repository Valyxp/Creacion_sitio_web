import uuid
from django.db import models


class Flan(models.Model):
    flan_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=64)
    description = models.TextField()
    image_url = models.URLField()
    slug = models.SlugField()
    is_private = models.BooleanField(default=False)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True
    )
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=64)
    message = models.TextField()

    def __str__(self):
        return self.customer_name


class Testimonio(models.Model):
    nombre_cliente = models.CharField(max_length=100)
    texto_testimonio = models.TextField()
    fecha_creacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Testimonio de {self.nombre_cliente}"
