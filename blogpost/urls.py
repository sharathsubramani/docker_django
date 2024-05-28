from django.contrib import admin
from django.urls import path, include
from .views import BlogPostViewSet

urlpatterns = [
    path('', BlogPostViewSet.as_view(), name='blogs_post'),
]
