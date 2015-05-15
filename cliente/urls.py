from django.conf.urls import patterns, include, url
from .views import RegistrarCliente, ReportarCliente


urlpatterns = patterns('',
    
    url(r'^registrar_cli/$' , RegistrarCliente.as_view() , name="registrar_cli"),
     url(r'^reportar_cli/$' , ReportarCliente.as_view() , name="reportar_cli"),
      

)