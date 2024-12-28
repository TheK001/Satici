from django.urls import path,include
from . import veiws

urlpatterns = [
    path('all-products/', veiws.list_product_api_view, name='all-products')
]
