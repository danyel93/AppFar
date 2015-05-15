from django.shortcuts import render
from .models import cliente
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView,TemplateView,ListView
from django.template import RequestContext

# Create your views here.

##clases de registro de usuario
class RegistrarCliente(CreateView):
	template_name = 'cliente/registrar_cliente.html'
	model = cliente
	success_url = reverse_lazy('login')

##clase de muestra de clientes
class ReportarCliente(ListView):
	template_name = 'cliente/reportar_cliente.html'
	model = cliente
	context_object_name = 'clientes'


def borrar_cliente(request, id_cliente):
	cliente = producto.objects.get(pk=cliente)
	cliente.delete()
	return HttpResponseRedirect("/")