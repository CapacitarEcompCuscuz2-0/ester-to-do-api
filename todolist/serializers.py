from rest_framework import serializers
from todolist.models import Tarefa

# permite a manipulação dos dados do model associado como arquivos json, por exemplo
class TarefaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarefa
        fields = '__all__'