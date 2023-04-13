from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

urlpatterns = []

# View set
router = DefaultRouter()
router.register(r'profession', ProfessionViewSet)
router.register(r'singer', SingerViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'country', CountryViewSet)
router.register(r'song', SongViewSet)
urlpatterns += router.urls
