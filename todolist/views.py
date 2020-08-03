from django.shortcuts import render
from todolist.models import Tarefa
from todolist.serializers import TarefaSerializer
from rest_framework import viewsets
from rest_framework import generics

# conjunto de rotinas de manipulação do model, como criar, exibir; métodos get, post, etc
class TarefaViewSet(viewsets.ModelViewSet):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer

# visualização de todos os elementos do banco de dados em lista na interface, difere do
# anterior pois apenas exibia o último dado adicionado
class TarefaList(generics.ListCreateAPIView):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer

# adiciona a interface da aplicação as rotinas get, post, delete, update
class TarefaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer