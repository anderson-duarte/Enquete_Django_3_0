from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta


# Create your models here.

class Questao(models.Model):
    texto_questao = models.CharField(max_length=200)
    data_publicacao = models.DateTimeField('Data Publicação')

    def __str__(self):
        return self.texto_questao

    def questao_recente(self):
        return  self.data_publicacao >= timezone.now() - timedelta(days=1)

class Opcao(models.Model):
    questao = models.ForeignKey(Questao, on_delete=models.CASCADE)
    texto_opcao = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)

    def __str__(self):
        return self.texto_opcao

