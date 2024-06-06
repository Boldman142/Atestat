from rest_framework import serializers
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):

    author_first_name = serializers.CharField(source="author.first_name", read_only=True)
    author_last_name = serializers.CharField(source="author.last_name", read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
