from django.urls import path
from .views import CadastrarUsuarioView

urlpatterns = [
    path('cadastrar/', CadastrarUsuarioView.as_view(), name="cadastrar"),
]