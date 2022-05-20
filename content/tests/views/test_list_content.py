from django.test import TestCase
from content.models import Content
from django.urls.base import reverse
import json
from django.core.cache import cache as redis_cache
from content.serializers import ContentSerializer, ContentReadSerializer

class ListCatalogTest(TestCase):
    def setUp(self):
        # prepare user login, client or something
        pass

    def test_list_catalog_successful(self):
        # TODO: bulk create
        Content.objects.create(name="Name - 1", description="Description 1", catalog_id=1)
        Content.objects.create(name="Name - 2", description="Description 2", catalog_id=2)
        Content.objects.create(name="Name - 3", description="Description 3", catalog_id=3)
        Content.objects.create(name="Name - 4", description="Description 4", catalog_id=4)
        Content.objects.create(name="Name - 5", description="Description 5", catalog_id=5)

        # Update Redis
        redis_cache.set('content_list', ContentReadSerializer(Content.objects.all(), many=True).data)
        response = self.client.get(
            reverse('content_list'),
            content_type='application/json'
        )

        json_string = response.content
        response_data = json.loads(json_string)
        self.assertEqual(response.status_code, 200)

        self.assertEqual(len(response_data), 5)

        # TODO: Test Authentication, Permission, Authorization, Body Params, Response keys ...
