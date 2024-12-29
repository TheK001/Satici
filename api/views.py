from rest_framework import status, generics, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from product.models import Product
from .serializer import ProductOutSerializer, ProductCreateSerializer

# @api_view(["GET", "POST"])
# def list_product_api_view(request):
#     if request.method == 'GET':
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)    
#         return Response(serializer.data)
#     elif request.method == "POST":
#        serializer = ProductSerializer(data = request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response({"message": "elave olundu!"}, status=status.HTTP_201_CREATED)
#        return Response(status=status.HTTP_400_BAD_REQUEST)
    
class ProductListCreateView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductOutSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductCreateSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "elave olundu!"}, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
        
class ProductListCreateGenericView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductOutSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)