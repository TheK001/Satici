from rest_framework import serializers
from product.models import Product

class ProductOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        read_only_fields = ["id",]

class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
