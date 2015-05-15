from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'AppFar.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^',include('principal.urls')),
    url(r'^cliente/' , include('cliente.urls')),
    url(r'^laboratorio/' , include('laboratorio.urls')),
     url(r'^medicamento/' , include('medicamento.urls')),
     url(r'^borrarcliente/(?P<id_cliente>\d+)$', 'cliente.views.borrar_cliente'),
    
   
)
