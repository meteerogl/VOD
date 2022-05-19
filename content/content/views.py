from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from content.models import Content
from content.serializers import ContentSerializer
from django.core.cache import cache as redis_cache


# TODO: Write helper functions or decarator for update redis -> Maybe we can use core/redis_helper line of code are same :(
class ContentViewSet(viewsets.ViewSet):
    def list(self, request):
        redis_response = redis_cache.get('content_list')
        if redis_response is None:
            # Update Redis
            redis_cache.set('content_list', ContentSerializer(Content.objects.all(), many=True).data)
            return Response(redis_cache.get('content_list'))

        return Response(redis_response)

    def create(self, request):
        serializer = ContentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # Update Redis
        redis_cache.set('content_list', ContentSerializer(Content.objects.all(), many=True).data)
        return Response(serializer.data, status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        content = Content.objects.get(id=pk)
        serializer = ContentSerializer(content)
        return Response(serializer.data)

    def update(self, request, pk):
        content = Content.objects.get(id=pk)
        serializer = ContentSerializer(instance=content, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # Update Redis
        redis_cache.set('content_list', ContentSerializer(Content.objects.all(), many=True).data)
        return Response(serializer.data, status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk):
        content = Content.objects.get(id=pk)
        content.delete()
        # Update Redis
        redis_cache.set('content_list', ContentSerializer(Content.objects.all(), many=True).data)
        return Response(status.HTTP_204_NO_CONTENT)

