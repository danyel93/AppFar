from django.db import models

# Create your models here.
class infobit(models.Model):
	operacion=models.CharField(max_length=50)
	fecha=models.DateField()
	