from rest_framework.serializers import ModelSerializer
from .models import *


class ProfessionSerializer(ModelSerializer):
    class Meta:
        model = Profession
        fields = '__all__'
        # exclude = ['name']


class SingerSerializer(ModelSerializer):
    class Meta:
        model = Singer
        fields = ['id', 'name', 'birthday', 'address', 'professions']
