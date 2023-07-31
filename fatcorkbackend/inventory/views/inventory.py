# flake8: noqa

from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, views, viewsets
from rest_framework.response import Response

from inventory.models import Cuvee, Vendor
from inventory.serializers import CuveeSerializer, CuveeListSerializer, VendorSerializer

class CuveeViewSet(viewsets.ModelViewSet):
    """
    Do we need the view set? Cuvees should be fetched by users but not modified/created
    """
    serializer_class = CuveeSerializer
    queryset = Cuvee.objects.all()
    http_method_names = ['get']


class VendorViewSet(viewsets.ModelViewSet):
    """
    Do we need the view set? Vendors should be fetched by users but not modified/created
    """
    serializer_class = VendorSerializer
    queryset = Vendor.objects.all()
    http_method_names = ['get']


class CuveeView(views.APIView):
    @csrf_exempt
    def get(self, request, pk):
        try:
            cuvee = Cuvee.objects.get(id=pk)
        except Cuvee.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        data = CuveeSerializer(cuvee).data
        return Response(data, status=status.HTTP_200_OK)

class CuveeListView(views.APIView):
    @csrf_exempt
    def get(self, request):
        data = CuveeListSerializer(Cuvee.objects.all().order_by('id'), many=True).data
        return Response(data, status=status.HTTP_200_OK)


class VendorView(views.APIView):
    @csrf_exempt
    def get(self, request, pk):
        try:
            vendor = Vendor.objects.get(id=pk)
        except Vendor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        data = VendorSerializer(vendor).data
        return Response(data, status=status.HTTP_200_OK)

class VendorListView(views.APIView):
    @csrf_exempt
    def get(self, request):
        data = VendorSerializer(Vendor.objects.all().order_by('id'), many=True).data
        return Response(data)
