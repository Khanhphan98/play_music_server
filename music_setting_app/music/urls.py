from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf.urls.static import static
from django.conf import settings
from .until import upload_file, delete_file

urlpatterns = [
                  path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                  path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
                  path('upload_file/', upload_file, name='file'),
                  path('delete_file/', delete_file)
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# View set
router = DefaultRouter()
router.register(r'profession', ProfessionViewSet)
router.register(r'singer', SingerViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'country', CountryViewSet)
router.register(r'song', SongViewSet)

urlpatterns += router.urls
