from rest_framework.routers import DefaultRouter
from api import movie

router = DefaultRouter(trailing_slash=False)
router.register(r'movies', movie.MovieViewset)