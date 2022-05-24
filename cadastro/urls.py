from django.urls import path
from .views import UnidadeCreate, UnidadeUpdate, UnidadeDelete

urlpatterns = [
    #path('endereco/', MinhaView.as_view(), name="nome-da-url"),
    path('unidade/cadastrar/', UnidadeCreate.as_view(), name="cadastrar-unidade"),
    path('unidade/editar/<int:pk>', UnidadeUpdate.as_view(), name="cadastrar-update"),
    path('unidade/excluir/<int:pk>', UnidadeDelete.as_view(), name="cadastrar-delete"),

]