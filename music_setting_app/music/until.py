import os.path

from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from mutagen.mp3 import MP3

MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB
ALLOWED_EXTENSIONS = ['.jpeg', '.jpg', 'png', '.gif']


def is_allowed_file(filename):
    _, ext = os.path.splitext(filename)
    return ext.lower() in ALLOWED_EXTENSIONS


def upload_file_image(files):
    fs = FileSystemStorage('media/image')
    filename = fs.save(files.name, files)
    uploaded_file_url = f'/api/{fs.base_location}/{filename}'

    return {
        'filename': files.name,
        'type': files.content_type,
        'size': files.size,
        'path': uploaded_file_url
    }


def upload_file_mp3(instance, files):
    fs = FileSystemStorage('media/songs')
    filename = fs.save(files.name, files)
    uploaded_file_url = f'/api/{fs.base_location}/{filename}'
    duration = MP3(fs.path(filename)).info.length

    return {
        'filename': files.name,
        'type': files.content_type,
        'size': files.size,
        'duration': duration,
        'path': uploaded_file_url
    }


@csrf_exempt
@permission_classes([AllowAny])
def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        response = None
        files = request.FILES['file']

        if files.size > MAX_FILE_SIZE:
            raise ValueError("File size is to large.")

        if files.name.endswith('.mp3'):
            response = upload_file_mp3(files)
        elif is_allowed_file(files.name):
            response = upload_file_image(files)

        if response:
            return JsonResponse(response, status=200)
        else:
            return JsonResponse({'error': 'Unsupported file type.'}, status=400)

    return JsonResponse({'error': 'Bad request'}, status=400)
