from django.db import models

# Create your models here.
class ArticulosNuevos(models.Model)
	nombre=models.CharField(max_length=200)
	precio=models.FloatField()
	fecha=models.DateField()


class ArticulosUsados(models.Model)
	nombre=models.CharField(max_length=200)
	precio=models.FloatField()
	fecha=models.DateField()
