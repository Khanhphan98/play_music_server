from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from mutagen.mp3 import MP3


def upload_avatar_path(instance, filename):
    return 'avatar/{filename}'.format(filename=filename)


def upload_file_path(instance, filename):
    return 'songs/{filename}'.format(filename=filename)


@csrf_exempt
@permission_classes([AllowAny])
def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        files = request.FILES['file']
        fs = FileSystemStorage('media/avatar')
        filename = fs.save(files.name, files)
        uploaded_file_url = f'/api/{fs.base_location}/{filename}'

        # Attach file size and type
        duration = None
        if files.name.endswith('.mp3'):
            duration = MP3(fs.path(filename)).info.length

        response = {
            'filename': files.name,
            'type': files.content_type,
            'size': files.size,
            'duration': duration,
            'path': uploaded_file_url
        }

        return JsonResponse(response, status=200)

    return JsonResponse({'error': 'Bad request'}, status=400)
