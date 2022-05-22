from django.urls import path
from .views import LoginView, CadastrarUsuarioView

urlpatterns = [
    path('cadastrar/', CadastrarUsuarioView.as_view(), name="cadastrar"),
    path('login/', LoginView.as_view(), name="login"),
]