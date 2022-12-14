from rest_framework import serializers

from .models import Product

class ProductSrlz(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ("extension",)


class ProductListRetrieveSrlz(serializers.ModelSerializer):
    img_url = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = ("id", "title", "vendor_code", "price", "status", "img_url")
    
    def get_img_url(self, product):
        ex = product.extension
        path_url = (product.img.url).split(".")[0]
        return {"path": path_url, "formats": ["webt", ex]}


class ProductCreateSrlz(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = ("id", "title", "vendor_code", "price", "status", "url")
    
    def get_url(self, product):
        path_url = product.img.url
        return {"path": path_url}