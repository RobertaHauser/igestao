from django.db import models
from django.conf import settings

# Create your models here.
class Unidade(models.Model):
    nome = models.CharField(max_length=30, unique=True, verbose_name='Unidade', help_text="Não utilizar espaço")
    sigla = models.CharField(max_length=3, unique=True, verbose_name='Sigla', help_text="03 letras")
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='+', verbose_name='Cadastro')
    created_at= models.DateTimeField(auto_now_add=True, verbose_name='Data cadastro')
    edit_by= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='+', verbose_name='Revisão')
    edit_at= models.DateTimeField(auto_now=True, verbose_name='Data revisão')

    class Meta:
        verbose_name="Unidade"
        verbose_name_plural="Unidades"
        db_table="unidade"
    
    def __str__(self):
       	return self.unidade_nome
