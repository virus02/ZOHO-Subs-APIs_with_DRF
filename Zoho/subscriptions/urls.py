from django.urls import path
from .views import get_subs_list, get_subs_id

urlpatterns = [
    path('subslist', get_subs_list),
    path('subs_by_id', get_subs_id),
]