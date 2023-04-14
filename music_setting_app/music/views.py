from rest_framework import viewsets
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser


# Create your views here.
class ProfessionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ProfessionSerializer
    queryset = Profession.objects.all()


class SingerViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = SingerSerializer
    queryset = Singer.objects.all()
    parser_classes = [MultiPartParser, FormParser]


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CountryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CountrySerializer
    queryset = Country.objects.all()


class SongViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = SongSerializer
    queryset = Song.objects.all()
