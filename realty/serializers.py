from rest_framework import serializers
from .models import Realty


class RealtySerializer(serializers.ModelSerializer):
    price_per_sqft = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Realty
        fields = [
            'id',
            'title',
            'description',
            'bedrooms',
            'bathrooms',
            'sqft',
            'garage',
            'floor',
            'price',
            'realtor_id',
            'price_per_sqft'
        ]
    
    def get_price_per_sqft(self, obj):
        return obj.price / obj.sqft
