from django.shortcuts import render
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from .models import ventas

# Create your views here.
class RegistrarVenta(CreateView):
	template_name ='ventas/registrar_vta.html'
	model = ventas
	fields = ['fecha','medicamentos','total','cliente','vendedor',]
	success_url = reverse_lazy('login')

