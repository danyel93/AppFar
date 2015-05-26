from django.shortcuts import render
from .models import medicamento
from django.views.generic import CreateView,ListView
from django.core.urlresolvers import reverse_lazy
from django.template import RequestContext


# Create your views here.
class RegistrarMedicamento(CreateView):
	template_name ='medicamento/registrar_med.html'
	model = medicamento
	fields = ['nombre','tipo','presentacion','precio','imagen','caducidad','laboratorio',]
	success_url = reverse_lazy('login')



class ReportarMedicamento(ListView):
	template_name = 'medicamento/reportar_med.html'
	model = medicamento
	context_object_name = 'meds'