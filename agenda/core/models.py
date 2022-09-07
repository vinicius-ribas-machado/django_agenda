import datetime
from django.contrib.auth.models import User
from django.db import models
from datetime import datetime, timedelta

# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True,null=True)
    data_evento = models.DateTimeField(verbose_name='Data do evento')
    data_criacao = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)


    class meta:
        db_table = 'evento'

    def __str__(self):
        return self.titulo

    def get_data_evento (self):
        return self.data_evento.strftime('%d/%m/%y %H:%M Hrs')

    def get_data_input_evento(self):
        return self.data_evento.strftime('%y-%m-%dT %H:%M')

    def get_evento_atrasado(selfself):
        if self.data_evento < datetime.now():
            return True
        else:
            return False


