from rest_framework import serializers
from .models import Content
from core.consumers.catalog_consumer import get_catalog_name_list


class ContentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Content
        fields = '__all__'

    def validate(self, data):
        #TODO: Nice to have -> When create content, control category id exist in category list
        return data


class ContentReadSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()

    class Meta:
        model = Content
        fields = ('id', 'category_name', 'created_at', 'updated_at', 'name', 'description')

    def get_category_name(self, obj):
        catalog_name_list = get_catalog_name_list()
        if catalog_name_list:
            return next(item for item in catalog_name_list if item["id"] == obj.catalog_id)['name']
        return None