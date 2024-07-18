from django.urls import path, include
from MyProject.views import *
from Applic.views import *
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', Home, name='home'),
    path('acerca/', Acerca, name='acerca'),
    path('contacto/', Contacto, name='contacto'),

    path('form/', Form, name='form'),

    
    path('actualizacion/client/<int:id_data>/', Actualizacion, {'model_type': 'client'}, name='actualizacion-cliente'),
    path('actualizacion/market/<int:id_data>/', Actualizacion, {'model_type': 'market'}, name='actualizacion-mercado'),
    path('actualizacion/worker/<int:id_data>/', Actualizacion, {'model_type': 'worker'}, name='actualizacion-trabajador'),
    path('eliminacion/client/<int:id_data>/', Eliminacion, {'model_type': 'client'}, name='eliminacion-cliente'),
    path('eliminacion/market/<int:id_data>/', Eliminacion, {'model_type': 'market'}, name='eliminacion-mercado'),
    path('eliminacion/worker/<int:id_data>/', Eliminacion, {'model_type': 'worker'}, name='eliminacion-trabajador'),

    path('search/', Search, name='search'),
    path('find/', Find, name='Find'),


    path('login/', Loguear, name='login'),
    path('logout/', LogoutView.as_view(template_name='Applic/logout.html'), name='logout'),
    path('registro/', Registracion, name='registro'),
]

