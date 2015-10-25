from django.shortcuts import render
from miapp.models import Articulo
# Create your views here.

def indice(request):
   lista_articulos = Articulo.objects.all()
   return render(request, 'index.html', {'lista_articulos': lista_articulos })
