from django.urls import path
from .views import *


urlpatterns = [
    path('profession/create', create_profession),
    path('profession/update/<index>', update_profession),
    path('profession/delete/<index>', delete_profession),
    path('profession/get-by-id/<index>', get_profession_by_id),
    path('profession/search', search_profession),
]