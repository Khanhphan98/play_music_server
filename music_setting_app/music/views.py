from rest_framework import viewsets
from .serializers import *
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class ProfessionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ProfessionSerializer
    queryset = Profession.objects.all()


class SingerViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = SingerSerializer
    queryset = Singer.objects.all()
