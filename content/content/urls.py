from django.contrib import admin
from django.urls import path

from content.views import ContentViewSet

urlpatterns = [
    path('contents', ContentViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='content_list'),
    path('contents/<str:pk>', ContentViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy',
    }), name='content')
]