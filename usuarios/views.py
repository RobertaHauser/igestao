from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib import messages

from usuarios.forms import RegistrarUsuarioForm

class CadastrarUsuarioView(FormView):
    template_name = "cadastrar.html"
    form_class = RegistrarUsuarioForm
    success_url = reverse_lazy("cadastrar")

    def form_invalid(self, form):
        contexto = {"form": form, "sucesso": False}
        return self.render_to_response(self.get_context_data(**contexto))

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, "Cadastro realizado com sucesso.")
        
        # Registrar usuário
        form.registrar_usuario()        

        # Enviar email

        contexto = {"form": form, "sucesso": True}
        return self.render_to_response(self.get_context_data(**contexto))
