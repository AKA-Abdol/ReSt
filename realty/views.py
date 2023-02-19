from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Realty
from .serializers import RealtySerializer

@api_view(["POST"])
def create_realty(request):
    data = request.data 
    serializer = RealtySerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)

@api_view(["GET"])
def get_all_realties(request):
    queryset = Realty.objects.all()
    data = RealtySerializer(queryset, many=True).data
    print(f'ins:{data}')
    return Response(data)