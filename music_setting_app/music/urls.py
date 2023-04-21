from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf.urls.static import static
from django.conf import settings
from .until import upload_file, delete_file
from .service import *

urlpatterns = [
  path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
  path('upload_file/', upload_file, name='file'),
  path('delete_file/', delete_file),
  # Song
  path('song/recent/', get_list_song),
  path('song/country/', get_list_song_by_country),
  path('song/exclude-country/', get_list_song_by_exclude_country),
  # Singer
  path('singer/recent/', get_list_singer),
  # Statistik
  path('statistik/singer/', get_singer_with_statistik),
  path('statistik/song/', get_song_with_statistik),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# View set
router = DefaultRouter()
router.register(r'profession', ProfessionViewSet)
router.register(r'singer', SingerViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'country', CountryViewSet)
router.register(r'song', SongViewSet)
router.register(r'user', UserViewSet)
router.register(r'statistik', StatistikViewSet)

urlpatterns += router.urls
