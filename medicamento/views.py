from django.shortcuts import render
from .models import medicamento
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy

# Create your views here.
class RegistrarMedicamento(CreateView):
	template_name ='medicamento/registrar_med.html'
	model = medicamento
	success_url = reverse_lazy('login')