from django.db import models
from django.contrib.auth.models import User

class Perfiles(models.Model):
	usuario = models.OneToOneField(User)
	cuidad=models.CharField(max_length=50)
	calle=models.CharField(max_length=50)
	colonia=models.CharField(max_length=50)
	telefono = models.CharField(max_length=50)

	def __unicode__(self):
		return self.usuario.username