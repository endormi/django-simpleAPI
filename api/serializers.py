from rest_framework import serializers
from .models import Movie


class movieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'name', 'description', 'category', 'director', 'based_on', 'main_actor', 'release_date')

