from .models import Song, Singer
from django.http import JsonResponse


def get_list_song(request):
    try:
        # Sắp xếp các bản ghi theo thời gian tạo
        list_recent = Song.objects.order_by('-created_at').prefetch_related('categories', 'countries', 'singers')

        songs = []
        for song in list_recent:
            song_dict = {
                'name': song.name,
                'release': song.release,
                'time': song.time,
                'file_mp3': song.file_mp3,
                'lyric': song.lyric,
                'picture': song.picture,
                'description': song.description,
                'categories': [category.name for category in song.categories.all()],
                'countries': [country.name for country in song.countries.all()],
                'singers': [singer.name for singer in song.singers.all()],
                'created_at': song.created_at,
                'updated_at': song.updated_at,
            }
            songs.append(song_dict)

        # Return
        return JsonResponse({'data': songs}, status=200)

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
