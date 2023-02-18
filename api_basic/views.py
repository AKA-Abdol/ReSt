from django.forms.models import model_to_dict
from .models import Product
import json

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer

@api_view(["GET"])
def test(request):
    try:
        body = json.loads(request.body)
    except:
        body = {'name': 'unknown'}
    instance = Product.objects.first()
    if(body['name'] == 'sehat'):
        data = ProductSerializer(instance).data
        return Response(data)
    else:
        return Response({'error':'unknown product'})
    