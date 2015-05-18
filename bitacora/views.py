from django.shortcuts import render
from .models import informe
from django.views.generic import ListView

# Create your views here.

class ReportarB(ListView):
	template_name= 'bitacora/reportar_bit.html'
	model = informe
	context_object_name = 'bits'



