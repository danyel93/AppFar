from django.db import models
from medicamento.models import medicamento
from django.contrib.auth.models import User
from cliente.models import cliente
# Create your models here.

class ventas(models.Model):
	fecha=models.DateTimeField('fecha de venta')
	medicamentos=models.ManyToManyField(medicamento)
	total=models.PositiveIntegerField()
	cliente=models.ForeignKey(cliente)
	vendedor= models.ForeignKey(User)

	def __unicode__(self):
		return self.vendedor
	
