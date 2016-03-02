from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):


    class Meta:
        model = Movie
        fields = ('title', 'synopsis', 'status',)


#    def create(self, validated_data):
#        print 'creating'
#        validated_data['title'] = 'test2'
#        return Movie.objects.create(**validated_data)