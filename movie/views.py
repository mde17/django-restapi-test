from django.shortcuts import render

from rest_framework import viewsets, filters, generics
from rest_framework.response import Response
from .serializers import MovieSerializer
from .models import Movie
from rest_framework.decorators import list_route

# Create your views here.

class MovieViewset(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title',)

#    def perform_create(self, serializer):
#        print 'performing create'
##        print self.request.data['title']
#        serializer.save(title='test1')

#    def create():

#    def list(self, request):
#        queryset = self.queryset
#        serializer = self.serializer_class(queryset, many=True)
#        return Response(serializer.data, status=200)
    
    @list_route()
    def get_deadpool(self, request):
        queryset = Movie.objects.filter(title__contains='Deadpool2')
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=200)