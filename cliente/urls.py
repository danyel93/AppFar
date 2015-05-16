from django.conf.urls import patterns, include, url
from .views import RegistrarCliente, ReportarCliente,EditarCliente,EliminarCliente


urlpatterns = patterns('',
    
    url(r'^registrar_cli/$' , RegistrarCliente.as_view() , name="registrar_cli"),
    url(r'^reportar_cli/$' , ReportarCliente.as_view() , name="reportar_cli"),
    url(r'^editar_cli/(?P<pk>\d+)$' , EditarCliente.as_view() , name="editar_cli"),
    url(r'^eliminar_cli/(?P<pk>\d+)$' , EliminarCliente.as_view() , name="eliminar_cli"),
    
    # url(r'^delete/(?P<pk>\d+)$', EliminarCliente.as_view(), name="borrado"),
    # url(r'^borrarcliente/(?P<id_cliente>\d+)$', 'cliente.views.borrar_cliente'),
    
      

)