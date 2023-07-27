# flake8: noqa

from django.http import HttpResponse
from django.views import View
from django.views.generic.base import TemplateView
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view

from inventory.models import Cuvee, Vendor
from inventory.serializers import CuveeSerializer, CuveeListSerializer, VendorSerializer

class CuveeViewSet(viewsets.ModelViewSet):
    serializer_class = CuveeSerializer
    queryset = Cuvee.objects.all()
    http_method_names = ['get']


class VendorViewSet(viewsets.ModelViewSet):
    serializer_class = VendorSerializer
    queryset = Vendor.objects.all()
    http_method_names = ['get']


@api_view(('GET',))
class CuveeView(View):
    def get(self, request, *args, **kwargs):
        cuvee = Cuvee.objects.filter(id=kwargs['cuvee_id']).first()
        data = CuveeSerializer(cuvee).data
        content = {'data': data}
        return Response(content, status=status.HTTP_200_OK)
        # return HttpResponse(f'found cuvee {args} | {kwargs} | {cuvee} | {data}')


class CuveeListView(View):
    def get(self, request, *args, **kwargs):
        data = CuveeListSerializer(Cuvee.objects.all().order_by('id'), many=True).data
        return HttpResponse(data)


class VendorView(View):
    def get(self, request, *args, **kwargs):
        vendor = Vendor.objects.filter(id=kwargs['vendor_id']).first()
        data = VendorSerializer(vendor).data
        return Response(data)


class VendorListView(View):
    def get(self, request, *args, **kwargs):
        data = VendorSerializer(Vendor.objects.all().order_by('id'), many=True).data
        return HttpResponse(data)

