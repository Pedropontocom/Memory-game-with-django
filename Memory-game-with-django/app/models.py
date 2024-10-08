from django.db import models

class Player(models.Model):
  nome_jogador = models.CharField(max_length=100)
  tentativas = models.IntegerField()
  tempo = models.IntegerField(null=True, blank=True)
  data_hora = models.DateTimeField(auto_now_add=True)
