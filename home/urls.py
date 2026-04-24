from django.urls import path
from .views import projeto_detalhe
from . import views

urlpatterns = [
    path('', views.lista_projetos),
    path('projeto/<int:projeto_id>/', projeto_detalhe, name='projeto_detalhe'),
]