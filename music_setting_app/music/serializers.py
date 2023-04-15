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
        fields = '__all__'

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        professions = instance.professions.all()
        ret['professions'] = [{'id': profession.id, 'name': profession.name} for profession in professions]
        if instance.avatar:
            ret['avatar'] = '/api' + instance.avatar.url
        return ret


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CountrySerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class SongSerializer(ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'
