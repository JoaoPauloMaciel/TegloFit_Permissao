from django.http import HttpResponse
from .serializers import UserSerializer, GroupSerializer, PesagemSerializer
from balanca.models import Pesagem
from django.shortcuts import render
from rest_framework import viewsets, generics
from django.contrib.auth.models import User, Group
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
#
from rest_framework.decorators import detail_route
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PesagemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Pesagem.objects.all()
    serializer_class = PesagemSerializer


def index(request):
    return HttpResponse("Hello, world. Essa é a view da balança!")

