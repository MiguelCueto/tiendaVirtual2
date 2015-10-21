from django.db import models

# Create your models here.
class ArticuloNuevo(models.Model):
	nombre=models.CharField(max_length=50)
	fecha=models.DateField()
	precio=models.FloatField()

class ArticuloUsado(models.Model):
	nombre=models.CharField(max_length=50)
	fecha=models.DateField()
	precio=models.FloatField()

