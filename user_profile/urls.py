from django.contrib import admin
from django.urls import path, include
from .views import UserProfileViewSet, UserActivationSet


urlpatterns = [
    path('', UserProfileViewSet.as_view(), name='user-profile'),
    # path('<str:uid>/<str:uid_token>/',
    #      UserActivationSet.as_view(), name='user-activation')
]
