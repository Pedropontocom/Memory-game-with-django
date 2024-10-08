from django.shortcuts import redirect, render
from .models import Player

def index(request):
  return render(request, 'index.html')

def indexTelaNome(request):
  return render(request, 'indexTelaNome.html')

def indexTelaGame(request):
  return render(request, 'indexTelaGame.html')

def add(request):
  x=request.POST['nome_jogador']
  y=request.POST['tentativas']
  z=request.POST['tempo']
  player=Player(nome_jogador=x, tentativas=y, tempo=z)
  player.save()
  return redirect("/")
  
def indexTelaOpicoes(request):
  return render(request, 'indexTelaOpicoes.html')

def indexTelaRanking(request):
  player=Player.objects.all().order_by("tentativas", "tempo").values()
  return render(request, 'indexTelaRanking.html', {'player':player})