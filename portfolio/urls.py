from django.urls import path, include
from .views import home, contacto, gracias

urlpatterns = [
    path('',  home, name="home"),
    path('contacto/', contacto, name="contacto"),
    path('¡Gracias!', gracias, name="gracias")
]