from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
#class MovieSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
#        id = serializers.HyperlinkedIdentityField(view_name='movie-detail', format='html')
        
        model = Movie
        fields = ('title', 'synopsis', 'status',)
#        fields = ('url', 'id', 'title', 'synopsis')
    

#    def create(self, validated_data):
#        print 'creating'
#        validated_data['title'] = 'test2'
#        return Movie.objects.create(**validated_data)