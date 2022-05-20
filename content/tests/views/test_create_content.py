from django.test import TestCase
from content.models import Content
from django.urls.base import reverse
import json


class ListCatalogTest(TestCase):
    def setUp(self):
        # prepare user login, client or something
        pass

    def test_create_content_successful_with_all_required_params(self):
        # Name and Description required but content_id(default=0)
        content_name = "Test Content"
        content_description = "Test Description"
        request_body = {
            "name": content_name,
            "description": content_description,
        }

        response = self.client.post(
            reverse('content_list'),
            request_body,
            content_type='application/json'
        )

        json_string = response.content
        response_data = json.loads(json_string)
        self.assertEqual(response.status_code, 201)

        self.assertEqual(Content.objects.all().count(), 1)

        self.assertEqual(Content.objects.all().first().name, content_name)
        self.assertEqual(Content.objects.all().first().description, content_description)
        self.assertEqual(Content.objects.all().first().catalog_id, 0)

    def test_create_content_failure_without_required_params(self):
        # Name and Description required but content_id(default=0)
        request_body = {
            "description": "Test Description",
        }

        response = self.client.post(
            reverse('content_list'),
            request_body,
            content_type='application/json'
        )

        json_string = response.content
        response_data = json.loads(json_string)
        self.assertEqual(response.status_code, 400)

        self.assertEqual(response_data, {'name': ['This field is required.']})
