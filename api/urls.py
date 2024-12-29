from django.urls import path,include
from . import views

urlpatterns = [
    path('all-products/', views.ProductListCreateGenericView.as_view(), name='all-products')
]
