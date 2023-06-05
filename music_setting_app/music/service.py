import json
from .models import Song, Singer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import F


def convertDataSong(data):
    try:
        songs = []
        for song in data:
            song_dict = {
                'id': song.id,
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
                'statistik': {
                    'id': song.statistikID,
                    'song_play_count': song.song_play_count
                },
            }
            songs.append(song_dict)

        # Return
        return songs
    except Exception as e:
        # Return
        return JsonResponse({'sucess': False, 'error': str(e)})


@csrf_exempt
def get_list_song(request):
    try:
        # GET id singer
        song_id = json.loads(request.body)['id']
        if song_id:
            # Sắp xếp các bản ghi theo thời gian tạo
            list_recent = Song.objects.filter(id=song_id).order_by('-created_at') \
                .prefetch_related('categories', 'countries', 'singers') \
                .annotate(song_play_count=F('statistik__song_play_count'), statistikID=F('statistik__id'))
        else:
            # Sắp xếp các bản ghi theo thời gian tạo
            list_recent = Song.objects.all().order_by('-created_at') \
                .prefetch_related('categories', 'countries', 'singers') \
                .annotate(song_play_count=F('statistik__song_play_count'), statistikID=F('statistik__id'))

        songs = convertDataSong(list_recent)

        # Return
        return JsonResponse({'data': songs}, status=200)

    except Exception as e:
        # Return
        return JsonResponse({'sucess': False, 'error': str(e)})


@csrf_exempt
def get_list_singer(request):
    try:
        # GET id singer
        singer_id = json.loads(request.body)['id']
        if singer_id:
            # Sắp xếp các bản ghi theo thời gian tạo
            list_recent = Singer.objects.filter(id=singer_id).prefetch_related('professions') \
                .annotate(singer_play_count=F('statistik__singer_play_count'), statistikID=F('statistik__id'))
        else:
            # Sắp xếp các bản ghi theo thời gian tạo
            list_recent = Singer.objects.all().prefetch_related('professions') \
                .annotate(singer_play_count=F('statistik__singer_play_count'), statistikID=F('statistik__id'))

        # Chỉ lấy các trường cần thiết
        singers = []
        for singer in list_recent:
            singer_dict = {
                'id': singer.id,
                'name': singer.name,
                'birthday': singer.birthday,
                'address': singer.address,
                'avatar': singer.avatar,
                'description': singer.description,
                'professions': [profession.name for profession in singer.professions.all()],
                'statistik': {
                    'id': singer.statistikID,
                    'singer_play_count': singer.singer_play_count
                },
            }
            singers.append(singer_dict)

        # Return
        return JsonResponse({'data': singers}, status=200)
    except Exception as e:
        # Return
        return JsonResponse({'sucess': False, 'error': str(e)})


@csrf_exempt
def get_list_song_by_country(request):
    try:
        # GET id country by song
        country_ids = json.loads(request.body)['country_ids']
        # Get Song
        songs_in_country = Song.objects.filter(countries__id__in=country_ids) \
            .annotate(song_play_count=F('statistik__song_play_count'), statistikID=F('statistik__id'))

        data = convertDataSong(songs_in_country)

        # Return
        return JsonResponse({'data': data}, status=200)
    except Exception as e:
        # Return
        return JsonResponse({'sucess': False, 'error': str(e)})


@csrf_exempt
def get_list_song_by_exclude_country(request):
    try:
        # GET id country by song
        country_ids = json.loads(request.body)['country_ids']
        # Lay ra cac bai hat tru hai bai hat o hai quoc gia nay
        songs_exclude_country = Song.objects.exclude(countries__id__in=country_ids) \
            .annotate(song_play_count=F('statistik__song_play_count'), statistikID=F('statistik__id'))

        data = convertDataSong(songs_exclude_country)

        # Return
        return JsonResponse({'data': data}, status=200)
    except Exception as e:
        # Return
        return JsonResponse({'sucess': False, 'error': str(e)})


def get_singer_with_statistik(request):
    qs = Singer.objects.annotate(
        singer_play_count=F('statistik__singer_play_count'),
    ).values('name', 'birthday', 'address', 'professions', 'description', 'avatar', 'singer_play_count')

    singers = [
        {
            'name': item['name'],
            'singer_play_count': item['singer_play_count'],
        }
        for item in qs
    ]

    # Return
    return JsonResponse({'data': singers}, status=200)


def get_song_with_statistik(request):
    qs = Song.objects.annotate(
        song_play_count=F('statistik__song_play_count'),
    ).values('name', 'release', 'time', 'file_mp3', 'categories', 'countries', 'singers', 'picture', 'song_play_count')

    songs = [
        {
            'name': item['name'],
            'release': item['release'],
            'time': item['time'],
            'file_mp3': item['file_mp3'],
            'categories': item['categories'],
            'countries': item['countries'],
            'singers': item['singers'],
            'song_play_count': item['song_play_count'],
        }
        for item in qs
    ]

    # Return
    return JsonResponse({'data': songs}, status=200)


@csrf_exempt
def get_list_songs_by_singer(request, singer_id):
    try:
        # GET id country by song
        # Lay ra cac bai hat tru hai bai hat o hai quoc gia nay
        songs_by_singer = Song.objects.filter(singers__id=singer_id) \
            .annotate(song_play_count=F('statistik__song_play_count'), statistikID=F('statistik__id'))

        songs = convertDataSong(songs_by_singer)

        singer = Singer.objects.get(id=singer_id)

        singer_data = {
            'id': singer.id,
            'name': singer.name,
            'birthday': singer.birthday.strftime('%Y-%m-%d'),
            'address': singer.address,
            'description': singer.description,
            'avatar': singer.avatar,
        }

        # Return
        return JsonResponse({'data': { 'songs': songs, 'singer': singer_data }}, status=200)
    except Exception as e:
        # Return
        return JsonResponse({'sucess': False, 'error': str(e)})
