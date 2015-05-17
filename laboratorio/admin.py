from django.contrib import admin
from .models import laboratorio
# Register your models here.
class Adminlaboratorio(admin.ModelAdmin):
	list_display = ('nombre','cuidad')

admin.site.register(laboratorio,Adminlaboratorio)
