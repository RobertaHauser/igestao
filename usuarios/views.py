from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib import messages

from usuarios.forms import RegistrarUsuarioForm

class CadastrarUsuarioView(FormView):
    template_name = "cadastrar.html"
    form_class = RegistrarUsuarioForm
    success_url = reverse_lazy("cadastrar")

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, "Cadastro realizado com sucesso.")
        # Enviar email
        return super().form_valid(form)
