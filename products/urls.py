from django.urls import include, path
from rest_framework.routers import DefaultRouter
from products.views import ProductViewSet
from products.apps import ProductsConfig

app_name = ProductsConfig.name

products_router = DefaultRouter()
products_router.register(r'products', ProductViewSet, basename='products')

urlpatterns = [
    path('', include(products_router.urls)),
]