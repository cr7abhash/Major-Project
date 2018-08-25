from rest_framework import serializers
from products.models import Product

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # field = ('id', 'product', 'customer')
        fields = '__all__'

