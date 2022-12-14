from django_filters import rest_framework as filter

from .models import Product

class PriductFilter(filter.FilterSet):
    class Meta:
        model = Product
        fields = ("status",)
    