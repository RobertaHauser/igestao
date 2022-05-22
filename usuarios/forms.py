from django import forms
from django.core.validators import MinLengthValidator

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

    def clean(self):

        super().clean()

        senha = self.cleaned_data.get("senha")
        confirmacao_senha = self.cleaned_data.get("confirmacao_senha")

        if senha and confirmacao_senha and senha != confirmacao_senha:
            self.add_error("confirmacao_senha", "A confirmação de senha não confere.")
        
        return self.cleaned_data
