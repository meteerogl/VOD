from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from content.models import Content
from content.serializers import ContentSerializer


class ContentViewSet(viewsets.ViewSet):
    def list(self, request):
        contents = Content.objects.all()
        serializer = ContentSerializer(contents, many=True)
        return Response(serializer.data)

    def create(self, request):
        pass

    def retrieve(self, request):
        pass

    def update(self, request):
        pass

    def destroy(self, request):
        pass