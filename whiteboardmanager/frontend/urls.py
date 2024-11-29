from django.urls import path
from . import views

urlpatterns = [
    # Agrega aquí las URLs que maneja el frontend
    path('', views.index, name='index'),  # La página de inicio, por ejemplo
]
