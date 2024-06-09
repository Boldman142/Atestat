from django.urls import include, path
from rest_framework.routers import DefaultRouter
from sales_net.views import SalesNetViewSet
from sales_net.apps import SalesNetConfig

app_name = SalesNetConfig.name

salesnet_router = DefaultRouter()
salesnet_router.register(r'salesnet', SalesNetViewSet, basename='salesnet')

urlpatterns = [
    path('', include(salesnet_router.urls)),
]