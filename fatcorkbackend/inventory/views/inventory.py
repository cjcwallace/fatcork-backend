# flake8: noqa

from rest_framework import viewsets
from django.views.generic.base import TemplateView

from inventory.models import Cuvee, Vendor
from inventory.serializers import CuveeSerializer, VendorSerializer

class CuveeViewSet(viewsets.ModelViewSet):
    serializer_class = CuveeSerializer
    queryset = Cuvee.objects.all()
    http_method_names = ['get']


class VendorViewSet(viewsets.ModelViewSet):
    serializer_class = VendorSerializer
    queryset = Vendor.objects.all()
    http_method_names = ['get']
