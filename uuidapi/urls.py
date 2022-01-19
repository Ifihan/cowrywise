from django.urls import path
from .views import GetUUID

urlpatterns = [
    path("uuid/", GetUUID.as_view(), name='get_uuid'),
]
