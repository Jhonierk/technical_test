from django.shortcuts import render

#El mixin autentica y muestra el usuario
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views import generic
# Create your views here.

#los mixin siempre se heredan a la izq 
class Home(LoginRequiredMixin, generic.TemplateView):
    #hace refertencia a la plantilla que va a mostrar
    template_name = 'bases/home.html'
    #cuando el usuario  que quiera acceder a la vista home y no esta registrado lo redirige
    login_url='bases:login'