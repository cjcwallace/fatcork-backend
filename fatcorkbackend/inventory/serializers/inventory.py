# flake8: noqa
from rest_framework import serializers
from inventory.models import Cuvee, Vendor

class CuveeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuvee
        fields = ['id', 'title', 'vendor', 'type', 'vintage', 'see', 'smell', 'taste', 'pair']
        read_only_fields = fields


class CuveeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuvee
        fields = ['id', 'title', 'image_src']


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['id', 'name']
        read_only_fields = fields
