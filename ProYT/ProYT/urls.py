"""ProYT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#from ProYT.views import Principal, Comenter, FexaDoy, Calculef
from ProYT.views import Principal

urlpatterns = [
    path('admin/', admin.site.urls),  # Url propiciada por Django
    path('Home/', Principal),  # Url con el menu para elegir que hacer
    #path('CajCome/', Comenter),
    #path('Fexa/', FexaDoy), # Contenido cambiante en cada actualizacion
    #path("An/<int:agno>", Calculef), #Vamos a pasar por la URL un parametro
]


# El proposito de este proyecto es que Melo (Mi novia) escriba en una caja de texto cualquier queja que tenga en
# relacion a la experiencia de noviazgo conmigo, el comentario se envia a mi mail y de esa manera podre tomar medidas
