from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    disc = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
            'sale_price',
            'disc'
        ]
    
    def get_disc(self, obj):
        return float(obj.price) * 0.15
