from django.db import models
from laboratorio.models import laboratorio
from PIL import Image
# Create your models here.
class medicamento(models.Model):
	ESTADOST =((1,"Adulto"),(2,"Infatil"))
	ESTADOSP =((1,"Tabletas"),(2,"Jarabe"),(3,"Pomada"))
	#Atributos
	nombre=models.CharField(max_length=50)
	tipo=models.IntegerField(choices=ESTADOST,default=2)
	presentacion=models.IntegerField(choices=ESTADOSP,default=3)
	precio=models.CharField(max_length=50)
	imagen=models.ImageField(upload_to='Imagenes')
	caducidad=models.DateField(auto_now=False)
	laboratorio=models.ForeignKey(laboratorio)
