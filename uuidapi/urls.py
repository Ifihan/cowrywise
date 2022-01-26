from django.urls import path
from .views import GetUUID

urlpatterns = [
    path("", GetUUID.as_view(), name='get_uuid'),
]
