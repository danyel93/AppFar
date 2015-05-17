from django.contrib import admin
from .models import medicamento
# Register your models here.
class AdminMedicamento(admin.ModelAdmin):
	list_display = ('nombre','laboratorio')

admin.site.register(medicamento,AdminMedicamento)

