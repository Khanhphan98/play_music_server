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

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        # Query category
        categories = instance.categories.all()
        ret['categories'] = [{'id': category.id, 'name': category.name} for category in categories]
        # Query Country
        countries = instance.countries.all()
        ret['countries'] = [{'id': country.id, 'name': country.name} for country in countries]
        # Query Singer
        singers = instance.singers.all()
        ret['singers'] = [{'id': singer.id, 'name': singer.name} for singer in singers]

        return ret


