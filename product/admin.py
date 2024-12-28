from django.contrib import admin
from product.models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "cost", "image"]
    list_display_links = ["id", "name"]

admin.site.register(Product, ProductAdmin)