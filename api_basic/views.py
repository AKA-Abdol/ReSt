from django.forms.models import model_to_dict
from .models import Product
import json

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .serializers import ProductSerializer


@api_view(["GET"])
def test(request):
    try:
        body = json.loads(request.body)
    except:
        body = {'name': 'unknown'}
    instance = Product.objects.first()
    if (body['name'] == 'sehat'):
        data = ProductSerializer(instance).data
        return Response(data)
    else:
        return Response({'error': 'unknown product'})


@api_view(["POST"])
def add_product(request):
    data = request.data
    serializer = ProductSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        instance = serializer.save()
        print(f'ins:{instance}')
        res = serializer.data
        res['success'] = True
        return Response(res)
    else:
        print('Error')
        return Response({"error": "Fields not enough!"})


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


product_detail_view = ProductDetailAPIView.as_view()


class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        print(serializer.validated_data['title'])
        serializer.save()
        return Response({'success': True})


product_create_view = ProductCreateAPIView.as_view()

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

product_list_view = ProductListCreateAPIView.as_view()

@api_view(["GET"])
def get_below_price(request):
    data = request.data
    try:
        max_price = data['max']
    except:
        max_price = 101
    
    qs = Product.objects.all()
    ans = []
    for product in qs:
        if product.price < max_price:
            ans.append(product)
    return Response(ProductSerializer(ans, many=True).data)