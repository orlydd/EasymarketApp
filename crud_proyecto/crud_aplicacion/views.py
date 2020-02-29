from django.shortcuts import render
from rest_framework import viewsets
from .models import ciudad
from .serializers import ciudadSerializer

class ciudadView(viewsets.ModelViewSet):
    queryset = ciudad.objects.all()
    serializer_class = ciudadSerializer
