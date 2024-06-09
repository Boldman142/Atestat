from rest_framework import serializers
from sales_net.models import SalesNet
from products.serliazers import ProductSerializer


class SalesNetSerializer(serializers.ModelSerializer):

    author_first_name = serializers.CharField(source="author.first_name", read_only=True)
    author_last_name = serializers.CharField(source="author.last_name", read_only=True)
    product = ProductSerializer(many=True, required=False)
    supplier = serializers.SlugRelatedField(slug_field='title', queryset=SalesNet.objects.all())

    class Meta:
        model = SalesNet
        fields = '__all__'
