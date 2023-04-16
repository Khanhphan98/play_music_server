import os.path
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import permission_classes, api_view
from mutagen.mp3 import MP3
from rest_framework.permissions import IsAuthenticated
from django.conf import settings

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
@permission_classes([IsAuthenticated])
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


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete_file(request):
    try:
        # init value
        file_path = request.data['path']
        path_root = os.path.join(settings.MEDIA_ROOT)

        # Kiểm tra xem file có tồn tại không
        if os.path.exists(f'{path_root}{file_path}'):
            # Delet file
            os.remove(f'{path_root}{file_path}')
            # Return
            return JsonResponse({"sucess": "Deleted file " + file_path}, status=200)
        # Return
        return JsonResponse({'error': 'Not found path file'}, status=400)
    except Exception as e:
        # Return
        return JsonResponse({'sucess': False, 'error': str(e)})
