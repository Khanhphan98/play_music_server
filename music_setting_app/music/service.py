from .models import Song, Singer
from django.http import JsonResponse


def get_list_song(request):
    try:
        # Sắp xếp các bản ghi theo thời gian tạo
        list_recent = Song.objects.order_by('-created_at')
        # Chỉ lấy các trường cần thiết
        data = list_recent.values()
        # Return
        return JsonResponse({'data': list(data)}, status=200)
    except Exception as e:
        # Return
        return JsonResponse({'sucess': False, 'error': str(e)})


def get_list_singer(request):
    try:
        # Sắp xếp các bản ghi theo thời gian tạo
        list_recent = Singer.objects.all()
        # Chỉ lấy các trường cần thiết
        data = list_recent.values()
        # Return
        return JsonResponse({'data': list(data)}, status=200)
    except Exception as e:
        # Return
        return JsonResponse({'sucess': False, 'error': str(e)})