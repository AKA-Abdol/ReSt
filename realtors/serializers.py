from rest_framework import serializers
from .models import Realtor

class RealtorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Realtor
        fields = [
            'id',
            'first_name',
            'last_name',
            'description',
            'email',
            'phone',
            'is_mvp',
            'hire_date'
        ]