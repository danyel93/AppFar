from django.db import models

# Create your models here.
class laboratorio(models.Model):
	nombre=models.CharField(max_length=50)
	cuidad=models.CharField(max_length=50)
	calle=models.CharField(max_length=50)
	colonia=models.CharField(max_length=50)
	rfc=models.CharField(max_length=50)

	def __unicode__(self):
		return self.nombre
