from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models
from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets


class Pesagem(models.Model):
    owner = models.ForeignKey('auth.User', related_name='pesagem', on_delete=models.CASCADE, null=True)
    peso = models.FloatField('peso', max_length=6)
    dataEHoraDePesagem = models.DateTimeField('dataEHoraDePesagem', default=timezone.now)


class Mensagem(models.Model):
    assunto = models.TextField
    titulo = models.CharField

