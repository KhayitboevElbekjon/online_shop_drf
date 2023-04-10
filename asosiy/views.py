from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .serializer import *
class BolimAPISerializer(ModelViewSet):
    queryset = Bolim.objects.all()
    serializer_class = BolimSerializer
