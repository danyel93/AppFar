from django.shortcuts import render
from .forms import UserForm
from .models import Perfiles
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView,FormView

# Create your views here.
class Registrarse(FormView):
	template_name = 'principal/registrarse.html'
	form_class = UserForm
	success_url = reverse_lazy('login')


	def form_valid(self, form):
		user = form.save()
		perfil = Perfiles()
		perfil.usuario= user
		perfil.cuidad= form.cleaned_data['cuidad']
		perfil.calle= form.cleaned_data['calle']
		perfil.colonia= form.cleaned_data['colonia']
		perfil.telefono= form.cleaned_data['telefono']
		perfil.save()
		return super(Registrarse , self).form_valid(form)
	
	