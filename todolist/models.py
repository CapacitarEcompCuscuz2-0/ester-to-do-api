from django.db import models

# dados e formatos dos dados da API
class Tarefa(models.Model):
    
    # define uma sobrescrita para os valores padrão do BooleanField
    CHOICES = [(True, 'Sim'), (False, 'Não')]

    name = models.CharField(verbose_name="Nome", max_length=255)
    status = models.BooleanField(verbose_name="Concluído", default=False, choices=CHOICES)
    creation_date = models.DateField(verbose_name="Data de criação", auto_now_add=True)