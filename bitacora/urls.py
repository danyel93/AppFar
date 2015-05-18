from django.conf.urls import patterns, include, url
from .views import ReportarB


urlpatterns = patterns('',
    
    url(r'^reportar_bit/$' , ReportarB.as_view() , name="reportar_bit"),
    
    # url(r'^delete/(?P<pk>\d+)$', EliminarCliente.as_view(), name="borrado"),
    # url(r'^borrarcliente/(?P<id_cliente>\d+)$', 'cliente.views.borrar_cliente'),
    
      

)