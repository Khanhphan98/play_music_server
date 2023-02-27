from rest_framework.serializers import ModelSerializer
from .models import *


class ProfessionSerializer(ModelSerializer):
    class Meta:
        model = Profession
        fields = '__all__'
        # exclude = ['name']
