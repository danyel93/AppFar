from django.conf.urls import patterns, include, url
from .views import RegistrarL,ReportarL


urlpatterns = patterns('',
    
    url(r'^registrar_lab/$' , RegistrarL.as_view() , name="registrar_lab"),
    url(r'^reportar_lab/$' , ReportarL.as_view() , name="reportar_lab"),
    #url(r'^reportar_cli/$' , ReportarCliente.as_view() , name="reportar_cli"),
     #url(r'^borrarcliente/(?P<id_cliente>\d+)$', 'cliente.views.borrar_cliente'),
    

)