from django.contrib import admin
from django.urls import path, include
from .views import UserProfileViewSet


urlpatterns = [
    path('', UserProfileViewSet.as_view(), name='user-profile'),
]
