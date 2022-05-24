from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import LoginView, CadastrarUsuarioView, home

urlpatterns = [
    #path('endereco/', MinhaView.as_view(), name="nome-da-url"),
    path('index/', home, name='home'),
    path('cadastrar/', CadastrarUsuarioView.as_view(), name="cadastrar"),
    path('', LoginView.as_view(), name="login"),
    path('logout', LogoutView.as_view(), name="logout")
]