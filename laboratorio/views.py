from django.shortcuts import render
from django.views.generic import CreateView,ListView
from .models import laboratorio
from django.core.urlresolvers import reverse_lazy

# Create your views here.
class RegistrarL(CreateView):
	template_name ='laboratorio/registro_lab.html'
	model = laboratorio
	success_url = reverse_lazy('login')


class ReportarL(ListView):
	template_name = 'laboratorio/reportar_lab.html'
	model = laboratorio
	context_object_name = 'laboratorios'
