import imp
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.views.generic.list import ListView
from .models import Unidade
from django.urls import reverse_lazy
#from urllib import request

# Create your views here.

#### CREATE

class UnidadeCreate(CreateView):
	model=Unidade
	fields=['nome','sigla']
	#Unidade.created_by = request.user
	template_name='form.html'
	sucess_url=reverse_lazy('usuarios/home')

def post(request, *args, **kwargs):
    print(self.request)



#### UPDATE

class UnidadeUpdate(UpdateView):
	model=Unidade
	fields=['nome','sigla']
	template_name='form.html'
	sucess_url=reverse_lazy('usuarios/home')


#### DELETE

class UnidadeDelete(DeleteView):
	model=Unidade
	template_name='form-excluir.html'
	sucess_url=reverse_lazy('usuarios/home')


#### LIST
class UnidadeList(ListView):
	model=Unidade
	template_name='cadastro-read.html'
