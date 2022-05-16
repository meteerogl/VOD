from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from content.models import Content
from content.serializers import ContentSerializer


class ContentViewSet(viewsets.ViewSet):
    def list(self, request):
        contents = Content.objects.all()
        serializer = ContentSerializer(contents, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ContentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        content = Content.objects.get(id=pk)
        serializer = ContentSerializer(content)
        return Response(serializer.data)

    def update(self, request):
        pass

    def destroy(self, request):
        pass