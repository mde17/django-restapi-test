from django.shortcuts import render

from rest_framework import viewsets
from .serializers import MovieSerializer
from .models import Movie

# Create your views here.

class MovieViewset(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer