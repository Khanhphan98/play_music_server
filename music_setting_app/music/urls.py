from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

# View set
router = DefaultRouter()
router.register(r'profession', ProfessionViewSet)
router.register(r'singer', SingerViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'country', CountryViewSet)
router.register(r'song', SongViewSet)


urlpatterns += router.urls
