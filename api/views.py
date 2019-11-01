from django.shortcuts import render
from rest_framework import viewsets
from .models import Movie
from .serializers import movieSerializer


class movies(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = movieSerializer
