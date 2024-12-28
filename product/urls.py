from django.urls import path
from . import views


urlpatterns = [
    path('details/<int:pk>/', views.product_details, name='details' ),
    path('all_products/', views.all_products, name='all_products' ),
    path('add/', views.add_products, name='add_products' ),
    path('update/<int:pk>', views.update_product, name='update' ),
    path('delete/<int:pk>', views.delete_product, name='delete' ),

]
