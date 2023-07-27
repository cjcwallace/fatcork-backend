# flake8: noqa
from rest_framework import serializers
from inventory.models import Cuvee, Vendor

class CuveeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuvee
        fields = ['id', 'name', 'activity_date', 'location']
        read_only_fields = fields


class CuveeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuvee
        fields = ['title', 'image_src']


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['name']
        read_only_fields = fields
