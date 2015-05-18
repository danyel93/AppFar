from django.db import models

# Create your models here.
class informe(models.Model):
	operacion=models.CharField(max_length=1)
	fecha=models.DateField(auto_now=True)
	usuario=models.CharField(max_length=50)
	campo=models.CharField(max_length=50)
	atributo=models.CharField(max_length=50)

def __unicode__(self):
	return self.nombre