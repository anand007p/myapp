from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import item
from .serializers import *


class Userviewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    # serializer_class = UserSerializer

