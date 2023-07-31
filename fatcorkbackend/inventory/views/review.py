# flake8: noqa

from rest_framework import status, viewsets


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    http_method_names = ['create', 'get', 'update', 'delete']
