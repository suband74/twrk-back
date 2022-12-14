from rest_framework.viewsets import GenericViewSet
from rest_framework import status
from rest_framework.response import Response
from pathlib import Path
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from .models import Product
from .serializers import ProductSrlz, ProductListRetrieveSrlz, ProductCreateSrlz


class CustomCreateModelMixin:
    def create(self, request, *args, **kwargs):
        suffix = Path(request.data["img"]._name).suffix
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        ins = Product.objects.create(**serializer.validated_data, extension=suffix[1::])
        serializer = ProductCreateSrlz(ins)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CustomRetrieveModelMixin:
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ProductListRetrieveSrlz(instance)
        return Response(serializer.data)


class CustomListModelMixin:
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = ProductListRetrieveSrlz(queryset, many=True)
        return Response(serializer.data)


class ProductViewSet(CustomCreateModelMixin,
                   CustomRetrieveModelMixin,
                   CustomListModelMixin,
                   GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSrlz
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ("status",)
    search_fields = ("vendor_code", "title")
