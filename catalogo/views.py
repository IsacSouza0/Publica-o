from django.shortcuts import render
from catalogo.models import Filme


# Create your views here.

def catalogo_view(request):
    filmes = Filme.objects.all()


    contexto = {
        'filmes': filmes
    }
    return render(requets,'catalogo.html', contexto)