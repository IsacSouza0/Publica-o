from django.db import models

# Create your models here.


class Filme(models.Model):
    genero_acao = 'ac'
    genero_ficcao = 'fc'
    genero_terror = 'tr'
    genero_aventura = 'av'
    genero_comedia = 'cm'
    genero_drama= 'dr'
    genero_romance = 'ro'
    genero_opcoes = [
        (genero_acao,'Ação'),
        (genero_aventura, 'Aventura'),
        (genero_ficcao, 'Ficção'),
        (genero_terror, 'Terror'),
        (genero_comedia,'Comedia'),
        (genero_drama, 'Drama'),
        (genero_romance, 'Roamance'),
    ]

    nome = models.CharField(max_length=120)
    genero = models.CharField(max_length=2, choices=genero_opcoes, default=None)
    sinopse = models.TextField()
    lancamento = models.DateField()
    duracao = models.PositiveIntegerField()
    classificacao_indicativa = models.PositiveIntegerField()
    carta = models.ImageField(upload_to='media')

    def __stf__(self):
        return self.nome