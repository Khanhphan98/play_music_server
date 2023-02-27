from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

urlpatterns = [
    # path('profession/create', create_profession),
    # path('profession/update/<index>', update_profession),
    # path('profession/delete/<index>', delete_profession),
    # path('profession/get-by-id/<index>', get_profession_by_id),
    # path('profession', ProfessionView.as_view()),
]

# View set
router = DefaultRouter()
router.register(r'profession', ProfessionViewSet)
router.register(r'singer', SingerViewSet)
urlpatterns += router.urls
