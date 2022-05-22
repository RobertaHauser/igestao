from django import forms
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User

class RegistrarUsuarioForm(forms.Form):

    nome = forms.CharField(
            max_length=255,
            required=True, 
            widget=forms.TextInput(attrs={'placeholder': 'Nome'})
        )

    sobrenome = forms.CharField(
            max_length=255, 
            required=True,
            widget=forms.TextInput(attrs={'placeholder': 'Sobrenome'})
        )

    email = forms.EmailField(
            required=True,
            widget=forms.TextInput(attrs={'placeholder': 'Email'})
        )

    senha = forms.CharField(
            max_length=255, 
            required=True,
            widget=forms.PasswordInput(attrs={'placeholder': 'Senha'})
        )

    confirmacao_senha = forms.CharField(
            max_length=255, 
            required=True,
            widget=forms.PasswordInput(attrs={'placeholder': 'Confirmação de senha'}),
            validators=[MinLengthValidator(limit_value=6)] 
        )

    def registrar_usuario(self):

        usuario = User(first_name=self.cleaned_data.get("nome"),
                       last_name=self.cleaned_data.get("sobrenome"),
                       email=self.cleaned_data.get("email"))

        usuario.set_password(self.cleaned_data.get("senha"))
        usuario.save()

    def clean(self):

        super().clean()

        senha = self.cleaned_data.get("senha")
        confirmacao_senha = self.cleaned_data.get("confirmacao_senha")

        if senha and confirmacao_senha and senha != confirmacao_senha:
            self.add_error("confirmacao_senha", "A confirmação de senha não confere.")
        
        usuario_por_email = User.objects.filter(email=self.cleaned_data.get("email")).exists()

        if usuario_por_email:
            self.add_error("email", "Já existe um usuário com o email inserido.")

        return self.cleaned_data
