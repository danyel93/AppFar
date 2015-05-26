from django.shortcuts import render
from django.views.generic import CreateView,ListView,DeleteView,UpdateView
from .models import laboratorio
from django.core.urlresolvers import reverse_lazy

# Create your views here.
class RegistrarL(CreateView):
	template_name ='laboratorio/registro_lab.html'
	model = laboratorio
	fields = ['nombre','cuidad','calle','colonia','rfc',]
	success_url = reverse_lazy('login')


class ReportarL(ListView):
	template_name = 'laboratorio/reportar_lab.html'
	model = laboratorio
	context_object_name = 'laboratorios'

class EditarL(UpdateView):
	template_name= 'laboratorio/editar_lab.html'
	model = laboratorio
	success_url = reverse_lazy('reportar_lab')
class EliminarL(DeleteView):
	template_name='laboratorio/confirmacion.html'
	model = laboratorio
	success_url = reverse_lazy('reportar_lab')
