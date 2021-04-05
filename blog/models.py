from django.db import models

# Create your models here.
class Objetos(models.Model):
	producto = models.CharField(max_length=50)
	descripcion = models.CharField(max_length=200)
	precios = models.DecimalField(max_digits=5,decimal_places=2)