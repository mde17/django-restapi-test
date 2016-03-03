from django.shortcuts import render

from rest_framework import viewsets, filters, generics
from rest_framework.response import Response
from ..serializers import MovieSerializer
from ..models import Movie
from rest_framework.decorators import list_route
from app_utils import error_handler

# Create your views here.

class MovieViewset(viewsets.ModelViewSet):
#class MovieViewset(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title',)
    lookup_field = 'id'

#    def perform_create(self, serializer):
#        print 'performing create'
##        print self.request.data['title']
#        serializer.save(title='test1')

#    def create():

#    def list(self, request):
#        queryset = self.get_queryset()
#        serializer = MovieSerializer(queryset, many=True)
#        return Response(serializer.data, status=200)
#    
#    @list_route()
#    def get_deadpool(self, request):
#        queryset = Movie.objects.filter(title__contains='Deadpool2')
#        serializer = self.serializer_class(queryset, many=True)
#        return Response(serializer.data, status=200)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = MovieSerializer(instance)

        return error_handler.render_error(error_handler.AUTH)

#        return Response(serializer.data, status=201)