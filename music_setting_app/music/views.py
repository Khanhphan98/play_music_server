from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q
from .models import Profession
from .serializers import ProfessionSerializer


# Create your views here.
class ProfessionViewSet(viewsets.ModelViewSet):
    serializer_class = ProfessionSerializer
    queryset = Profession.objects.all()


# class ProfessionView(APIView):
#     @staticmethod
#     def get(self):
#         try:
#             professions = Profession.objects.all()
#             return Response(ProfessionSerializer(professions, many=True).data)
#
#         except Exception as e:
#             return Response({'success': False, 'error': str(e)})
#
#     @staticmethod
#     def post(self, request):
#         try:
#             serializer = ProfessionSerializer(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#             else:
#                 return Response(serializer.errors, status=400)
#
#         except Exception as e:
#             return Response({'success': False, 'error': str(e)})


# @api_view(['POST'])
# def create_profession(request):
#     try:
#         serializer = ProfessionSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'success': True})
#         else:
#             return Response(serializer.errors, status=400)
#
#     except Exception as e:
#         return Response({'success': False, 'error': str(e)})
#
#
# @api_view(['PUT'])
# def update_profession(request, index):
#     try:
#         profession = Profession.objects.get(id=index)
#         serializer = ProfessionSerializer(data=request.data, instance=profession)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'success': True})
#         else:
#             return Response(serializer.errors, status=400)
#
#     except Exception as e:
#         return Response({'success': False, 'error': str(e)})
#
#
# @api_view(['DELETE'])
# def delete_profession(request, index):
#     try:
#         profession = Profession.objects.get(id=index)
#         profession.delete()
#         return Response({'success': True})
#
#     except Exception as e:
#         return Response({'success': False, 'error': str(e)})
#
#
# @api_view(['GET'])
# def get_profession_by_id(request, index):
#     try:
#         profession = Profession.objects.get(id=index)
#         return Response(ProfessionSerializer(profession).data)
#
#     except Exception as e:
#         return Response({'success': False, 'error': str(e)})
#
#
# @api_view(['GET'])
# def search_profession(request):
#     keyword = request.GET.get('keyword', '')
#     professions = Profession.objects.filter(
#         Q(name__icontains=keyword)
#     )
#     return Response(ProfessionSerializer(professions, many=True).data)
