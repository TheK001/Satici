from django.urls import path,include


urlpatterns = [
    path('product/', include('api.urls'))
]