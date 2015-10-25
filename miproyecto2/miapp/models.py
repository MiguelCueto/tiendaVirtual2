from django.db import models

# Create your models here.
class Articulo(models.Model):
	TIPO_CHOICES =(
	('N','Nuevo'),
	('U','Usado'),
	)
	nombre=models.CharField(max_length=50)
	fecha=models.DateField()
	precio=models.FloatField()
	tipo=models.CharField(max_length=1, choices=TIPO_CHOICES)



