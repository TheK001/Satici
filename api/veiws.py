from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from product.models import Product
from .serializer import ProductSerializer

@api_view(["GET", "POST"])
def list_product_api_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)    
        return Response(serializer.data)
    elif request.method == "POST":
       serializer = ProductSerializer(data = request.data)
       if serializer.is_valid():
           serializer.save()
           return Response({"message": "elave olundu!"}, status=status.HTTP_201_CREATED)
       return Response(status=status.HTTP_400_BAD_REQUEST)