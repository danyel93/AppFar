from django.conf.urls import patterns, include, url
from .views import RegistrarVenta

urlpatterns = patterns('',
    
   url(r'^registrar_vta/$' , RegistrarVenta.as_view() , name="registrar_vta"),
  # url(r'^reportar_med/$' , ReportarMedicamento.as_view() , name="reportar_med"),
    #zzzurl(r'^reportar_lab/$' , ReportarL.as_view() , name="reportar_lab"),
    #url(r'^reportar_cli/$' , ReportarCliente.as_view() , name="reportar_cli"),
     #url(r'^borrarcliente/(?P<id_cliente>\d+)$', 'cliente.views.borrar_cliente'),
    

)