from django.db import models

class cliente(models.Model):
	nombre=models.CharField(max_length=50)
	cuidad=models.CharField(max_length=50)
	calle=models.CharField(max_length=50)
	colonia=models.CharField(max_length=50)
	telefono=models.CharField(max_length=50)
	rfc=models.CharField(max_length=50)
	correo=models.EmailField(max_length=50)

	def __unicode__(self):
		return self.nombre

# Create your models here.
