from django.views.generic.edit import FormView
from django.views.generic import View
from django.shortcuts import render

from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate, login

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

class LoginView(View):
    template_name = "login.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):

        email = request.POST.get("email")
        senha = request.POST.get("senha")
        
        usuario = authenticate(email=email, password=senha)
        
        if usuario:
            login(request, usuario)

        return render(request, self.template_name)
