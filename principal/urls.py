from django.conf.urls import patterns, include, url
from .views import Registrarse

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'AppFar.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    ##url(r'^$',Principal.as_view()),  

   url(r'^$' , 'django.contrib.auth.views.login',
		{'template_name':'principal/index.html'}, name='login'),

  	url(r'^cerrar/$' , 'django.contrib.auth.views.logout_then_login',
		 name='logout'),

  	url(r'^registrarse/$', Registrarse.as_view() , name = 'registrarse')
)
