from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'AppFar.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # pagina principal
    url(r'^',include('principal.urls')),
    # url de la aplicacion cliente
    url(r'^cliente/' , include('cliente.urls')),
    # url de la aplicacion laboratorio
    url(r'^laboratorio/' , include('laboratorio.urls')),
    # url de la aplicacion medicamento
    url(r'^medicamento/' , include('medicamento.urls')),
    # url de imagenes
    url(r'Imagenes/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT, } ),
    
   
)
